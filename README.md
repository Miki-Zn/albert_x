# albert_x
# Autonomous Web3/Crypto AI Agent 

An autonomous, LLM-powered agent designed for X (Twitter) networking, Alpha discovery, and scam filtering within the Web3 ecosystem. It features a Human-in-the-Loop architecture via a Telegram Bridge for financial decisions and operates on a human-like schedule.

## Core Architecture
- **Intent Classification**: Uses GPT-4o to categorize incoming content (Financial Intent, Alpha Project, or General Networking).
- **Telegram Bridge**: Halts execution and requests manual approval via Telegram whenever financial triggers (OTC, investments, promos) are detected.
- **Alpha Radar**: Automatically tracks high-potential projects based on tokenomics and fundamentals, sending detailed SWOT breakdowns to the admin.
- **Anti-Detect**: Implements randomized delays (jitter) and distinct morning/evening behavior cycles.

## Deployment & Website Integration
The system is built to run autonomously via an automatic daily cron job, functioning as a core backend component within the technical specification for the future website launch. The integration ensures continuous operation and state synchronization using a PostgreSQL database.

## Prerequisites
- Docker and Docker Compose
- API Keys: X (Twitter) API v2, OpenAI API, Telegram Bot Token

## Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/crypto-agent.git](https://github.com/your-username/crypto-agent.git)
   cd crypto-agent

2. Create a .env file in the root directory based on the configuration logic:


X_BEARER_TOKEN=your_token
X_API_KEY=your_key
X_API_SECRET=your_secret
X_ACCESS_TOKEN=your_access
X_ACCESS_SECRET=your_access_secret
OPENAI_API_KEY=your_openai_key
TG_BOT_TOKEN=your_tg_token
TG_ADMIN_ID=your_telegram_id
PROXY_URL=http://your_proxy (optional)
DATABASE_URL=postgresql://user:password@db:5432/crypto_db
