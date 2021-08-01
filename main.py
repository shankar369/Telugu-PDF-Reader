# from utils import get_lib_dir, delimited_string
from dotenv import load_dotenv, dotenv_values
# from tesseract_comp import extract_info
# from pdf2imageconverter import convert_pdf_to_image
# import pytesseract
# from gtts import gTTS
# import playsound
import os

from fastapi import FastAPI, Request, File, UploadFile, BackgroundTasks, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from scheduler import add_task

import aiofiles

load_dotenv()


app = FastAPI()
app.queue = []
app.mount(
    "/static",
    StaticFiles(directory= dotenv_values()["STATICS"]),
    name="static",
)

templates = Jinja2Templates(directory="Views")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.post("/pdf")
async def handle_post_pdf(background_tasks: BackgroundTasks,pdf_file: UploadFile = File(...), ):
    if(not pdf_file.content_type == "application/pdf"):
        response.status_code = 404
        return {
            'error': 'Only PDF files are allowed'
        }
    try:
        async with aiofiles.open(dotenv_values()["PDF_UPLOAD_PATH"]+pdf_file.filename, 'wb') as out_file:
            while content := await pdf_file.read(1024):  # async read chunk
                await out_file.write(content)  # async write chunk
        
        background_tasks.add_task(add_task, file_name=pdf_file.filename)
        return {
            "status": "uploaded",
            "file_name": pdf_file.filename,
            "fileb_content_type": pdf_file.content_type,
        }
    except Exception as ex:

        return {
            "status": "error",
            "message" : str(ex)
        }

@app.get("/audios")
def get_audio_folders(request: Request):
    audio_folders = os.listdir(dotenv_values()["AUDIOS_PATH"])
    return templates.TemplateResponse("audios.html",{"request":request,"folders":audio_folders})

@app.get("/audios/{folder_name}")
def get_audio_folders(request: Request,folder_name):
    audio_files = os.listdir(dotenv_values()["AUDIOS_PATH"]+folder_name)
    return templates.TemplateResponse("audio.html",{"request":request,"audios":audio_files,"folder":folder_name})