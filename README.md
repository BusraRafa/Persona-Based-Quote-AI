# 🎭 Persona-Based Quote AI

Persona-Based Quote AI is a Python-based project that generates AI-powered responses and quotes using persona-driven prompt engineering.  
The system customizes AI behavior based on predefined personas to produce structured and context-aware outputs.

---

## 🚀 Overview

This project focuses on **persona-based AI response generation**, where different personalities influence how the AI responds to user input.

It is useful for:
- AI-generated quotes
- Persona-based chat systems
- Prompt engineering experiments
- Creative AI response generation

---

## 📂 Project Structure
```
Persona-Based-Quote-AI/
│── prompt.py # Core persona definitions and prompt engineering logic
│── new_app.py # Main application (latest working version)
│── shahin_app.py # Experimental / alternate version of the app
```

---

## 🧠 How It Works

1. `prompt.py` defines different AI personas and response styles  
2. `new_app.py` takes user input and sends it to the AI model  
3. The AI responds based on the selected persona rules  
4. Output is returned as a structured quote or response  

---

## 🛠️ Tech Stack

- Python 🐍  
- OpenAI API / LLM integration  
- Prompt Engineering  
- Persona-based AI design  

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/BusraRafa/Persona-Based-Quote-AI.git
cd Persona-Based-Quote-AI
```

```
pip install -r requirements.txt
```
3. Add your API key:
```
OPENAI_API_KEY=your_api_key_here
```
## ▶️ Running the App

Run the main version:
```
python new_app.py
```
Or try experimental version:
```
python shahin_app.py
```

## 🧪 File Roles
```
prompt.py → Persona definitions + prompt logic
new_app.py → Main production app
shahin_app.py → Experimental testing version
```

