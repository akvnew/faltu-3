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

## Workflows

### 1. JSON to CSV

- This workflow converts a JSON file to the CSV file.
- JSON file path need to be provided before executing the workflow by editing *Enter InputFile path here* node.

Workflow Screenshot:

![image](https://github.com/user-attachments/assets/0985e483-7e76-40bb-8294-2f0aa42bc1e9)

JSON and CSV File:

![image](https://github.com/user-attachments/assets/e97490a0-e746-4c6b-876b-04b59ac65764)

### 2. RAM Usage

- This workflow fetches current RAM usage of the n8n hosting machine on every 5 seconds interval and saves to the Google sheet.
- I've used *Execute Command* node to execute `cat /proc/meminfo` command to fetch the RAM usage.

Workflow Screenshot:

![image](https://github.com/user-attachments/assets/e296218d-66bf-4aa8-942f-5d667a4005eb)

Google Sheet Data:

![image](https://github.com/user-attachments/assets/5ca94226-7154-47d9-99bf-7d0198dbd4f5)

### 3. Daily Weather Report

- This workflow sends message on Slack everyday 6 AM to notify about weather of that day by fetching weather data from OpenWeatherMap API.

Workflow Screenshot:

![image](https://github.com/user-attachments/assets/18d1a30e-8fb8-4f76-87fe-68553ab1462e)

Slack Message:

![image](https://github.com/user-attachments/assets/c9f218ef-30bf-4b7d-84db-258b1f8f4efc)

### 4. Website Health Check

- This workflow checks health of a website by hitting its url on 5 minutes interval.
- If the status code is NOT `OK` (statusCode < 299) for consecutive 3 times, it will send a slack notification.
- To store the state i.e. current count of consective NOT OK status, I've used *Read/Write Files from Disk* node to save the count in a file and read it in next runs.

Workflow Screenshot:

![image](https://github.com/user-attachments/assets/e5d8394d-a419-4c7f-9b92-54e1bbdaa39f)

Slack Notification on Alarm:

![image](https://github.com/user-attachments/assets/c98f2e72-74ae-4008-87c1-b58d3b2356b4)

### 5. Google Form New Complaint Notification

- This workflow send notification on Slack when a new complaint is registered on the Google Form.
- On Google Form submission, one row is added in the Google sheet, and this workflow works on Google sheet trigger *rowAdded*.

Workflow Screenshot:

![image](https://github.com/user-attachments/assets/2f67f50d-047a-4ed1-b8a4-d0a6264f8838)

Google Form:

![image](https://github.com/user-attachments/assets/58aea494-1f57-42ab-8726-a3087458fbf7)

Slack Notification:

![image](https://github.com/user-attachments/assets/ab18347a-5941-48c5-a1e1-382e9e505a36)
