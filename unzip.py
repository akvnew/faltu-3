import zipfile
import os
import pathlib
import shutil

def extract_zip(zip_file_path, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
        zip_file.extractall(destination_folder)

def list_zip_files(directory):
    zip_files = []
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path) and filename.lower().endswith('.zip'):
            zip_files.append(file_path)
    return zip_files

def get_list_of_files_in_dir(directory):
    all_files = []
    for dir, subdirs, files in os.walk(directory):
        for file in files:
            all_files.append({'file_name':file, 'path':os.path.join(dir, file)})

def move_file(source_file_path, destination_file_path):
    try:
        shutil.move(source_file_path, destination_file_path)
    except Exception as e:
        print(f"Error while moving the file {source_file_path} to {destination_file_path}: {e}")


def unzip_files(directory):
    zip_files = list_zip_files(directory)
    for zip_file in zip_files:
        print(zip_file)
        destination_folder = '.'.join(zip_file.split('.')[:-1])
        extract_zip(zip_file, destination_folder)
        files_list = get_list_of_files_in_dir(destination_folder)
        if len(files_list) == 1:
            move_file(files_list[0]['path'], os.path.join(directory, files_list[0]['file_name']))
            try:
                shutil.rmtree(destination_folder)
            except Exception as e:
                print(f"Error while removing the directory {destination_folder}: {e}")
        try:
            os.remove(zip_file)
        except Exception as e:
            print(f"Error while removing the file {zip_file}: {e}")

def main():
    dir = pathlib.Path(__file__).parent.resolve()
    unzip_files(dir)

if __name__ == '__main__':
    main()
