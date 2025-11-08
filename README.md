# Hello Kubernetes (Python + Flask, Docker, Minikube)

A tiny Flask app running on Kubernetes. Demonstrates:
- Docker image build on Minikube’s daemon
- Deployment + Service (NodePort)
- ConfigMap-driven env config
- Downward API (pod & node name)
- Liveness/Readiness probes
- Resource requests/limits
- Scaling and rolling restarts

## Dependencies

Make sure the following tools are installed before starting:

| Dependency | Purpose | Check Installation |
|-------------|----------|--------------------|
| **Python 3.10+** | Run Flask app locally (optional) | `python3 --version` |
| **Docker / Docker Desktop** | Build container images | `docker --version` |
| **Minikube** | Run a local Kubernetes cluster | `minikube version` |
| **Kubectl** | Apply and manage Kubernetes manifests | `kubectl version --client` |
| **Git (optional)** | Version control and GitHub repo management | `git --version` |

💡 **Tip:** If you’re using Docker Desktop on Mac or Windows, ensure it’s running before starting Minikube.  
On Linux, you can install Docker Engine directly without Docker Desktop.

## Quick start
```bash
minikube start
eval $(minikube docker-env)
docker build -t flask-k8s:local ./app
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/configmap.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```
Retrive URL with: ```minikube -n hello-k8s service web-svc --url```

```bash
Open: ```$(URL)```
```

## Useful commands
```bash
# View all running pods, services, and deployments in the hello-k8s namespace
kubectl -n hello-k8s get pods,svc,deploy
# Scale the deployment up or down
kubectl -n hello-k8s scale deploy/web --replicas=4
#Restart all pods in the deployment (useful after changing config or image)
kubectl -n hello-k8s rollout restart deploy/web
# Stream logs from all pods in the deployment to check app output
kubectl -n hello-k8s logs deploy/web
```

## What I learned

- Built a small Flask service and containerized it

- Deployed with Deployment + Service and basic resource policies

- Managed config via ConfigMap; exposed pod metadata via Downward API

- Implemented health probes and performed rolling restarts