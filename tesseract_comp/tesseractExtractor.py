import pytesseract


def extract_info(image, lan='tel+eng'):
    return pytesseract.image_to_string(image, lang=lan)
