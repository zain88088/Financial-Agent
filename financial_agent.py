from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

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

multi_ai_agent = Agent(
    team = [web_search_agent, finance_agent],
    instructions = ["Always include sources", "Use table to display the data"],
    show_tools_calls = True,
    markdown = True,
)

multi_ai_agent.print_response("Summarize analyst recommendation and share the latest news for TSLA", stream= True)



#You can also make an agent to calculation investment metric agent to calculation how is the current investment opportunity looks like