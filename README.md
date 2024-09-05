# Multilingual OCR, Translation, and Summarization Tool
This project is a comprehensive tool designed for text extraction, translation, and summarization across multiple languages. The tool uses Optical Character Recognition (OCR) to extract text from various file formats such as images (PNG, JPG) and PDFs. Once the text is extracted, users can translate it into multiple languages or generate concise summaries of the content. The project leverages advanced libraries like pytesseract for OCR, googletrans for translation, and transformers for text summarization.

Key features include:

* OCR: Supports text extraction from images and PDFs in multiple languages.
* Translation: Translates extracted text into numerous languages using Google Translate.
* Summarization: Summarizes long texts into concise, readable summaries using advanced transformer-based models.
* User Interface: A simple and interactive Tkinter-based GUI allows users to upload files, translate, and summarize text seamlessly.

This tool is ideal for users working with multilingual documents, providing a unified platform for text processing.

# How to run the code:
1. create environment.
2. use pip install -r requirements.txt
3. Install OCR Software(already in a folder), Copy the OCR path and paste it in upload function(in mypackage).
4. Select the summarization model from mypackage i.e tensorflow or pytorch and update in finale.
5. run all files in mypackage and then run the main project i.e finale.py
6. files in Test are experiments and that ITTS file is base model.




# Steps to use Multi-lang Support:
Here are the steps:

1. Download Language Data Files
You can download additional language data files from the official Tesseract GitHub repository:

Link to language data files: Tesseract-OCR Language Data:

2. Steps to Add Multiple OCR Languages in Your Project
Follow these steps to add multiple languages to your OCR functionality:

* Download the Required Language Files:

 Go to the Tesseract language data files page.
Download the .traineddata files for the languages you need. For example, if you want to add Spanish (spa), Japanese (jpn), Hindi (hin), and Malayalam (mal), download the respective .traineddata files.

* Place Language Files in the Tesseract Directory:

Locate your Tesseract installation directory (e.g., C:\Program Files\Tesseract-OCR\tessdata).
Place the downloaded .traineddata files inside the tessdata folder.

* Update the OCR Code to Include Multiple Languages:

In your Python OCR code, you can update the language parameter to include multiple languages using the lang parameter.
