# Rick and Morty Characters Service
This service provides information about characters from the Rick and Morty universe including their image, name and location (by default).

## Auto CI/CD Workflow
The project uses GitHub Actions for continuous integration and deployment.
The workflow is defined in `.github/workflows/test-deploy.yml` directory.

    ### Overview
    - Trigger: Runs on push to main branch
    - Environment: Ubuntu

    ### Job Steps
    1. Clone of the repository
    2. Deploy Minikube: 
        - Install and start Minikube
        - Enables ingress addon
    3. Helm Setup:
        - Installs Helm package manager
    4. Docker Build:
        - Builds image inside Minikube
        - Tag as rick-morty-service:latest
    5. Deploy Helm:
        - Install app using the Helm chart
    6. Testing:
        - Wait for pods and ingress to be up adn ready
        - Configure local DNS (/etc/hosts)
        - Test /healthcheck and /characters endpoints

**************************************************************************************

## Local Testing
Steps and commands for local testing:

    ### Prerequisites
    - Minikube installed
    - kubectl configured
    - Helm 3.x installed

    ### Deployment Steps
    1. Start your Kubernetes cluster (if using Minikube):
        minikube start --driver=docker --kubernetes-version=v1.28.0
    2. Enable the Ingress addon and verify:
        minikube addons enable ingress
        kubectl get pods -n ingress-nginx
    3. Build the Docker image inside the minikube:
        eval $(minikube -p minikube docker-env)     # point insdie the minikube
        docker build -t rick-morty-service .
    4. Navigate to the helm directory:
        cd helm
    5. Install/upgrade the Helm chart:
        helm install rick-morty ./rick-morty-chart      #for new installation
        helm upgrade rick-morty ./rick-morty-chart      #for updating existing one
    6. Test the deployment:
        kubectl get pods        # Verify all pods are running
        kubectl get services    # Verify all services are running
        kubectl get ingress     # Verify all ingress are running
    7. Retrive the Minikube IP and update /etc/hosts
        export MINIKUBE_IP=$(minikube ip)
        echo "$MINIKUBE_IP rick-morty.local" | sudo tee -a /etc/hosts
    8. Test the endpoints
        curl http://rick-morty.local/healthcheck
        curl http://rick-morty.local/characters