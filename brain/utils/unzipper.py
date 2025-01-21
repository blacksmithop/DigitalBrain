import zipfile
from os import path


def unzip_file(directory_path: str, file_name: str):
    file_path = path.join(directory_path, file_name)
    with zipfile.ZipFile(file_path, "r") as zip_ref:
        zip_ref.extractall(directory_path)
