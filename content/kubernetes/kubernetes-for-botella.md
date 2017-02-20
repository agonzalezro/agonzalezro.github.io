date: 2017-02-20
tags: botella, kubernetes, plugin, go, elixir, slack

Write your Kubernetes's Slack bot with Botella (Go) & Elixir
============================================================

Before you continue reading the post I want to clarify that the ideas on it are not applicable just to Elixir, Kubernetes, Go or Elixir. If you want to write your Slack bot, for example, to send some fortune cookie messages to your channels and you write to write it with RUby this post will help you as well.

Let me start introducing you to [Botella](https://agonzalezro.github.io/botella/), Botella is something similar to a bot "framework" written in Go that provides you with an easy way to run a bot in Slack and develop your own plugins with the help of Docker. Basically, Botella is the Slack sender/receiver and it will call your Docker plugins making use of the stdin/stdout of your Docker container. This means that if you want to write a plugin you will expect a json line and you will just write to stdout whatever you want to be a response, or nothing if you don't want to handle that message with this plugin.

After the presentations are made I am going to list what I will explain you in this post:

1. How to write a small bot that receives stdin message and answer to them.
2. How to make that bot use the Kubernetes API.
3. How to deploy that bot in Kubernetes.

Let's go for it!

Ping handler
------------

For educational purposes we will start writing a simple ping/pong bot. As I said the bot is going to be written with Elixir, but don't worry, the code is going to be extremely simple. I am not an expert either, so feel free to review my code.

We will need to handle the input to know if we should reply to a ping, or not. The plugin will receive all the message in the channels were the bot is [unless you say the opposite](https://github.com/agonzalezro/botella#usage):

```elixir
defmodule Mix.Tasks.Bot.Run do
  def run(_) do
    HTTPoison.start
    IO.gets("") |> Bot.parse |> IO.puts
  end
end


defmodule Bot do
  def get_handler(body) do
    cond do
      ~r/ping$/ |> Regex.match?(body) ->
        {:ok, &Handler.ping/0}
      true ->
        {:nothandled, &Handler.nop/0}
    end
  end

  def parse(line) do
    case Poison.decode(line) do
      {:ok, payload} ->
        {_, f} = get_handler(payload |> Map.get("body"))
        f.()
      {:error, _} -> ""
    end
  end
end

defmodule Handler do
  def ping do
    "pong"
  end

  def nop do
  end
end
```

Few things are happening here:

1. We are defining a new task that is going to be something like the `main`. This task will read a line `IO.puts` and pipe it to our bot.
2. Our bot will try to understand it in the `parse` function. To understand it, it should receive a JSON with a `body` key.
3. It will try to get a handler for that `body` and as it always will get one (in case that nothing matches `noop` is returned) it will call the function.
4. The function `ping` will just return `pong`, so going back to the `main` task we see that this string will be `IO.puts`'d to stdout.

Talking with the Kubernetes API
-------------------------------

### First steps

We have several ways to connect to the Kubernetes apiserver. Probably, the most reliable one that I know at the moment is using your file `$HOME/.kube/config` and the Go client. But we are not doing that (kinda).

Another option is using the files under `/var/run/secrets/kubernetes.io/serviceaccount/token` (which are just secrets mounted as a filesystem). However, I have bad and good news for you, the bad news are that since the Botella plugins are running in containers inside your Pod containers (containerception) you can't access those files, the good news are that we still have hope.

So, what do we need to access the API?

- The token that we are able to copy/paste it from any of the above methods or just running (if you are in minikube):

```bash
kubectl describe secret $(kubectl get secrets | grep default | cut -f1 -d ' ') | grep -E '^token' | cut -f2 -d':' | tr -d '\t'
```
- And the server host.

You can simplify all the previous process while you are developing just using the `kubectl proxy` which will deal with auth for you.

### Developing the client

We will take advantage of mix configurations and setup two configurations to our app that are going to be set via environment variable: `token` & `apiserver`. With that we have all we need (if you don't use ceritificates) to connect to the API:

```elixir
defmodule Kubernetes do
  def headers do
    token = Application.get_env(:bot, :token)
    ["Authorization": "Bearer #{token}"]
  end

  def get(resource) do
    apiserver = Application.get_env(:bot, :apiserver)
    {:ok, response} = HTTPoison.get("#{apiserver}/api/v1/#{resource}", headers(), hackney: [:insecure])
    response.body
  end

  def pods do
    get("pods")
  end
  
  ...
```

This snippet is straight forward. We do a request to the API adding the authentication headers. Now we just need to make them interact with the world. Do you remember where we where checking for `ping` as an input? Now we have another input:

```elixir
      ~r/get pods/ |> Regex.match?(body) ->
        {:ok, &Handler.get_pods/0}
```

And the handler for it:

```elixir
defmodule Handler do
  @kubernetes_client Application.get_env(:bot, :kubernetes_client)

  def get_pods do
    pods = @kubernetes_client.pods
    |> Poison.decode!
    |> Map.get("items")
    |> Enum.map(&(get_in(&1, ["metadata", "name"])))
    |> Enum.join(", ")
    "Your running pods are: #{pods}"
  end

  ...
```
 

Do you see what I did there? Whenever the `body` matches with "get pods" I will use the `@kubernetes_client` to ask for the pods and return them formated.

If you are interested about testing, take a look to why I am using `@kubernetes_client` there. [Here you have a clue](https://github.com/agonzalezro/kubernetes-for-botella/blob/master/config/test.exs#L4).

Deploy to Kubernetes
--------------------

TBD

Next steps
----------

It would be cool to add some useful functions to this bot and perhaps make it an standard implementation for botella. However, I am not 100% sure yet that an agnostic bot for Kubernetes would be that helpful out of a nice POC, I see far much more utility in a bot that can connect to your private github repos, create a helm package and deploy it, basically you could be doing deployment from Slack while you have a pint of beer in a pub (been there, done that).

If you have any comment or concern use the comments section or [just ping me on twitter](https://twitter.com/agonzalezro)!
