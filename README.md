# 🤖 PROJECT JARVIS  
### AI-Powered Voice Assistant (Python + Gemini API)

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/AI-Google%20Gemini-orange" />
  <img src="https://img.shields.io/badge/Voice%20Assistant-Background%20Service-green" />
  <img src="https://img.shields.io/github/stars/Aryaman-Saraf/JARVIS-Project-1?style=social" />
  <img src="https://img.shields.io/github/forks/Aryaman-Saraf/JARVIS-Project-1?style=social" />
</p>

---

## 🚀 Overview

**PROJECT JARVIS** is a **background-running, AI-powered virtual assistant** built entirely in **Python**.  
It listens for a wake word, processes voice commands, and performs real-world actions such as opening applications, browsing the web, playing music, and delivering real-time news and weather updates — all powered by **Google Gemini AI**.

This project demonstrates **systems programming, voice interfaces, API integration, and AI orchestration**.

---

## 🎯 Key Capabilities

- 🎙️ **Always-On Wake Word Detection**
- 🧠 **Natural Language Understanding (Gemini AI)**
- 🖥️ **Application Automation**
- 🌐 **Website Navigation**
- 🎵 **Music Playback**
- 📰 **Live News Updates**
- ☁️ **Real-Time Weather Information**
- 🔊 **Text-to-Speech Responses**
- 🌍 **Network Awareness (Offline Handling)**

---

## 🧠 Tech Stack

| Category | Tools |
|--------|------|
| Language | Python |
| AI | Google Gemini API |
| Speech Recognition | SpeechRecognition |
| Text-to-Speech | pyttsx3, gTTS |
| Audio | PyAudio, pygame |
| Wake Word | openwakeword |
| APIs | News & Weather APIs |

---

## 🎬 Demo

> ⚠️ *Add your demo GIF here after recording*

```md
![JARVIS Demo](assets/jarvis-demo.gif)
📌 Suggested demo ideas

Saying wake word → “Open Chrome”

Asking for news

Asking for weather

AI conversation response

📂 Project Architecture
text
Copy code
JARVIS-Project-1/
│
├── main.py                 # Application entry point
├── aihandler.py            # Gemini AI request/response handling
├── wakeWordDetection.py    # Wake word listener
├── audioFunctions.py       # Speech input/output
├── internetCheck.py        # Network status detection
├── news.py                 # News API integration
├── requirements.txt        # Dependencies
└── README.md               # Documentation
⚙️ Installation
1️⃣ Clone Repository
bash
Copy code
git clone https://github.com/Aryaman-Saraf/JARVIS-Project-1.git
cd JARVIS-Project-1
2️⃣ Setup Virtual Environment
bash
Copy code
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
3️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
🔑 Environment Configuration
Set your Gemini API Key:

bash
Copy code
export GEMINI_API_KEY="your_api_key_here"
Windows

bash
Copy code
set GEMINI_API_KEY=your_api_key_here
▶️ Running the Assistant
bash
Copy code
python main.py
🗣️ Example Commands:

“Open Chrome”

“Play music”

“Tell me today’s news”

“What’s the weather?”

🧪 Skills Demonstrated (Resume-Ready)
✔️ Voice Interface Engineering

✔️ AI Integration (LLM APIs)

✔️ Real-Time Event Handling

✔️ System Automation

✔️ Modular Python Architecture

✔️ Audio Processing

✔️ Background Services

🔮 Future Roadmap
GUI Dashboard

Multi-language support

Custom wake words

Persistent conversation memory

OS-level automation (screenshots, shutdown, etc.)

👨‍💻 Author
Aryaman Saraf
Python Developer | AI Enthusiast | Systems Builder

🔗 GitHub: https://github.com/Aryaman-Saraf

⭐ Support
If you find this project useful:

🌟 Star the repository

🍴 Fork it

🐛 Open issues

📢 Share feedback

📜 License
This project is released for educational and personal use.