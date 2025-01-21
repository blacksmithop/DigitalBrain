import re
from typing import List

EXPORT_FINDER = re.compile('(?i)^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}_Export-[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\.zip$') 

def identify_notion_export_file(files: List[str]):
    export_files = list(filter(EXPORT_FINDER.match, files))
    print(export_files)

if __name__ == "__main__":
    files = [
        "0b696380-e17c-4c70-9fec-1c6f1b3cac73_Export-0cedc12d-2c73-4bdb-a964-65277991495c.zip",
        "about.txt",
        "mydata.zip"
    ]
    identify_notion_export_file(files=files)
