# Generative AI Text to SQL Query App

![Screenshot 2024-08-23 193559](https://github.com/user-attachments/assets/69115749-8ab6-4f06-9bd0-cab4d0bd9ec4)


# Overview
The Generative AI SQL Query App is a unique tool that leverages a Google LLM (Large Language Model) to convert natural English language into SQL queries. This app allows users to interact with databases using simple English commands, which are then translated into SQL queries to fetch the required data. It provides an easy-to-use interface through Streamlit, a popular Python web application framework, making database interaction accessible to non-technical users.

# Features
- Natural Language to SQL: Automatically converts natural language questions into SQL queries.
- Google LLM Integration: Uses state-of-the-art natural language processing to interpret user queries.
- SQLite3 Database: Built-in database management using SQLite3 to store and retrieve data.
- Streamlit Interface: User-friendly web interface for seamless interaction with the application.

# Project Structure
- sql.py: This script uses sqlite3 to create a database and manage records. It sets up the database and provides functions to create tables and manipulate data.
- app.py: The main application script that runs the Streamlit app. It handles user input, processes natural language using the Google LLM model, converts it into SQL queries, and displays results.

# Installation

Clone the repository:

Create an Virtual Environment : conda create -p text2sql python==3.11 -y

Activate your virtual Environment

Install requirements.txt file : pip install -r requirements.txt

Create .env file and save your GOOGLE_API_KEY:

Run Database: python sql.py

Run App: streamlit run app.py

Access the application: (It will redirect automatically.)

# Contributing
Contributions are welcome! If you have suggestions or improvements, please fork the repository and create a pull request.

# License
This project is licensed under the MIT License - see the LICENSE file for details.

# Contact
If you have any questions or feedback, please feel free to reach out:

- Email: brijesh29.it11@gmail.com
- LinkedIn: https://www.linkedin.com/in/brijesh-kapadiya-536406282/

# Acknowledgments
- Google for their powerful LLM model.
- The Streamlit community for providing an excellent framework for building web apps.

# Author
- Brijesh Kapadiya
- Data Scientist and AI Enthusiast



