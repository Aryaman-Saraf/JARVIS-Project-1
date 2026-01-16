# 🤖 PROJECT JARVIS

PROJECT JARVIS is a **Python-based virtual assistant** that runs in the background and responds to voice commands.  
It can open applications, browse websites, play music, provide news and weather updates, and generate intelligent responses using the **Gemini API**.

---

## 🚀 Features

- 🎙️ Wake word detection (background listening)
- 🖥️ Open desktop applications via voice commands
- 🌐 Open websites on request
- 🎵 Play music
- 📰 Read out the latest news
- ☁️ Provide current weather updates
- 🧠 AI-powered responses using **Gemini API**
- 🔊 Text-to-Speech output
- 🌍 Internet connectivity checks

---

## 🛠️ Tech Stack

- **Language:** Python
- **AI:** Google Gemini API
- **Speech Recognition:** SpeechRecognition
- **Text-to-Speech:** pyttsx3, gTTS
- **Audio Handling:** PyAudio, pygame
- **Wake Word Detection:** openwakeword
- **APIs:** News & Weather APIs
- **Execution:** Runs in background

---

## 📂 Project Structure

JARVIS-Project-1/
│
├── main.py # Main entry point
├── aihandler.py # Gemini AI logic
├── wakeWordDetection.py # Wake word detection
├── audioFunctions.py # Audio input/output
├── internetCheck.py # Internet connectivity check
├── news.py # News fetching logic
├── requirements.txt # Python dependencies
├── README.md # Documentation

yaml
Copy code

---

## 📦 Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/JARVIS-Project-1.git
cd JARVIS-Project-1
2. Create a virtual environment (recommended)
bash
Copy code
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
3. Install dependencies
bash
Copy code
pip install -r requirements.txt
🔑 API Configuration
This project uses the Google Gemini API.

Generate your API key from Google AI Studio

Set the API key as an environment variable:

bash
Copy code
export GEMINI_API_KEY="your_api_key_here"
(Windows)

bash
Copy code
set GEMINI_API_KEY=your_api_key_here
▶️ Usage
Start the assistant by running:

bash
Copy code
python main.py
Say the wake word, then try commands like:

“Open Chrome”

“Play music”

“Tell me the news”

“What’s the weather today?”

📋 Requirements
All required libraries are listed in requirements.txt, including:

SpeechRecognition

PyAudio

pygame

pyttsx3

gTTS

openwakeword

google-genai

requests

⚠️ Notes
A working microphone is required

Internet connection is mandatory for AI, news, and weather features

Best performance in a quiet environment

🔮 Future Enhancements
GUI interface

Multi-language support

Task scheduling

System-level automation

Persistent memory and context

👨‍💻 Author
Aryaman Saraf

📜 License
This project is intended for educational and learning purposes.
Feel free to modify and extend it.

Copy code
