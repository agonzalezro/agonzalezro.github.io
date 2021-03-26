---
title: How to deploy and update a python app using Kubernetes
date: 2015-10-09
tags:
    - talks
    - python
    - kubernetes
---

Two days ago I gave a small talk in the [DJUGL (Django User Group London)](https://twitter.com/DJUGL) explaining how we could deploy a test application into Kubernetes. This post is going to explain something pretty similar, how to deploy a Flask app into Kubernetes and how to rolling update it.

Before starting, you can find all the materials of this post in my [k8s-py-example](https://github.com/agonzalezro/k8s-py-example) repo.

Download the app and build it twice, one for each of the version that you want to deploy. This versions will need to be tagged properly and sent to [Docker Hub](https://hub.docker.com/). Basically the steps to follow are:

    docker build -t agonzalezro/k8s-py-example .
    docker tag agonzalezro/k8s-py-example:latest agonzalezro/k8s-py-example:0.1
    # Change the code (src/app.py) a little bit to see the differences
    docker build -t agonzalezro/k8s-py-example .
    docker tag agonzalezro/k8s-py-example:latest agonzalezro/k8s/py-example:0.2
    docker push agonzalezro/k8s-py-example

Now that all the work related with Docker is done, let's take a look to the needed k8s files:

**rc-0.1.yml**
<script src="http://gist-it.appspot.com/http://github.com/agonzalezro/k8s-py-example/blob/master/rc-0.1.yml"></script>

**rc-0.2.yml**
<script src="http://gist-it.appspot.com/http://github.com/agonzalezro/k8s-py-example/blob/master/rc-0.2.yml"></script>

**service.yml**
<script src="http://gist-it.appspot.com/http://github.com/agonzalezro/k8s-py-example/blob/master/service.yml"></script>

The `rc` files are the definitions of your replication controllers, one of them using the version `0.1` and the other the image `0.2`. The service file is share since the application is going to be the same.

Let's run the first version of the app:

    kubectl -f rc-0.1.yml -f service.yml --validate=false
    # The validate tag is just needed because of a bug in current k8s

Now, if you do `kubectl get services` you will see the external IP of your service. You can use it to check that it's running and showing the code of the version `0.1`.

Cool! You have deployed your first k8s application, now, let's update it:

    kubectl rolling-update flaskapp-rc -f rc-0.2.yml

If you wait a little bit you will see in the logs what's happening there. Let the command finish and you will have your `0.2` version deployed having causing 0 downtime!

As always, feel free to contact me here or use twitter: [@agonzalezro](https://twitter.com/agonzalezro)
