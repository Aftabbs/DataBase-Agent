# DB Agentic AI

![image](https://github.com/user-attachments/assets/b7296dfc-295d-4457-855a-9234f9c2ded0)


A **DB Agent** built using `phidata`, `Groq`, and `SQLAlchemy` to interact with SQL databases. This project allows users to query a SQL database using natural language and get responses in a user-friendly format. The agent is integrated with a **Gradio UI** for easy interaction.

---

## Features

- **Natural Language Queries**: Ask questions about your database in plain English.
- **SQL Database Integration**: Connects to Microsoft SQL Server using `pyodbc` and `SQLAlchemy`.
- **Gradio UI**: A simple and interactive web interface for querying the database.
- **ANSI Escape Code Removal**: Ensures clean and readable responses in the UI.

---

## Prerequisites

Before running the project, ensure you have the following installed:

1. **Python 3.8+**
2. **ODBC Driver 18 for SQL Server**: Install the ODBC driver for your operating system.
   - [Download ODBC Driver 18 for SQL Server](https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver16)
3. **Git**: To clone the repository.

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/db-agent-project.git
   cd db-agent-project
   ```

2. **Set Up a Virtual Environment** (Optional but Recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## Configuration

1. **Set Up Environment Variables**:
   - Create a `.env` file in the root directory and add your database credentials:
     ```plaintext
     SERVER_NAME=server
     DATABASE_NAME=UCC
     USERNAME=usn
     PASSWORD=pwd
     GROQ_API_KEY=your_groq_api_key
     ```

2. **Update the Code**:
   - Replace the placeholders in the `db_agent.py` file with your actual database credentials and Groq API key.

---

## Usage

1. **Run the Gradio UI**:
   ```bash
   python db_agent.py
   ```

2. **Access the UI**:
   - Open your browser and navigate to the URL provided in the terminal (e.g., `http://127.0.0.1:7860`).

3. **Enter Database Details**:
   - Provide the server name, database name, username, and password in the respective fields.

4. **Ask a Query**:
   - Enter a natural language query (e.g., "List the tables in the database").
   - Click **Submit** to get the agent's response.

---

## Example Queries

- **List Tables**:
  ```
  List the tables in the database.
  ```

- **Describe a Table**:
  ```
  Tell me about the contents of the Filings table.
  ```

- **Count Rows**:
  ```
  How many rows are in the Filings table?
  ```

---

## Project Structure

```
db-agent-project/
├── gradio_ui.py            # Main script for the Gradio UI
├── requirements.txt        # List of dependencies
├── README.md               # Project documentation
├── .env                    # Environment variables (not included in the repo)
└── .gitignore              # Files to ignore in Git
```

---

## Dependencies

- **phidata**: For building the agent.
- **SQLAlchemy**: For database connectivity.
- **pyodbc**: For connecting to SQL Server.
- **gradio**: For the web interface.
- **python-dotenv**: For loading environment variables.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

