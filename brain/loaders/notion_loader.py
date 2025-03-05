from brain.utils import unzip_file

NOTION_EXPORT_PATH = "./hippocampus/notion"

class NotionLoader:
    def __init__(self):
        pass
    
    def load_notion_export(self, file_content: bytes):
        output_file_path = unzip_file(file_name="notion_export", output_directory=NOTION_EXPORT_PATH, zip_file_content=file_content)
        return output_file_path