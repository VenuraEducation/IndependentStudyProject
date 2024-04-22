from langchain_google_genai import GoogleGenerativeAI
from langchain.utilities.sql_database import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain,SQLDatabaseSequentialChain
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from langchain.vectorstores.chroma import Chroma
from langchain.prompts import SemanticSimilarityExampleSelector
from langchain.chains.sql_database.prompt import PROMPT_SUFFIX, _mssql_prompt
from langchain.prompts import FewShotPromptTemplate
from langchain.prompts.prompt import PromptTemplate
from chromadb.utils import embedding_functions
import os
from dotenv import load_dotenv
# import pyodbc
# from sqlalchemy import create_engine

from few_shots import few_shots

load_dotenv()

def getfew_shot_db_chain(): 

   
    db_user = 'DGLCMB\venura.madushan'
    db_password = 'abcdef123'
    db_host = 'sqlserver\server1'
    db_name = 'LLMData'

    db = SQLDatabase.from_uri(f"mssql+pymssql://{db_user}:{db_password}@{db_host}/{db_name}",
                              sample_rows_in_table_info=1)
    llm = GoogleGenerativeAI(model="gemini-pro",google_api_key=os.environ['GOOGLE_API_KEY'], temperature=0.1)

    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    # default_ef = embedding_functions.DefaultEmbeddingFunction()
    to_vectorize = [" ".join(exmple.values()) for exmple in few_shots]

    vectorstore = Chroma.from_texts( to_vectorize, embeddings, metadatas=few_shots)

    example_selector = SemanticSimilarityExampleSelector(vectorstore=vectorstore, k=2)

    sql_prompt = """You are a MSSQL expert. Given an input question, first create a syntactically correct MSSQL query to run, then look at the results of the query and return the answer to the input question.
    Unless the user specifies in the question a specific number of examples to obtain, query for at most {top_k} results using the TOP clause as per MySQL. You can order the results to return the most informative data in the database.
    Never query for all columns from a table. You must query only the columns that are needed to answer the question. Wrap each column name in backticks (`) to denote them as delimited identifiers.
    Pay attention to use only the column names you can see in the tables below. Be careful to not query for columns that do not exist. Also, pay attention to which column is in which table.
    Pay attention to use CURDATE() function to get the current date, if the question involves "today".
    
    Use the following format:
    
    Question: Question here
    SQLQuery: Query to run with no pre-amble
    SQLResult: Result of the SQLQuery
    Answer: Final answer here
    
    No pre-amble.
    """

    sql_prompt2 = """You are a MSSQL expert. Given an input question, first create a syntactically correct MSSQL query to run, then look at the results of the query and return the answer to the input question. Always give SQLQuery as the answer.
    Unless the user specifies in the question a specific number of examples to obtain, query for at most {top_k} results using the TOP clause as per MySQL. You can order the results to return the most informative data in the database.
    Never query for all columns from a table. You must query only the columns that are needed to answer the question. Wrap each column name in backticks (`) to denote them as delimited identifiers.
    Pay attention to use only the column names you can see in the tables below. Be careful to not query for columns that do not exist. Also, pay attention to which column is in which table.
    Pay attention to use CURDATE() function to get the current date, if the question involves "today".
    
    Use the following format:
    
    Question: Question here
    SQLQuery: Query to run with no pre-amble
    SQLResult: Result of the SQLQuery
    Answer: SQLQuery
    
    No pre-amble.
    """

    example_prompt = PromptTemplate(
        input_variables=["Question", "SQLQuery", "SQLResult", "Answer"],
        template="\nQuestion: {Question}\nSQLQuery: {SQLQuery}\nSQLResult: {SQLResult}\nAnswer: {Answer}",
    )

    few_shot_prompt = FewShotPromptTemplate(
        example_selector=example_selector,
        example_prompt=example_prompt,
        prefix=sql_prompt,
        suffix=PROMPT_SUFFIX,
        input_variables=["input","table_info","top_k"]
    )
    print(few_shot_prompt)
    chain = SQLDatabaseChain.from_llm(llm, db, prompt=few_shot_prompt, verbose=True, return_sql=True, use_query_checker=True)
    # chain = SQLDatabaseSequentialChain.from_llm(llm, db, prompt=few_shot_prompt,verbose=True, return_sql=True, use_query_checker=True)

    return chain

if __name__ == "__main__":
    chain = getfew_shot_db_chain()
    chain.run()

