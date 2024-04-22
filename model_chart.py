from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain.prompts.prompt import PromptTemplate
from langchain_core.output_parsers import BaseGenerationOutputParser
from langchain_core.outputs import ChatGeneration, Generation
from typing import Any, List
import os
from dotenv import load_dotenv
import json

load_dotenv()

#Defining the LLM
llm = GoogleGenerativeAI(model="gemini-pro",google_api_key=os.environ['GOOGLE_API_KEY'], temperature=0.2)

#Creating the Output parser function
def convert_to_json(text):
    
    # Parse the response string
    chart_type = text.split('\n')[0].split(':')[1].strip()
    columns = [column.strip() for column in text.split('\n')[1].split(':')[1].split(',')]

    # Construct a dictionary
    json_output = {
    "Chart Type": chart_type,
    "Columns": columns
        }

    return json_output

class TexttoJson(BaseGenerationOutputParser[str]):
    "Pass the output from the LLM to the JSON"

    def parse_result(self, result: List[Generation], *, partial: bool = False) -> Any:
        generation = result[0]
        json_output = convert_to_json(generation.text)
        return json_output
#End of Output parser

examples = [
    {
        "userInput": "i need bar chart who are the clients we worked in Germeny in last 6 months with no of shipments?",
        "sql_query": """select BillingClientName, count(ShipmentNumber) as ShipmentCount
                    from RevandVolume_ShipmentDate
                    where ShipmentDate >= DATEADD(MONTH, -6, GETDATE()) AND ShipmentDate <= GETDATE() 
                    and OriginCountry = 'Germeny' group by BillingClientName order by ShipmentCount desc
                    """,
        "chart_type": "bar chart",
        "chart_columns": "BillingClientName, ShipmentCount",
    },
    {
        "userInput": "i want Bar chart on agent list and their shipment count who worked with us in Sri Lanka in last 2 months.",
        "sql_query": """select distinct AgentName, count(*) as shipment_count 
                    from RevandVolume_ShipmentDate WHERE AgentCountryName like 'United kingdom' and INCO = 'EXW'  
                    and ShipmentDate >= DATEADD(MONTH, -2, GETDATE()) AND ShipmentDate <= GETDATE()
                    group by AgentName\n""",
        "chart_type": "bar chart",
        "chart_columns": "AgentName, shipment_count",
    }
]


#Creating the Promt Template
#The PromptTemplate is used to generate a prompt for a language model, with the specified variables filled in from the provided data.

exaple_prompt = PromptTemplate(
    input_variables=["userInput", "sql_query", "chart_type", "chart_columns"],
    template="Question: {userInput}\nSQL Query: {sql_query}\nChart Type: {chart_type}\nColumns: {chart_columns}",
)

chart_prompt = """You are now generating visualizations based on the User Input and the SQL query provided.
First Identify the visualization type from the following list: bar chart, area chart, scatter chart, line chart, tabulate.
Then Identify the columns to be displayed in the visualization. Pay attention to use only Question & SQL Query as input to generate the visualization.
If you cannot find the visualization type or columns, then just use Chart Type: None and Columns: None

Use the following format:

Question: Question here
SQLQuery: SQL Query here
Chart Type: Identified chart type which user needed to generate
Columns: Identified columns which needs to generate charts

No pre-amble."""

#Creating the Few Shot Prompt Template for the LLM as a one single object
few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=exaple_prompt,
    prefix=chart_prompt,
    suffix="""{input}""",
    input_variables=["input"],
)

#Creating the LLM Chain
chain = few_shot_prompt| llm | TexttoJson()

#Calling LLM Chain
def get_chart_type(question,sql_query):
    text = f"Question: {question}\nSQLQuery: {sql_query}"
    result = chain.invoke(text)
    return result