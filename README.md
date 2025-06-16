# 🤖 Jarvis AI (Python Voice Assistant)

Jarvis is a Python-based voice assistant that leverages advanced AI models (Google Gemini, OpenAI GPT, ElevenLabs) to help you with daily tasks, answer questions, play music, and more—all through natural voice commands.

---

## ✨ Features

- **🎤 Voice Activation:**  
  Say "Jarvis" to wake up your assistant and start interacting hands-free.

- **🧠 AI-Powered Conversations:**  
  Uses Google Gemini or OpenAI GPT models for smart, context-aware responses.

- **🔊 Text-to-Speech:**  
  Replies are spoken aloud using either gTTS (Google Text-to-Speech) or ElevenLabs voices.

- **🌐 Web Automation:**  
  Instantly open popular websites like Google, YouTube, Facebook, and LinkedIn with a command.

- **🎵 Music Playback:**  
  Play your favorite songs from a customizable music library.

- **📰 News Updates:**  
  Get the latest news headlines read out to you.

---

## 🚀 Getting Started

1. **Clone the repository:**
   ```sh
   git clone <repo-url>
   cd Jarvis
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Set up API keys:**  
   Create a `.env` file (already present) and add your API keys for Gemini and ElevenLabs.

4. **Run the assistant:**
   ```sh
   python main.py
   ```

---

## 🛠️ Configuration

- **API Keys:**  
  - `GEMINI_API_KEY` for Google Gemini  
  - `ELEVEN_LABS_API` for ElevenLabs TTS

- **Music Library:**  
  Edit [`musiclibrary.py`](d:/Bikash%20coding/00.%20python%20projects/Jarvis/musiclibrary.py) to add or change songs.

---

## 🗣️ Example Commands

- "Jarvis, open Google"
- "Jarvis, play attention"
- "Jarvis, what's the latest news?"
- "Jarvis, tell me a joke"

---

## 📦 Dependencies

- `speech_recognition`
- `pyttsx3`
- `gtts`
- `pygame`
- `requests`
- `openai`
- `google-generativeai`
- `elevenlabs`

---

## 📄 License

MIT License

---

> **Made with ❤️ by