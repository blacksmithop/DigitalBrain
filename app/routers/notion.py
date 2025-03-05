from fastapi import APIRouter, File, HTTPException, UploadFile
from brain import NotionLoader
import logging


# Initialize the GitHub router
notion_router = APIRouter(prefix="/notion", tags=["Notion"])

# POST endpoint to fetch repositories
@notion_router.post("/download")
def extract_notion_archive(zip_file: UploadFile = File(...)):
    """
    Index content for a Notion Workspace
    - zip_file: Notion export
    """
    if not zip_file.filename.endswith(".zip"):
        raise HTTPException(
            status_code=400,
            detail="Only .zip files are allowed."
        )
    notion_loader = NotionLoader()
    try:
        file_content = zip_file.file.read()
        output_file_path = notion_loader.load_notion_export(file_content=file_content)
    except Exception as e:
        logging.info(e)
    return "Extracting Notion data"
