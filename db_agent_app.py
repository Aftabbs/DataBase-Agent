from phi.agent import Agent
from phi.tools.sql import SQLTools
from phi.model.groq import Groq
from sqlalchemy import create_engine, URL  
import pyodbc  
import warnings
import gradio as gr
from io import StringIO
import sys
import re
warnings.filterwarnings("ignore")

def connect_win(server, database, username, password):
    try:
        connection_url = URL.create(
            "mssql+pyodbc",
            username=username,
            password=password,
            host=server,
            database=database,
            query={
                "driver": "ODBC Driver 18 for SQL Server",
                "TrustServerCertificate": "yes",
                "Encrypt": "no",
                "Network": "DBMSSOCN"
            }
        )
        engine = create_engine(connection_url, fast_executemany=True)
        print("Connection successful!")
        return engine
    except Exception as e:
        print(f"Connection Error: {e}")
        return None

def remove_ansi_escape_codes(text):
    """
    Removes ANSI escape codes from the text.
    """
    ansi_escape = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")
    return ansi_escape.sub("", text)

def query_agent(server, database, username, password, user_query):
    """
    Establishes a connection to the database and sends the user query to the agent.
    """
    try:
        engine = connect_win(server, database, username, password)
        if not engine:
            return "Failed to establish a connection to the database. Please check your connection details."

        agent = Agent(
            model=Groq(id="llama-3.3-70b-versatile", api_key='API-KEY'),
            tools=[SQLTools(db_engine=engine)]
        )

        output_capture = StringIO()
        sys.stdout = output_capture  
        agent.print_response(user_query, markdown=True)
        sys.stdout = sys.__stdout__ 
        response = output_capture.getvalue() 

        cleaned_response = remove_ansi_escape_codes(response)
        return cleaned_response
    except Exception as e:
        return f"Error: {e}"

def gradio_ui():
    with gr.Blocks() as demo:
        gr.Markdown("## DATABASE AGENT: Agentic AI")
        
        with gr.Row():
            server = gr.Textbox(label="Server Name", placeholder="e.g., sqldev.corp.convergenceinc.com")
            database = gr.Textbox(label="Database Name", placeholder="e.g., UCC")
        with gr.Row():
            username = gr.Textbox(label="Username", placeholder="e.g., maftab")
            password = gr.Textbox(label="Password", type="password", placeholder="e.g., your_password")
        
        user_query = gr.Textbox(label="Enter your query", placeholder="e.g., List the tables in the database")
        
        output = gr.Textbox(label="Agent Response", interactive=False)
        
        submit_button = gr.Button("Submit")
        
        submit_button.click(
            fn=query_agent,
            inputs=[server, database, username, password, user_query],
            outputs=output
        )
    
    demo.launch()

if __name__ == "__main__":
    gradio_ui()
