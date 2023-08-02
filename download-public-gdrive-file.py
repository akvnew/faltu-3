import requests

def download_public_file(file_id, destination_path):
    file_url = f"https://drive.google.com/uc?id={file_id}"
    response = requests.get(file_url)

    with open(destination_path, "wb") as f:
        f.write(response.content)
    print(f"Downloaded file to {destination_path}")

if __name__ == "__main__":    
    # https://drive.google.com/file/d/1wReO0ku60mg4wB04CTaJ/view?usp=drive_link
    download_public_file('1wReO0ku60mg4wB04CTaJ', 'file.ext')
