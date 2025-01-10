# Financial Agent

## Overview
Financial Agent is an AI-powered multi-agent platform designed to provide real-time financial insights and web-based information retrieval. Built using advanced language models like **Groq** and tools such as **YFinanceTools** and **DuckDuckGo**, this platform enables seamless financial analysis and data exploration.

With specialized agents collaborating for better efficiency, the platform is ideal for financial analysts, researchers, and developers seeking real-time market insights and reliable data from the web.

---

## Features
1. **Web Search Agent**:
   - Uses **Groq's LLM** and **DuckDuckGo** to fetch real-time web-based information.
   - Provides sources for all retrieved data to ensure accuracy and reliability.

2. **Finance Agent**:
   - Powered by **Groq** and **YFinanceTools** to fetch financial data.
   - Offers stock prices, analyst recommendations, company news, key financial ratios, and stock fundamentals.
   - Presents data in structured tables for easy interpretation.

3. **Playground Interface**:
   - A web-based interactive interface built using **phi.api** and **FastAPI**.
   - Allows seamless interaction with AI agents and real-time query handling.

---

## Requirements
To run the project, ensure you have the following:
- **Python 3.8+**
- **Required Python Packages**:
  - `phidata`
  - `python-dotenv`
  - `yfinance`
  - `packaging`
  - `duckduckgo-search`
  - `fastapi`
  - `uvicorn`
  - `groq`
  - `openai`

---

## Setup Instructions

### Clone the Repository
```bash
git clone https://github.com/yourusername/financial-agent.git
cd financial-agent
```

### Set Up Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Configure API Keys
1. Create a `.env` file in the root directory.
2. Add the following keys:
   ```plaintext
   GROQ_API_KEY=gsk_your_groq_api_key
   PHI_API_KEY=phi_your_phi_api_key
   OPENAI_API_KEY=sk_your_openai_api_key
   ```
3. Replace the placeholders (`your_groq_api_key`, etc.) with your actual API keys.

---

## Run the Application

### Execute the Financial Agent Script
```bash
python financial_agent.py
```

### Launch the Playground Interface
```bash
uvicorn playground:app --reload
```

### Open the Browser
Navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000) to access the interactive Playground App.

---

## Usage
- **Web Search Agent**:
  - Use for real-time web-based queries with reliable sources.
- **Finance Agent**:
  - Use to analyze financial data such as stock prices, ratios, and company news.
- **Playground Interface**:
  - Interact with agents seamlessly and retrieve actionable insights.

---

## Contributing
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature"
   ```
4. Push the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## License
None.

---

## Acknowledgments
- [phi.ai](https://phi.ai)
- [Groq](https://groq.com)
- [YFinanceTools](https://github.com/ranaroussi/yfinance)
- [DuckDuckGo](https://duckduckgo.com)

---

## Contact
For questions or feedback, feel free to contact:
- **Mohammad Ali**
- **Email**: [Mohammad.ali2601@gmail.com]
- **GitHub**: [https://github.com/zain88088](https://github.com/zain88088)
"""