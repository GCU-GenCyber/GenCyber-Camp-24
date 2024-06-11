## Updating Your Docker Installation

Keeping your Open WebUI Docker installation up-to-date ensures you have the latest features and security updates. You can update your installation manually or use Watchtower for automatic updates.

### Manual Update

Follow these steps to manually update your Open WebUI:

#### 1. Pull the Latest Docker Image

First, you need to pull the latest image from the repository:

```bash
sudo docker pull ghcr.io/open-webui/open-webui:main
```

#### 2. Stop and Remove the Existing Container

Next, stop and remove the existing container to ensure you can create a new container from the updated image:

```bash
sudo docker stop open-webui
sudo docker rm open-webui
```

#### 3. Create a New Container with the Updated Image

Finally, create a new container using the updated image. Use the same `docker run` command you used initially to create the container, ensuring all your configurations remain the same:

```bash
sudo docker run -d -p 8080:8080 -v ollama:/root/.ollama -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:ollama
```
