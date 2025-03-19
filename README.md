
# Rick and Morty Characters Service

This service provides information about characters from the Rick and Morty universe.

## CI/CD Workflow

The project uses GitHub Actions for continuous integration and deployment. The workflow is defined in `.github/workflows/test-deploy.yml`.

### Workflow Overview
- **Trigger**: Runs on push/PR to main branch
- **Environment**: Ubuntu latest

### Job Steps
1. **Checkout**: Clones the repository
2. **Minikube Setup**: 
   - Installs and starts Minikube
   - Enables ingress addon
3. **Helm Setup**: Installs Helm package manager
4. **Docker Build**:
   - Builds service image inside Minikube
   - Tags as rick-morty-service:latest
5. **Helm Deploy**:
   - Installs application using Helm chart
   - Waits for deployment rollout
6. **Testing**:
   - Waits for pods and ingress to be ready
   - Configures local DNS
   - Tests healthcheck and characters endpoints

### Local Testing
Follow these steps to test locally:

<<<<<<< HEAD
# rick-morty-characters
=======
---- Rick and Morty Characters Service ---- 
This service provides information about live human characters from Earth in the Rick and Morty universe.

1. Build the Docker image:
bash:
docker build -t rick-morty-service .


2. Run the container:
bash:
docker run -p 5000:5000 rick-morty-service

The service will be available at http://localhost:5000.

## REST API Endpoints

### 1. Health Check
- **Endpoint**: `/healthcheck`
- **Method**: GET
- **Description**: Checks if the service is running
- **Response Example**:
json:
{
    "status": "healthy",
    "message": "The service is running!"
}

### 2. Characters
- **Endpoint**: `/characters`
- **Method**: GET
- **Description**: Returns all live human characters from Earth
- **Response Example**:
json:
{
    "status": "successful",
    "message": "All the live human characters from Earth!",
    "count": 89,
    "characters": [
        {
            "name": "Rick Sanchez",
            "location": "Citadel of Ricks",
            "image": "https://rickandmortyapi.com/api/character/avatar/1.jpeg"
        },
        ...
    ]
}

## Testing the API

Curl to test the endpoints:

bash:
# Health check
curl http://localhost:5000/healthcheck

# Get characters
curl http://localhost:5000/characters



## Kubernetes Deployment
### Prerequisites
- Minikube installed
- kubectl configured

### Deployment Steps
1. Start your Kubernetes cluster (if using Minikube):
bash:
minikube start --driver=docker --kubernetes-version=v1.28.0


2. Enable the Ingress addon and verify:
bash:
minikube addons enable ingress
kubectl get pods -n ingress-nginx

3. Build the Docker image inside the minikube:
bash:
eval $(minikube -p minikube docker-env)
docker build -t rick-morty-service .

4. Apply the Kubernetes manifests:
bash:
kubectl apply -f yamls/deployment.yaml
kubectl apply -f yamls/service.yaml
kubectl apply -f yamls/ingress.yaml

5. Get Minikube's IP address:
bash:
export MINIKUBE_IP=$(minikube ip)
echo $MINIKUBE_IP

6. Add/update the following line in your /etc/hosts file:
bash:
echo "$MINIKUBE_IP rick-morty.local" | sudo tee -a /etc/hosts

7. Verify the hosts entry:
bash:
cat /etc/hosts | grep rick-morty.local

8. Access the service:
- Health check: http://rick-morty.local/healthcheck
- Characters: http://rick-morty.local/characters

Note: If you still can't access the service, try:
bash:
# Check if ingress controller is running
kubectl get pods -n ingress-nginx

# Verify your ingress configuration
kubectl describe ingress rick-morty-ingress

### Verify Deployment
Check the status of your deployment:
bash:
kubectl get pods
kubectl get services
kubectl get ingress



## Helm Deployment
### Prerequisites
- Helm 3.x installed
- Kubernetes cluster running (e.g., Minikube)
- kubectl configured

### Deployment Steps
1. Navigate to the helm directory:
```bash
cd helm
```

2. Install the Helm chart:
```bash
helm install rick-morty ./rick-morty-chart
```

3. To upgrade an existing deployment:
```bash
helm upgrade rick-morty ./rick-morty-chart
```

4. To uninstall the chart:
```bash
helm uninstall rick-morty
```

### Configuration
The following table lists the configurable parameters of the Rick and Morty chart and their default values:

| Parameter | Description | Default |
|-----------|-------------|---------|
| `replicaCount` | Number of replicas | `2` |
| `image.repository` | Image repository | `rick-morty-service` |
| `image.tag` | Image tag | `latest` |
| `image.pullPolicy` | Image pull policy | `Never` |
| `service.type` | Service type | `ClusterIP` |
| `service.port` | Service port | `80` |
| `service.targetPort` | Container port | `5000` |
| `ingress.enabled` | Enable ingress | `true` |
| `ingress.host` | Ingress host | `rick-morty.local` |

To override values during installation:
```bash
helm install rick-morty ./rick-morty-chart --set replicaCount=3
```


3. Test the deployment:
```bash
# Verify all resources are running
kubectl get pods
kubectl get services
kubectl get ingress

# Get Minikube IP and update hosts file (if not done already)
export MINIKUBE_IP=$(minikube ip)
echo "$MINIKUBE_IP rick-morty.local" | sudo tee -a /etc/hosts

# Test the endpoints
curl http://rick-morty.local/healthcheck
curl http://rick-morty.local/characters

# If you experience issues, check:
# Ingress controller status
kubectl get pods -n ingress-nginx

# Your specific release's ingress configuration
kubectl describe ingress rick-morty-rick-morty

# Pod logs
kubectl logs -l app=rick-morty-service
```

4. To upgrade an existing deployment:
```bash
helm upgrade rick-morty ./rick-morty-chart
```

5. To uninstall the chart:
```bash
helm uninstall rick-morty
```
>>>>>>> 49cf30a (Initial commit: Rick and Morty Characters Service)
