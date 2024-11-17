## Introduction

This document consists of brief description of the five automated workflows created using N8N, a powerful workflow automation platform.

N8N platform is available as:
- Cloud service
- NPM module
- Docker image

For this demonstration, I've used Docker image to use N8N platform on localhost.

## Deployment of N8N using Docker

- Setup Docker on the machine https://docs.docker.com/engine/install/
- Verify that Docker engine and client are setup successfully
  
  ```bash
  docker --version # Displays Docker client version
  
  docker info # Displays Docker client and server version and status
  ```
- Start N8N by running below command

  ```bash
  docker run -it --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n docker.n8n.io/n8nio/n8n
  ```

  > This command will download all required n8n images and start the container, expose the n8n service on port `5678`. To save our work between container restarts, it also mounts a docker volume, `n8n_data`, to persist our data locally.

- Now we can access n8n by opening: http://localhost:5678
- When we launch n8n for the first time, it asks to enter some details. After that we can see the **Home** page.
- That's it, now we are ready to create workflows by clicking `Add Workflow` button, which navigate us to canvas, where we can add different kind of nodes one after another to create workflow.

## Workflows Demo

### JSON to CSV

- This workflow converts a JSON file to the CSV file.
- JSON file path need to be provided before executing the workflow by editing `Enter InputFile path here` node.

Workflow Screenshot:
![image](https://github.com/user-attachments/assets/0985e483-7e76-40bb-8294-2f0aa42bc1e9)

JSON and CSV File:
![image](https://github.com/user-attachments/assets/e97490a0-e746-4c6b-876b-04b59ac65764)

### RAM Usage

- This workflow fetches current RAM usage on every 5 seconds interval and saves to the Google sheet.

Workflow Screenshot:
![image](https://github.com/user-attachments/assets/e296218d-66bf-4aa8-942f-5d667a4005eb)

Google Sheet Data:
![image](https://github.com/user-attachments/assets/5ca94226-7154-47d9-99bf-7d0198dbd4f5)





