from utils import get_lib_dir, delimited_string
from dotenv import load_dotenv, dotenv_values
from tesseract_comp import extract_info
from pdf2imageconverter import convert_pdf_to_image
import pytesseract
from gtts import gTTS
import playsound
import os


load_dotenv()

def process_pdf(file):
    pdf_path = f'{os.getcwd()}{dotenv_values()["PDF_PATH"]}'

    tesser_data = os.getcwd()+dotenv_values()['TESSER_TES_DATS']

    os.environ['TESSDATA_PREFIX'] = tesser_data

    tesser_path = dotenv_values()['TESSER_PATH_']+f"{delimited_string}tesseract.exe"

    pytesseract.pytesseract.tesseract_cmd = f'''{os.getcwd()}{tesser_path}'''

    dir = "statics/audios" + delimited_string

    # for file in os.listdir(pdf_path):

    #     if file.split('.')[-1] == 'pdf':
    op_dir = dir+f'{file.split(".")[0]}{delimited_string}'
    os.mkdir(op_dir)
    images = convert_pdf_to_image(pdf_path+f'{delimited_string}{file}', get_lib_dir(os.getcwd(),
                delimited_string, dotenv_values()['POPPLER_BIN'], 0))

    cnt = 0
    print(len(images),"----images count")
    for image in images:
        try:
            cnt += 1
            print("extracting page: ", image)

            myobj = gTTS(text=extract_info(image), lang="te", slow=False)
            myobj.save(op_dir+f'page-{cnt}.mp3')
        except Exception as ex:
            print(str(ex))


def add_task(file_name):
    print(file_name, " added for processing .......")
    process_pdf(file_name)