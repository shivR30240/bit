I built and deployed a basic Hello World Program with a focus on automating the development-to-deployment workflow. 
I containerized the application using Docker to ensure consistency across environments and deployed it on Google Cloud Platform (GCP).

For secure deployment, I used SSH access with public-private key authentication instead of passwords. 
I configured the VM instance on GCP, managed access through SSH keys, and handled the deployment process remotely.

I also implemented a CI/CD pipeline using GitHub Actions to automate the build and deployment process. 
This included setting up GitHub Secrets to securely store sensitive information like SSH private keys and server credentials. 
The pipeline automates steps like installing dependencies, building the Docker image, and deploying it to the cloud environment, eliminating the need for repetitive manual setup.
Additionally, I integrated Nginx as a reverse proxy to manage incoming traffic and route requests to the application running on different ports.
I explored basic load balancing concepts by distributing traffic across services and handling port configurations efficiently.

Overall, this project helped me gain hands-on experience with Docker, cloud deployment, secure authentication, and workflow automation using CI/CD practices.
