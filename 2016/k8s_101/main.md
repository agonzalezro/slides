# [fit] **kubernetes** 101
# [@agonzalezro](https://twitter.com/agonzalezro)

---

# [fit] What's Kubernetes?
> "Kubernetes is an open source orchestration system ~~for Rocket containers~~ for Docker containers."

^ Go to next

---

![](gifs/mindblown.gif)

^ Explain it here: deploy, optimize hw usage, scale...
^ Also says it runs everywhere

---

# [fit] **Concepts**

**NOTE:** all the names link to their documentation.

^ Introduce them as prerequisites

---

# [Pod](http://kubernetes.io/docs/user-guide/pods/)

![right fit original](images/forever-alone.png)

^ Pod is mortal (dixit)

^ Container vs Pod

---

# [Replication Controller](http://kubernetes.io/docs/user-guide/replication-controller/)

![right original](images/v.jpg)

^ Current state vs Desired state

---

# [Label](http://kubernetes.io/docs/user-guide/labels/)

![fit original](images/post-it.jpg)

^ Query them with selectors

---

# [Namespace](http://kubernetes.io/docs/user-guide/namespaces/)

![original right](images/buckets.jpg)

^ Multitenant || multiple k8s in 1 cluster

---

# [Service](http://kubernetes.io/docs/user-guide/services/)
### _ClusterIP_
### _NodePort_
### _LoadBalancer_

![original](images/door.jpg)

^ Logical set of Pods & policy to access to them

^ ClusterIP: internal IP only
^ NodePort: same port each node
^ LoadBalancer: cloud-provider dependent

---

# [Ingress](http://kubernetes.io/docs/user-guide/ingress/)

![](images/imaginarium.jpg)

^ In top of services
^ SSL termination, name base virtual hosting, url mux...

---

# [{~~scheduled~~,}Job](http://kubernetes.io/docs/user-guide/jobs/)

![left 100%](images/jt.png)

^ scheduled to be delivered with 1.2, but it didn't happen

---

# [Secrets](http://kubernetes.io/docs/user-guide/secrets/)

![](images/whisper.jpg)

^ tmpfs volume

^ Ex: keys to Docker registry

---

# [fit] New in **1.2**

---

# [DaemonSet](http://kubernetes.io/docs/admin/daemons/)

![right original 45%](images/one-and-only.jpg)

^ All (or some) nodes run 1 (and just one) copy of a pod

^ Ex: Datadog

---

# [Deploy (β)](http://kubernetes.io/docs/user-guide/deployments/)

![right](gifs/deploy.gif)

^ Declarative update for pods & RCs

^ Just describe desired state

---

# [ConfigMap](http://kubernetes.io/docs/user-guide/configmap/)

![fit](images/map.jpg)

^ Holds key-value pairs of configuration data that can be consumed

---

![](gifs/tired.gif)

---

# One more thing

---

# [Readiness & liveness probes](http://kubernetes.io/docs/user-guide/production-pods/#liveness-and-readiness-probes-aka-health-checks)

^ HTTP Get, TCP || Exec

---

# [fit] DEMO!
## DEMO!
### DEMO!

---

# AWS

    export AWS_DEFAULT_PROFILE=myawsprofile
    export KUBE_AWS_ZONE=eu-west-1c
    export MASTER_SIZE=m3.medium
    export NODE_SIZE=m3.medium
    ... # config/aws/default-config.sh
    export KUBERNETES_PROVIDER=aws; wget -q -O - https://get.k8s.io | bash
    
---

# or GKE

    gcloud config set project k8s-jobandtalent
    gcloud container clusters get-credentials cluster-1
    
---

# Cluster thingies

    kubectl cluster-info
    kubectl config view
    
---

# Your first cattle

    kubectl run nginx --image=nginx:1.9.12 # Thanks Kelsey!
    kubectl expose deployment nginx --port=80 --type=LoadBalancer

---

    kubectl get services
    <<<
    NAME         CLUSTER-IP     EXTERNAL-IP    PORT(S)   AGE
    kubernetes   10.3.240.1     <none>         443/TCP   25m
    nginx        10.3.247.144   146.148.8.48   80/TCP    1m 

---

    kubectl exec -it nginx...

---

# Let's yamlized it

    cat examples/k8s/*.yml
    
---

    kubectl create -f ... # Change ... for your yaml :)
    
---

# Rolling upgrade

    kubectl rolling-update hello-rc -f api-rc2.yml

---

# Or... (since 1.2)

    # edit file
    kubectl replace -f ... # where ... is your yaml

---

# And {auto,}scaling

    kubectl scale rc hello-rc --replicas=5
    kubectl autoscale rc hello-rc --min=X --max=Y

---

# [fit] Thanks!
# [@agonzalezro](https://twitter.com/agonzalezro)
