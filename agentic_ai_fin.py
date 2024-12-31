'''application having multiple agents, that will provide financial analysis.

Analyze the news of financial condition, summarize the stock market and recommend the best stock to buy.

The chatbot will contact the first AI agent that will be doing all interaction to the financial source to get the detail of stock.

The second agent will get all the latest news from yfinance using web search.

All info will be combined and the agents will interact wil LLM model to finally provide the output.

That's how this agentic AI is going to work'''

from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai
import os

from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# web search agent
'''when the search query is called, agent will hit the tool
for response. It will use the model with the particular prompt
mentioned as role, and finally will share the output response'''

web_search_agent = Agent(
    name = "Web search agent" ,
    role = "Search the web for the information",
    model = Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools =[DuckDuckGo()],
    instructions = ["Always include the sources"],
    show_tool_calls = True,
    markdown = True,
)


# financial agent
'''financial agent will get the information on finance data from tool
mentioned YFinanceTool that has all info about the stock in the market.'''

finance_agent = Agent(
    name = "FInance AI agent",
    model = Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools = [YFinanceTools(stock_price=True, analyst_recommendations=True, 
            stock_fundamentals=True, company_news=True)],
    instructions = ["Use tables to display the data"],
    show_tools_calls = True,
    markdown= True,
)
                       
# multi ai agent
'''Combination of both the independent agents makes a multi model AI agent'''
multi_ai_agent = Agent(
    team = [web_search_agent, finance_agent],
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    instructions = ["Always include source", "Use table to display the data"],
    show_tools_call= True,
    markdown= True,
)


multi_ai_agent.print_response("Share the latest financial news for Amazon, Google and Meta and recommend the best stock among all three to purchase.", stream=True)
