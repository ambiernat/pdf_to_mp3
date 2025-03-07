PDF to MP3 Converter
This is a Python script that allows users to convert PDF files to MP3 audio files in the language of their choice. It uses PyPDF2 to extract text from the PDF files, Google Translate API to translate the text into the selected language, and Google Text-to-Speech (gTTS) API to synthesize the speech and save the audio file.
The script has a user-friendly command-line interface that prompts the user to select the PDF file, the language, and gives the option to exit or continue converting files. It also creates separate folders for PDF and MP3 files.

💡Practical use
This script can be useful for people who prefer to listen to text instead of reading. This can be convenient, for example, when traveling on public transport or playing sports. In addition, the script can be used to create audio books or audio lectures.




Settings
To use it, you need to complete the following steps:


📁 Clone this repository
git clone https://github.com/lazycatcoder/pdf-to-mp3.git

📦 Install dependencies
pip install -r requirements.txt
✨ How to use
Download the repository and install the required modules
Create "pdf" and "mp3" folders in the same directory as the script (optional)
Place the PDF files to be converted into the "pdf" folder
Run the script 🚀
Follow the instructions on the screen

🔧 Additional Information
🔴 For the script to work correctly, it is necessary that PDF files be recognized or that it is possible to highlight the characters contained in them, since this is necessary for the script to read text from files.
