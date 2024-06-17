## Introduction
This guide provides step-by-step instructions for installing Open WebU on a Windows operating system using WSL and Docker.

## Step 1: Install WSL
1. Open PowerShell as Administrator.
2. Install WSL using the following command:
   ```sh
   wsl --install
   ```
3. If Ubuntu is not installed automatically, install it with:
   ```sh
   wsl --install -d Ubuntu
   ```

## Step 2: Set Up Ubuntu in WSL
1. Launch Ubuntu from the Start menu.
2. Update the package list and install updates:
   ```sh
   sudo apt update && sudo apt upgrade -y
   ```

## Step 3: Install Docker
1. Install Docker using Snap:
   ```sh
   sudo snap install docker
   ```
2. Verify Docker installation:
   ```sh
   docker -v
   ```

## Step 4: Run Open WebU with Docker
1. Pull the Open WebU Docker image and run the container:
   ```sh
   sudo docker run -d -p 8080:8080 -v ollama:/root/.ollama -v open-webui:/app/backend/data --name open-webui ghcr.io/open-webui/open-webui:ollama
   ```
2. Check if the container is running:
   ```sh
   sudo docker ps
   ```

## Step 5: Access Open WebU
1. Open a web browser.
2. Navigate to `http://localhost:8080` to access Open WebU.

## Troubleshooting
- If you encounter any issues during installation, check the following:
  - Ensure that WSL and Docker are installed correctly.
  - Ensure that you have an active internet connection.
  - Check the Docker logs for any errors:
    ```sh
    sudo docker logs open-webui
    ```

## Contributing
If you have suggestions for improving this guide, please open an issue or submit a pull request.
