from utils import get_lib_dir, delimited_string, find_or_create
from dotenv import load_dotenv, dotenv_values
from tesseract_comp import extract_info
from pdf2imageconverter import convert_pdf_to_image
import pytesseract
from gtts import gTTS
import os
from PIL import Image



load_dotenv()

pdf_path = f'{os.getcwd()}{dotenv_values()["PDF_PATH"]}'

tesser_data = os.getcwd()+dotenv_values()['TESSER_TES_DATS']

os.environ['TESSDATA_PREFIX'] = tesser_data

tesser_path = dotenv_values()['TESSER_PATH_']+f"{delimited_string}tesseract.exe"

pytesseract.pytesseract.tesseract_cmd = f'''{os.getcwd()}{tesser_path}'''

audio_dir = "audios" + delimited_string
image_dir = "images"+ delimited_string
extracted_text = "text"+ delimited_string

for file in os.listdir(pdf_path):

    if file.split('.')[-1] == 'pdf':
        f_dir = f'{file.split(".")[0]}{delimited_string}'
        find_or_create([audio_dir+f_dir, image_dir+f_dir, extracted_text+f_dir])
        images = convert_pdf_to_image(pdf_path+f'{delimited_string}{file}', get_lib_dir(os.getcwd(),
                    delimited_string, dotenv_values()['POPPLER_BIN'], 0))

        cnt = 0
        for image in images:
            cnt += 1
            image.save(image_dir+f_dir+f'{cnt}.jpg', "JPEG")
            print("extracting page: ", image)
            with open(extracted_text+f_dir+f'{cnt}.txt', 'w', encoding="utf-8") as txt_file:
                txt_file.write(extract_info(image))
            myobj = gTTS(text=extract_info(image), lang="te", slow=False)
            myobj.save(audio_dir+f_dir+f'{cnt}.mp3')

