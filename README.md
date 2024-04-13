Certainly! Here's a README file for your project:

---

# Presentify

Presentify is a tool designed to assist teachers in generating questions and answers based on student project presentations, particularly in the form of PDF files. It automatically generates a set of general and intermediate questions to facilitate discussions about the project content.

## Features

- Automatic generation of 5 general and 5 intermediate questions based on inputted PDF files.
- Utilizes open source embedding models such as COHERE for text analysis and similarities
- Easy-to-use interface for teachers to upload PDF files and retrieve generated questionn which is povered by STREAMLIT 🔥

## Installation

To run the Presentation Helper locally, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/joelsiby02/PPT-QA.git
   ```

2. Navigate to the project directory:

   ```bash
   cd PPT-QA
   ```

3. Install the required dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project directory and add your GROQ_API_KEY and COHERE_API_KEY: search web for these keys!

   ```plaintext
   GROQ_API_KEY=<your_groq_api_key>
   COHERE_API_KEY=<your_cohere_api_key>
   ```

5. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

## Usage

1. Once the Streamlit app is running, you'll see an interface with options to input your Cohere and GROQ API keys in the sidebar.
2. Upload a PDF file containing the student project presentation using the file upload button.
3. Click the "Submit" button to process the uploaded PDF file.
4. After processing, the generated questions will be displayed in the main interface.
5. You can then copy the questions or save them to a file as needed or it automtically generates a reponce.txt file to store the questions and answers

## Note

- Make sure you have valid API keys for Cohere and GROQ services to use the application effectively.
- This project is currently designed to accept PDF files only. Support for other formats may be added in future updates such as direct PPT input could be done later.

---
