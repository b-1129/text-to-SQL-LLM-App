from dotenv import load_dotenv
load_dotenv() ## load all the environment variables

import streamlit as st
import os
import sqlite3

import google.generativeai as genai

## configure our API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load google gemini model and provide sql query as response
def get_gemini_response(question, prompt):
    model=genai.GenerativeModel('gemini-pro')
    combined_input=f"{prompt} {question}"
    response=model.generate_content(combined_input)
    return response.text

## Function to retrieve query from SQL database
def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows


## Define your prompt
prompt=[
    """
You are expert in converting English Questions to SQL Query!
The SQL Database has the name STUDENT and has the following columns - NAME, CLASS,
SECTION, and MARKS \n\n For example, \nExample 1: How many entries of records are present?,
The SQL command will be something like this SELECT COUNT(*) from STUDENT;
\nExample 2: Tell me all the students studying in Data Science Class?,
The SQL command will be something like this SELECT * from STUDENT
where CLASS="Data Science";
also the SQL code should not have ``` in beginning or end and SQL word in output.
"""
]

## Streamlit App:
st.set_page_config(page_title="I can Retrieve any SQL Query")
st.header("Gemini App to Retrieve SQL Data")

question=st.text_input("Input: ",key="input")
submit= st.button("Ask the Question")

## if submit is clicked:
if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    data=read_sql_query(response,"student.db")
    st.subheader("The Response is")
    for row in data:
        print(row)
        st.header(row)