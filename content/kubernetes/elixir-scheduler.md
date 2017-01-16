date: 2017-01-16
tags: elixir, scheduler, kubernetes

Scheduling Your Kubernetes Pods With Elixir
===========================================

> This was originally posted on [deis.com](https://deis.com/blog/2016/scheduling-your-kubernetes-pods-with-elixir/).

[Kelsey Hightower](https://twitter.com/kelseyhightower) gave a really interesting talk at [ContainerSched](https://skillsmatter.com/conferences/7208-containersched-2015) about how to create your own scheduler using the Kubernetes HTTP API.

The talk was awesome. It's incredible to see what kind of things you can do with a base system as good as Kubernetes.

However, I missed one thing. The [example](https://github.com/kelseyhightower/scheduler) provided by Kelsey was a Go application. Which is the main language used with Kubernetes. So, if you look at that code without any context, you might think it's using some kind of Kubernetes internal packages. But it's not! It's a standalone piece of code that happens to make some HTTP calls.

To illustrate this point, I decided to write my own scheduler, in a different language. In my case, [Elixir](http://elixir-lang.org/), because that's the language I happen to be learning at the moment.

This post isn't an intro to Elixir, but the code should be easy to follow.

Also, I'm going to use `localhost` when accessing the Kubernetes API. Why? For simplicity. If we run `kubectl proxy` on a computer connected to the Kubernetes master, we will not need to deal with authorization, hosts, and so on. The `proxy` command will do it for us.

So, let's dive in.

Get a List of Unscheduled Jobs
------------------------------

To start off with, we need a pod for our scheduler to schedule.

By default, Kubernetes will schedule all your pods. So, we need to create a unscheduled pod and we need to indicate to Kubernetes that we don't want our pod to get scheduled.

So, create a file called `pod.yml` and put this inside:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: custom
  annotations:
    scheduler.alpha.kubernetes.io/name: myOwnScheduler
spec:
  containers:
    - name: "nginx"
      image: "nginx:1.10.0"
```

Notice the `scheduler.alpha.kubernetes.io/name` annotation we use to specify that our scheduler (that we call `myOwnScheduler`) will be handling this pod.

Now, let's create the pod from the definition file:

```bash
kubectl create -f pod.yml
``` 

After you've done this, there will be an unscheduled job waiting for us inside Kubernetes. Why unscheduled? Because our pod says it wants to be scheduled by the `myOwnScheduler` scheduler, but we've not created it yet, so Kubernetes can't schedule it.

So, let's build our scheduler.

First, our scheduler must be able to grab this unscheduled job from the API.

Here's the function I wrote to do that:

```elixir
def unscheduled_pods do
  is_managed_by_us = &(get_in(&1, ["metadata", "annotations", "scheduler.alpha.kubernetes.io/name"]) == @name)

  resp = HTTPoison.get! "http://127.0.0.1:8001/api/v1/pods?fieldSelector=spec.nodeName="
  resp.body
  |> Poison.decode!
  |> get_in(["items"])
  |> Enum.filter(is_managed_by_us)
  |> Enum.map(&(get_in(&1, ["metadata", "name"])))
end
```
 
As you can see we are using `127.0.0.1` to query our API, this is posible thanks to the `kubectl proxy` command we mentioned in the intro.

This code grabs the name of all the pods that are waiting to be scheduled inside Kubernetes. It then uses the `is_managed_by_us` function to see whether the `@name` attribute is set to `myOwnScheduler`. If this is true, the pod has indicated that it should be managed by our scheduler.

An Elixir Introduction
----------------------

I said I wouldn't explain Elixir, but I will just comment on three piece of syntax.

The `|>` in the code above is a pipe, like the `|` character from a shell script. Using this passes the result from the left side as a parameter to the function on the right side. In this way return values can be piped through functions.

The `&` character marks an [anonymous function](https://en.wikipedia.org/wiki/Anonymous_function), i.e. a function that we define inline as an expression. And `&1` refers the first parameter received by the function.

We can also use an anonymous function as parameter to another function. As we are doing, in the `map` call.

Get a List of Available Nodes
-----------------------------

Our `unscheduled_pods` function gets us a list of pods that have not been scheduled yet. So next up, we can bind them to our nodes. That is, we tell our containers to run on particular nodes.

But wait, how do we know what nodes are available?

We'll need to grab those as well, like this:

```elixir
def nodes do
  resp = HTTPoison.get! "http://127.0.0.1:8001/api/v1/nodes"
  resp.body
  |> Poison.decode!
  |> get_in(["items"])
  |> Enum.map(&(get_in(&1, ["metadata", "name"])))
end
```

This code will return a list of all nodes.

We could potentially request a lot more information from the API at this point, but for what we're building, it's not necessary. If you want to now what extra information is available, [check the documentation for this endpoint](http://kubernetes.io/kubernetes/third_party/swagger-ui/#!/api%2Fv1/listNamespacedNode).

The Bind Function
-----------------

So let's review.

We have a list of all the unscheduled jobs that we are supposed to manage. And we have a list of all the nodes we can schedule jobs to.

But how do we actually schedule a pods on a node?

We call the bind endpoint, like this:

```elixir
def bind(pod_name, node_name) do
  url = "http://127.0.0.1:8001/api/v1/namespaces/default/pods/#{pod}/binding"
  payload = %{
    "apiVersion": "v1",
    "kind": "Binding",
    "metadata": %{
      "name": pod_name,
    },
    "target": %{
      "apiVersion": "v1",
      "kind": "Node",
      "name": node_name,
    }
  }
  headers = [{'content-type', 'application/json'}]

  HTTPoison.post! url, payload |> Poison.encode!, headers
  IO.puts "#{pod_name} pod scheduled in #{node_name}"
end
```

But before we can use this function, we need a scheduling strategy.

Scheduling Strategy
-------------------

For our simple scheduler, we will go with a random scheduling strategy.

In effect, we schedule each pod on a random node. Multiple pods might even end up on the same node.

Here's how we do that:

```elixir
def schedule(pods) do
  pods
  |> Enum.each(&(bind(&1, Enum.random(nodes))))
end
```

Of course, this is very basic, and there are much better ways to maximise the resources we have available to us. But we're building this as a learning exercise. Feel free to extend this code if you want to take things further.

Some ideas to get you going:

- [Round-robin](https://en.wikipedia.org/wiki/Round-robin_scheduling) pod scheduling.
- Implement your own version of Kubernete's load-aware scheduling.
- Annotate the pods with some extra information, for example: cluster.type: raspberry if you want to send them to the Raspberry Pi nodes in your cluster.
- You could use some external source of truth, e.g. Nagios, to determine which nodes to schedule jobs on.

Putting Everything Together
---------------------------

Now we have everything in place, a `main` function is all that's needed:

```elixir
def main(_args) do
  unscheduled_pods
  |> schedule
end
```

Now you are able to run your program!

A simple `elixir your_script.exs` should do it, if you have all the dependencies. But you probably don't, so I recommend you follow the Usage section in [the README](https://github.com/agonzalezro/escheduler#usage) for the code that accompanies this post.

Wrap Up
-------

For a most things, you probably don't want to write your own scheduler. The one provided by Kubernetes is good for so many things.

But if you want to do something the default Kubernetes scheduler can't do, it's not as difficult as you might think to write your own and slot it in, and continue to take advantage of everything Kubernetes has to offer.

I've put my code up for [my Elixir scheduler](https://github.com/agonzalezro/escheduler), on GitHub in case you want to check it out. This repository has everything you need to follow along with this post, from the YAML pod definition to the scheduler itself.
