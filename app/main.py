from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app import router_list, setup_rich_logger
import logging

# Initialize FastAPI app
app = FastAPI()
setup_rich_logger()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update to specific domains in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

for router in router_list:
    app.include_router(router=router)

# Base endpoint to confirm the service is running
@app.get("/")
def root():
    logging.info("Index page")
    return {"message": "Welcome to the Digital Brain API!"}
