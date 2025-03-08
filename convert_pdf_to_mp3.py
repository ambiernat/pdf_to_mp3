from google.colab import files, drive
from gtts import gTTS
from PyPDF2 import PdfReader
import os
import shutil

language='en'
tld='co.uk'

# import gtts
# gtts.lang.tts_langs()
# gives a list of available languages

#import pycryptodome===3.15.0

def upload_pdf_file():
    """
    Uploads a PDF file and returns its filename.
    """
    uploaded = files.upload()
    if uploaded:
        return next(iter(uploaded))
    else:
        raise Exception("No file uploaded")

def process_pdf_file(file_path, output_dir):
    """
    Processes a PDF file to convert its text to speech and saves it as an MP3 file.
    """
    text = ""
    pdf_reader = PdfReader(file_path)
    for page in pdf_reader.pages:
        text_intermediate = page.extract_text()
        text_intermediate = text_intermediate.replace("\n", "")
        text_intermediate = text_intermediate.replace("newline", "\n")
        text += text_intermediate or ""
    filename = os.path.splitext(os.path.basename(file_path))[0] + ".mp3"
    full_path = os.path.join(output_dir, filename)
    tts = gTTS(text=text, lang=language, tld=tld)
    tts.save(full_path)
    return full_path

def zip_files(directory, zip_name="audio_files.zip"):
    """
    Zips the files in a directory and returns the path to the zip file.
    """
    shutil.make_archive(zip_name, 'zip', directory)
    return zip_name + ".zip"

def main():
    """
    Main function to handle user input for single file or directory processing.
    """
    mode = input("Press Enter to upload a single file or type 'dir' to process an entire directory: ").strip()

    if mode.lower() == 'dir':
        directory = input("Enter the path to the directory on Google Drive (this can be obtained by browsing your Google Drive on the left hand column and clicking the three dots and selecting 'Copy Path'): ").strip()
        output_dir = directory

        mp3_paths = []
        for filename in os.listdir(directory):
            if filename.endswith('.pdf'):
                file_path = os.path.join(directory, filename)
                print(f"Processing {file_path}...")
                mp3_path = process_pdf_file(file_path, output_dir)
                mp3_paths.append(mp3_path)

        if mp3_paths:
            zip_path = zip_files(output_dir)
            files.download(zip_path)
    else:
        try:
            filename = upload_pdf_file()
            mp3_path = process_pdf_file(filename, '/content')
            files.download(mp3_path)
        except Exception as e:
            print(f"An error occurred: {e}")

# if 'google.colab' in str(get_ipython()):
 #   main()
#else:
 #   print('This code is intended to run in Google Colab.')
