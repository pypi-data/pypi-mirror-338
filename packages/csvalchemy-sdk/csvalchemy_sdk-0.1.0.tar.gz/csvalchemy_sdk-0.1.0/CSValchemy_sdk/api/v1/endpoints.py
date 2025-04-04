import os
import logging
import tempfile
from fastapi import APIRouter, HTTPException, File, UploadFile

from ...core import encode_workbook
from ...config import merge_config
from ...utils.excel import load_workbook_from_file

from app.config.default_config import DEFAULT_CONFIG

# Setup logging
logger = logging.getLogger(__name__)

# Create API router
router = APIRouter(
    prefix="/v1",
    tags=["v1"],
    responses={
        404: {"description": "Not found"},
        500: {"description": "Internal server error"},
    },
)

# Endpoints


@router.post("/encode")
async def encode_spreadsheet(file: UploadFile = File(...)):
    try:
        # Apply user configuration
        config = merge_config(DEFAULT_CONFIG)

        # Create temp file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx") as temp_file:
            temp_file.write(await file.read())
            temp_path = temp_file.name

        try:
            # Load workbook
            workbook = load_workbook_from_file(temp_path)

            # Encode workbook
            encoded = encode_workbook(workbook, config)

            # Create response
            response = {
                "encoded_workbook": encoded,
                "metadata": {
                    "filename": file.filename,
                    "sheets": list(encoded["sheets"].keys()),
                },
            }

            return response
        finally:
            # Clean up temp file
            if os.path.exists(temp_path):
                os.unlink(temp_path)

    except Exception as e:
        logger.error(f"Error encoding spreadsheet: {str(e)}")
        raise HTTPException(
            status_code=500, detail=f"Error encoding spreadsheet: {str(e)}"
        )
