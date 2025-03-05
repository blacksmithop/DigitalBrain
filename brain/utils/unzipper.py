import zipfile
from os import path
from io import BytesIO


def unzip_file(zip_file_content: bytes, file_name: str, output_directory: str):
    file_path = path.join(output_directory, file_name)

    with BytesIO(zip_file_content) as zip_buffer:
        with zipfile.ZipFile(zip_buffer, "r") as zip_ref:
            zip_ref.extractall(file_path)
    return file_path
