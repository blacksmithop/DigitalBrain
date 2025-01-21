from utils import unzip_file, identify_notion_export_file
from os import listdir

class NotionLoader:
    def __init__(self):
        pass
    
    def load_notion_export(self, target_directory: str = "./hippocampus/notion"):
        directory_files = listdir(target_directory)
        notion_export_files = identify_notion_export_file(files=directory_files)
        notion_export = notion_export_files[0]
        unzip_file(directory_path=target_directory, file_name=notion_export)
    