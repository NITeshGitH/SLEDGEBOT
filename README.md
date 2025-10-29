# Sledge Bot 🏏

A versatile Discord bot that brings the spice of sports sledging to your server! Initially focused on cricket, it's designed to be expandable to other sports. Perfect for gaming communities and sports enthusiasts.

## Features 🌟

### Slash Commands
- **Sledge Players**: Use grouped commands to sledge players with context-specific taunts.
  - `/sledge batter [target]` - Send a savage sledge to a cricket batter.
  - `/sledge bowler [target]` - Roast a cricket bowler with a witty sledge.
- **Smart Targeting**:
  - Prevents users from sledging themselves or any bots (including SledgeBot!).

### Automatic Responses
- **Cricket Bot Integration**: Automatically reacts to messages from a specific cricket game bot.
  - Sledges when a player gets out.
  - Sledges when a defensive shot is played.
  - Sledges when a big hit is registered.
- **Friendly Banter**: Responds to "hi" messages to feel more interactive.

## Setup 🛠️

### Prerequisites
- Python 3.10+
- A Discord Bot Token

### Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd SLEDGEBOT
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate 
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure environment variables:**
    - Create a file named `.env` in the root directory (`SLEDGEBOT/`).
    - Add your Discord bot token to this file:
      ```
      DISCORD_TOKEN=YourBotTokenHere
      ```

5.  **Run the bot:**
    ```bash
    python main.py
    ```
