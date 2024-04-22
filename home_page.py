
import pandas as pd
import pyodbc
from pandas_profiling import ProfileReport
from sqlalchemy import create_engine
import streamlit as st
import datetime

from model import getfew_shot_db_chain
from model_chart import get_chart_type



server = 'SQL_server' # to specify an alternate port
database = 'LLMData' 
username = 'iislogin' 
password = 'abcdd123'
driver = 'SQL Server'
driver2 = 'SQL+Server+Native+Client+11.0'

def create_sql_connection(server, database, username, password):
    # Construct the connection string
    connection_string = f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver}"
    # Create the engine and connect to the database
    engine = create_engine(connection_string)
    return engine

def log_question_answer(question, answer):
    log_entry = { 
        'DateTime': datetime.datetime.now().strftime(f"%Y-%m-%d %H:%M:%S"),
        'Question': question,
        'Answer': answer
    }
    with open('Q&A_log.py','a') as f:
        f.write(str(log_entry) + '\n')


# url = f"mssql+pyodbc://{username}:{password}@{server}:{port}/{database}?driver={driver}"
# sql_conn = pyodbc.connect('DRIVER=SQL Server;SERVER=sqlsrv-01\\dglbi;DATABASE=LLMData;Trusted_Connection=yes')
sql_con = create_sql_connection(server, database, username, password)

# engine = create_engine(url)

#Based on the result get from getchart type function, Render the Visualization

def View_Charts(df, question, answer):
    chart_col = get_chart_type(question=question,sql_query=answer)
    if chart_col is not None:
        print(chart_col)
        if df is not None:
            #st.dataframe(df)

            dataframe = pd.DataFrame(df,columns=chart_col["Columns"])

            # Parse the question to identify the requested visualization type
            if "bar chart" in chart_col["Chart Type"]:
                st.bar_chart(dataframe,x=chart_col["Columns"][0])
            elif "area chart" in chart_col["Chart Type"]:
                st.area_chart(dataframe,x=chart_col["Columns"][0])
            elif "scatter chart" in chart_col["Chart Type"]:
                st.scatter_chart(dataframe,x=chart_col["Columns"][0])
            elif "line chart" in chart_col["Chart Type"]:
                st.line_chart(dataframe,x=chart_col["Columns"][0])
            else:
                st.dataframe(dataframe)

def home_view():
    st.title("LLMData SQL Database Q&A Agent")

    question = st.text_input("Question : ")

    submit_button = st.button("Submit")


    if submit_button:
        if question:
            
            with st.spinner("Fetching answer... Please wait."):
                chain = getfew_shot_db_chain()
                try:
                    answer = chain.run(question)
                    log_question_answer(question, answer)
                    df = pd.read_sql(answer, sql_con)
                    print(answer)
                    st.subheader("Answer : ")
                    View_Charts(df, question, answer)
                except Exception as e:
                    st.warning(e)
                    print(answer)
                    pass
            st.subheader("SQL Query : ")
            st.write(answer)
            

        else:
            st.warning("Please enter a question..!")

if __name__ == "__main__":
    home_view()