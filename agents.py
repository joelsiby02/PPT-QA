from textwrap import dedent
from crewai import Agent
import os
# from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain_cohere import CohereEmbeddings
from dotenv import load_dotenv
load_dotenv()
from langchain_community.tools import DuckDuckGoSearchRun
# from crewai_tools import PDFSearchTool



# from crewai_tools import (
#     DirectoryReadTool,
#     FileReadTool,
#     SerperDevTool,
#     WebsiteSearchTool
# )



GROQ_API_KEY = os.getenv('GROQ_API_KEY')
COHERE_API_KEY = os.getenv('COHERE_API_KEY')
# llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature = 0.3)
llm = ChatGroq(temperature=0.008, groq_api_key= GROQ_API_KEY, model_name="mixtral-8x7b-32768")
# tool = PDFSearchTool(
#     config=dict(
#         llm=dict(
#             provider="groq",
#             config=dict(
#                 model="mixtral-8x7b-32768", 
#                 temperature=0.1,
#                 top_p=1,
#                 stream=True,
#             ),
#         ),
#         embedder=dict(
#             provider="cohere",
#             config=dict(
#                 model="embed-english-light-v3.0",
#                 task_type="retrieval_document",
#                 # title="Embeddings",
#             ),
#         ),
#     )
# )

# tool = PDFSearchTool()

search_tool = DuckDuckGoSearchRun()

class ProjectSelectionAgents:
    def teacher(self):
        return Agent(
            role='Professor',
            goal='Prepare questions from Student\'s project PDF',
            backstory=dedent("""\
                You are a Project approving classroom Professor at a leading college.
                Your expertise in guiding students through their project selection, and approval of their Project idea by asking them relevent questions about their project, and do your best to produce perfect clean and struchured questions understanding the students inputted PDF.
            """),
            llm=llm,
            tools=[search_tool],
            verbose=True
        )
