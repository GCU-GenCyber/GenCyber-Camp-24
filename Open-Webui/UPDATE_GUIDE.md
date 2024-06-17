## Updating Your Docker Installation

Keeping your Open WebUI Docker installation up-to-date ensures you have the latest features and security updates.

### Manual Update

Follow these steps to manually update your Open WebUI:

#### 1. Update Your System

Always update your system before any installation:

```bash
sudo apt update
```

You will be prompted for your password. The password won't be visible as you type, but don't worry, it is being entered. Press Enter once you have input your password.

#### 2. Pull the Latest Docker Image

First, pull the latest image from the repository:

```bash
sudo docker pull ghcr.io/open-webui/open-webui:main
```

#### 3. Stop and Remove the Existing Container

Next, stop and remove the existing container to ensure you can create a new container from the updated image:

```bash
sudo docker stop open-webui
sudo docker rm open-webui
```

#### 4. Create a New Container with the Updated Image

Finally, create a new container using the updated image. This will update Open WebUI with the local port changed to 8080. Use the following command, ensuring all your configurations remain the same:

```bash
sudo docker run -d -p 8080:8080 -v ollama:/root/.ollama -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:ollama
```

#### 5. Access Open WebUI

Change the URL to:

[http://localhost:8080](http://localhost:8080)

#### 6. Change the Clipboard Permission

On a separate tab in your browser, navigate to `about:config`. Accept the risk and continue. Search for `clipboard` in the search bar and copy the screenshot below:

![config](https://github.com/GCU-GenCyber/GenCyber-Camp-24/assets/117708036/952be693-78b5-4ec7-9706-59879cb1f80c)

