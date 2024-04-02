'''
This script utilizes several Python libraries to perform Optical Character Recognition (OCR) on an image, correct its grammar, and save the corrected transcription to a text file. It employs pytesseract for OCR, PIL (Python Imaging Library) for image processing, language_tool_python for grammar correction, and tqdm for displaying a progress bar. The script first performs OCR on the image, then corrects the grammar of the extracted text, and finally saves the corrected transcription to a text file.
'''

import pytesseract
from PIL import Image
import language_tool_python
from tqdm import tqdm

# Path to the Tesseract executable (update this to your Tesseract installation path)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Path to your image file
image_path = 'cartademotivoimg.png'

# Perform OCR on the image
image = Image.open(image_path)
transcription = pytesseract.image_to_string(image)

# Initialize LanguageTool
tool = language_tool_python.LanguageTool('en-US')

# Split the transcription into sentences for progress bar
sentences = transcription.split('.')

# Create a progress bar for grammar correction
with tqdm(total=len(sentences), desc="Correcting Grammar") as pbar:
    corrected_sentences = []
    for sentence in sentences:
        corrected_sentence = tool.correct(sentence)
        corrected_sentences.append(corrected_sentence)
        pbar.update(1)

# Combine the corrected sentences back into a single text
corrected_transcription = '. '.join(corrected_sentences)

# Define the output file path for the corrected transcription
output_file = 'corrected_transcription.txt'

# Write the corrected transcription to a text file
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(corrected_transcription)

print(f"Corrected transcription saved to {output_file}")
