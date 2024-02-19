# Interviews

# TIACLOUD LAB

## You have 24hrs to complete the task. 24hrs starts from when you recieved the email from Akosua.

## Please DO the below Task to the best of your ability. Use the url Akosua gave you to access the lab. Build and Deploy ALL resources in the provisioned lab. Exercise WILL NOT be accepted if done in another environment. 
## All your relevant files should to created in the '/home/coder/project' directory


## Setup on your Lab

```
1. You have a running single node kind cluster
2. All work is to be done in the 'tiacourse' namespace
3. Docker, Helm, and kubectl is already installed
```

## Task Instructions - Do this in the 'tiacourse' namespace

```
Prequistes:

0.1: 'FORK' the below git repo
https://github.com/tiacloudconsult/interviews.git
0.2: In the '/home/coder/project' dicrectory of your lab environment, 'CLONE' your 'forked' repo.

Task:

The purpose of your task is to be able to reach your web-server application when we do a 'kubectl port-forward'

1. Python app exists in 'task/applications/python-app' directory. But the Dockerfile for it is empty (this can be found in the 'task/applications/docker' directory), write a Dockerfile for it and build the docker image. This will be used when deploying the application in the kind cluster later.
2. Similarly, the deployment yaml file is empty (this can be found in the 'task/applications/k8s' directory). Write the deployment yaml so it can be used in the below tasks. The deployment yaml MUST have '2' replicas for the pod, and a rolling update strategy feature.

3. Deploy ArgoCD using the manifest file in task/argo-install.yaml - do this in the 'tiacourse' namespace
4. In the 'task/applications/argocd-app' directory, write an ArgoCD application manifest to deploy the application in the 
'task/applications/k8s/' directory to your kind cluster. Bonus points if you add some interesting sync policies
5. A lovely documentation of your process is welcomed. (Optional)
6. Commit and push all work done to your forked repository
```

# Submit a url of your forked repo to the below emails, so we can review your work. Make sure it is a public repo

```
francis.poku@tiacloud.io, sharhan.alhassan@tiacloud.io, akosua.nyarko@tiacloud.io
```
