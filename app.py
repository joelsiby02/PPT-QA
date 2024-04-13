import streamlit as st
import os
from textwrap import dedent
from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_cohere import CohereEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv
from crewai import Crew, Process, Agent
from tasks import ProjectSelectionTask
from agents import ProjectSelectionAgents
from langchain_groq import ChatGroq

load_dotenv()

# GROQ_API_KEY = os.getenv('GROQ_API_KEY')
COHERE_API_KEY = os.getenv('COHERE_API_KEY')
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

manager_llm = ChatGroq(temperature=0.1, groq_api_key= GROQ_API_KEY, model_name="mixtral-8x7b-32768")

# Function to process PDF and perform embedding
def process_pdf_and_embedding(pdf_file_path, cohere_api_key):
    try:
        # Load PDF file
        loader = UnstructuredPDFLoader(file_path=pdf_file_path)
        data = loader.load()

        # Initialize CohereEmbeddings with the GROQ API key
        embedding_model = CohereEmbeddings(cohere_api_key=cohere_api_key)

        # Split text from PDF and chunk for proper embeddings
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=8000, chunk_overlap=100)
        chunks = text_splitter.split_documents(data)

        # Add vector DB
        vector_db = Chroma.from_documents(
            documents=chunks,
            embedding=embedding_model,
            collection_name="rag-pdf"
        )

        # Return processed data
        return data, chunks, vector_db

    except Exception as e:
        st.error(f"Error processing PDF: {str(e)}")
        return None, None, None

def generate_q(pdf_file):
    task = ProjectSelectionTask()
    agent = ProjectSelectionAgents()

    # Create Agents
    professor_agent = agent.teacher()

    # Create Tasks
    professor_task = task.question_task(professor_agent, pdf_file)
    valuation = task.valuation_task(professor_agent, pdf_file)
    
    # Provide expected_output field
    professor_task.expected_output = {}

    # Create Crew responsible for Copy
    crew = Crew(
        agents=[professor_agent],
        tasks=[professor_task, valuation],
        manager_llm= manager_llm,  # Mandatory for hierarchical process
        process=Process.hierarchical,  # Specifies the hierarchical management approach
        memory=True,
        verbose=True
    )

    responce = crew.kickoff()
    
    file_name = 'responce.txt'
    # Write the game code to the file
    with open(file_name, "w") as file:
        file.write(responce)

    # st.write("\n\n########################")
    # st.write("Results")
    # st.write("########################\n")
    st.write("The Questions to be adreesed are:")
    st.code(responce)
    st.write("\n\nquestions have been saved to", file_name)


# Main Streamlit app
def main():
    st.title("Presentation Helper")

    # File upload
    pdf_file = st.file_uploader("Upload a PDF file", type=["pdf"])

    if pdf_file is not None:
        # Save the uploaded PDF file to a temporary directory
        with open("temp.pdf", "wb") as f:
            f.write(pdf_file.getvalue())

        # Process PDF file and perform embedding
        data, chunks, vector_db = process_pdf_and_embedding("temp.pdf", COHERE_API_KEY)

        if data is not None:
            # Display processed data
            st.success("PDF loaded and processed successfully!")
            # st.write("Chunks:", len(chunks))
            # st.write("Vector DB:", vector_db)

            # Generate questions
            generate_q(pdf_file)

# Run the app
if __name__ == "__main__":
    main()