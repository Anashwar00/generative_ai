# generative_ai
## 📁 Files Overview

### Before,Create a .env file in your project folder with the following line:

OPENAI_API_KEY=your_openai_api_key_here


### 1. `chatbot.py` — *Simple Real-Time Chatbot with Logging*

A terminal-based chatbot that interacts with the user in real-time and logs all inputs/outputs to a JSON file.

#### 🔍 Features
- Uses `gpt-4o` via OpenAI API
- Logs:
  - Timestamp
  - User query
  - AI response
  - Token usage
  - Response duration (in ms)
  - Errors (if any)
- Outputs logs to `chat_logs.json`
- Minimal setup, fast execution
# 🧠 AI Chatbot with Context Management

This Python script demonstrates how to build a memory-aware chatbot using OpenAI’s GPT models. It tracks and saves the entire conversation history to maintain context across sessions — simulating more natural, multi-turn dialogue.

---

## 📄 What It Does

- ✅ Remembers past conversations
- ✅ Summarizes old messages to manage token limits
- ✅ Stores and loads context from a local file (`db.json`)
- ✅ Automatically adds system prompts for consistent behavior

This chatbot is ideal for use cases where continuity of conversation matters — such as virtual assistants, helpdesks, or personal AI companions.

---

## 🚀 How It Works

1. **Conversation is loaded** from `db.json` if it exists.
2. If the history is long, it **summarizes older messages** into a brief context.
3. The user asks a question.
4. The question is appended to the context.
5. The model responds, and the answer is added to memory.
6. Updated memory is **saved** for future runs.

---

## 📁 File Breakdown

### `context_management.py`
- Main chatbot logic
- Loads, updates, and saves memory
- Summarizes if message count > 10

### `db.json`
- Stores conversation memory


---
## ⚙️ Setup Instructions

### 1. Install Required Libraries

You need Python 3.7+ and the following Python packages:

```bash
pip install openai 
pip install python-dotenv


