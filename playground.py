from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import phi.api
from dotenv import load_dotenv

import os
import phi
from phi.playground import Playground, serve_playground_app
load_dotenv()

phi.api = os.getenv("PHI_API_KEY")

#Web search agent
web_search_agent = Agent(
    name = "Web Search Agent", #name of the agent
    role = "Search the web for the information", #role of the agent 
    model = Groq(id = "llama-3.3-70b-versatile"),#llm model web agent will use, every agent will use a llm model which will use the data provided from the tools we use for eg. duckduckgo
    tools = [DuckDuckGo()], #tools used for searching
    instructions = ["Always include sources"],
    show_tools_calls = True,
    markdown = True,
)

#Financial Agent
finance_agent = Agent(
    name = "Finance AI agent",
    model = Groq(id = "llama-3.3-70b-versatile"),#This model is going to interact with the tool
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news = True, key_financial_ratios= True)],#It has all the information about any stock
    instructions = ["Use tables to display the data"],
    show_tools_calls = True,#What tools are we trying to access
    markdown = True,
)

app = Playground(agents = [finance_agent, web_search_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", reload = True)