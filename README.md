# Docker stuff
From `final_project` directory, run `docker-compose up`

# Kubernetes stuff
```
$ kind create cluster --name final
```

```
$ kubectl config use-context kind-final
```

Note: v1 loads templates into Docker image, v2 doesn't
```
$ docker build . -t final:v2
```

```
$ kind load docker-image final:v2 --name final
```

From project root, 
```
$ kubectl apply -f k8s/
```

```
$ kubectl port-forward svc/web 8000:8000
```

# Things accomplished
- Fastapi server with 
    - home page
    - create course page
    - add course route
    - drop course route
- Docker image built with Dockerfile + run with docker-compose
- Same app deployed on `kind` with templates mounted as config maps

