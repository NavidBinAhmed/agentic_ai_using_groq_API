# Agentic AI Using Groq, OpenAI and Phidata API
Agentic AI application that demonstrates the development of two AI agents for assessing the financial status and latest news for stock market analysis. These AI agents leverage large language models to provide recommendations to users as combined AI agent for buying and selling stocks.

The agents are capable to interact with a wide range of sources, tools and language model to gather and combine information and provide recommendations instantly.


## Agents Workflow

1. **Web Search Agent**: Searches the web for information using DuckDuckGo.
2. **Finance AI Agent**: Retrieves financial data using YFinanceTools.
3. **Multi AI Agent**: Combines the capabilities of the Web Search Agent and Finance AI Agent. Then, interacts with the language model to provide the final output.


## Dependancies and Tools

- `phidata api`
- `groq api`
- `openai api`
- `python-dotenv`
- `yfinance`
- `packaging`
- `duckduckgo-search`
- `fastapi`
- `unicorn`


## Procedure

1. Environment setup, -p will allow the env to store in the exact directory

      ```conda create -p venv python==3.12```

      ```conda activate "H:\AI Projects\Finance AI Agent\venv" ```

2. installing all necessary dependancies and tools
  
      ```pip install -r requirements.txt```

3. Setup the API keys from Groq, Phidata and OpenAI on `.end` file

  - Create a `.env` file in the root directory.
    
  - Add your API keys:
    
            PHI_API_KEY=<your-phidata-api-key>
    
            GROQ_API_KEY=<your-groq-api-key>
    
            OPENAI_API_KEY=<your-openai-api-key>

4. On your .py file, create prompt according to your search criteria using your combined agent name as follows ```multi_ai_agent.print_response```


## Usage

Run the `agentic_ai_fin.py` script to start the agents and get financial analysis and recommendations.

            python agentic_ai_fin.py

Run a multi-agent query: 

Sample Prompt 1:

```multi_ai_agent.print_response("Summarize analyst recommendation and share the latest news for NVDA", stream=True)```


Sample Prompt 2:

`Share the latest financial news for Amazon, Google and Meta and recommend the best stock among all three to purchase.`

The scripts output the latest financial news for Amazon, Google, and Meta, and recommend the best stock to purchase among the three.


## Repository Installation

1. Clone the repository.
   
   ```git clone https://github.com/NavidBinAhmed/agentic_ai_using_groq_openai_phidata_API.git```
   
3. Install the required dependencies

   ```pip install -r requirements.txt```

5. Set up environment variable for API keys

6. run `python agentic_ai_fin.py` file


## Project Structure

- `.env` : Environment variable file storing your API keys
- `agentic_ai_fin.py`: Main script containing the implementation of the agents.
- `requirements.txt` : Lists all dependencies and packages


## Exception Handling

- `openai.OpenAIError: The api_key client option must be set either by passing api_key to the client or by setting the OPENAI_API_KEY environment variable` : used command prompt to set environment variable `set OPENAI_API_KEY="openai-api-key-here" `

- `pydantic_core._pydantic_core.ValidationError: 1 validation error for Agent` : Solved by using the same model for 'Groq' in the model for `multi_agent_ai` function


## License

This project is licensed under the General Public License 3.0.

Any feedback regarding collaboration or suggestion for the improvement is warmly welcome.
