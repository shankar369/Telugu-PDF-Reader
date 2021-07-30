from pdf2image import convert_from_path


def convert_pdf_to_image(pdf_path, proppler_path, should_append=False):
    return convert_from_path(pdf_path, poppler_path=proppler_path)
