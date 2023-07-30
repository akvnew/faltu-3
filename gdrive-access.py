from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os

# If modifying these scopes, delete the file token.json.
OAUTH2_CLIENT_SECRET_FILE = 'client_secret.json'
SCOPES = ['https://www.googleapis.com/auth/drive']

def get_credentials(token_file='token.json', scopes=None, oauth2_client_secret_file=None):
    creds = None
    if os.path.exists(token_file):
        creds = Credentials.from_authorized_user_file(token_file, scopes)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                oauth2_client_secret_file, scopes)
            creds = flow.run_local_server(port=4000)
        with open(token_file, 'w') as token:
            token.write(creds.to_json())
    return creds

def download_file(service, file_id, destination_path):
    request = service.files().get_media(fileId=file_id)
    with open(destination_path, 'wb') as f:
        downloader = MediaIoBaseDownload(f, request)
        done = False
        while not done:
            _, done = downloader.next_chunk()

def download_folder(service, folder_id_to_download, destination_folder):    
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    results = service.files().list(
        q=f"'{folder_id_to_download}' in parents",
        fields="files(id, name, mimeType)").execute()
    items = results.get('files', [])
    for item in items:
        item_id = item['id']
        item_name = item['name']
        print(item_name)
        item_mimeType = item['mimeType']
        item_destination = os.path.join(destination_folder, item_name)

        if item_mimeType == 'application/vnd.google-apps.folder':
            os.makedirs(item_destination, exist_ok=True)
            download_folder(service, item_id, item_destination)
        else:
            download_file(service, item_id, item_destination)

    print("Download complete.")

def upload_folder(service, folder_path, parent_folder_id=None):
    folder_name = os.path.basename(folder_path)

    file_metadata = {
        'name': folder_name,
        'mimeType': 'application/vnd.google-apps.folder'
    }
    if parent_folder_id:
        file_metadata['parents'] = [parent_folder_id]

    folder = service.files().create(body=file_metadata, fields='id').execute()
    folder_id = folder.get('id')

    for item in os.listdir(folder_path):
        print(item)
        item_path = os.path.join(folder_path, item)
        if os.path.isfile(item_path):
            file_metadata = {
                'name': item,
                'parents': [folder_id]
            }
            media = MediaFileUpload(item_path)
            service.files().create(body=file_metadata, media_body=media).execute()
        elif os.path.isdir(item_path):
            upload_folder(service, item_path, parent_folder_id=folder_id)
    
    print("Upload complete.")

def main():

    service = build('drive', 'v3', credentials=get_credentials(
        scopes=SCOPES,
        oauth2_client_secret_file=OAUTH2_CLIENT_SECRET_FILE
    ))

    download_folder(service, '19CnUnM4Q17MmzhuQOFSZ6TblJ8rjfLI5', 'Site Uploaded')
    # upload_folder(service, 'Site Uploaded')

if __name__ == '__main__':
    main()
