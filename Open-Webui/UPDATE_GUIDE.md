## Updating Your Docker Installation

Keeping your Open WebUI Docker installation up-to-date ensures you have the latest features and security updates. You can update your installation manually or use Watchtower for automatic updates.

### Manual Update

Follow these steps to manually update your Open WebUI:
allways update your system before installation: 

```bash
sudo apt udate
```
It will ask for the password. The password won't be visible as you type, but don't worry, it is being entered. Press Enter once you have input your password.

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

Finally, create a new container using the updated image. This will update Open WebUI with the local port changed to 8080. Use the following command, ensuring all your configurations remain the same:
```bash
sudo docker run -d -p 8080:8080 -v ollama:/root/.ollama -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:ollama
```

##### 4. change the URL

http://localhost:8080

#### 5. change the clipboard permission

on a seperate tab search about:config accept the risk and continue. Search clipboard on the search bar and copy the screenshot.

![config](https://github.com/GCU-GenCyber/GenCyber-Camp-24/assets/117708036/952be693-78b5-4ec7-9706-59879cb1f80c)





