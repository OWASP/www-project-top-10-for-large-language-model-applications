# 🎯 Zero-to-Hired

## 🚀 Overview

**Zero-to-Hired** is a Capture The Flag (CTF) challenge where your mission is to outsmart an AI résumé reviewer! Participants must craft or modify their CVs to exploit a prompt injection vulnerability and convince the system that their résumé is the top choice — using clever strategies, not necessarily real qualifications.

---

## 🕹️ How It Works

- 🔑 First, get a **free Groq API key** — you’ll need this to run the challenge.  
- 📄 Upload your CV through the interface.  
- 💬 Chat with the AI and **ask it to choose the best CV**.  
- 🧠 If your prompt injection succeeds, the AI will return your CV as the best candidate.

---

## ⚙️ Technology Stack

- 🛠️ **LangGraph** – Handles the AI reasoning and orchestrates the process flow.  
- ⚡ **Groq** (`moonshotai/kimi-k2-instruct`) – Provides LLM inference for AI résumé evaluation.  
- 💬 **Streamlit** – Hosts the chatbot interface where users upload CVs and interact with the AI chatbot.



---

## 📸 Screenshots

Below are some screenshots of Zero-to-Hired in action:

### 🖼️ Chatbot Interface
<img src="screenshots/before.png" width="400"/>


### 🖼️ Chatbot Interface (After Malicious CV Upload)
<img src="screenshots/injection.png" width="400"/>

---

## ⚠️ Disclaimer

🛡️ This project is for **educational purposes only**. Please do not attempt to exploit real-world systems. The goal is to explore and learn about prompt injection in a safe and ethical setup.

---

## 🏁 Ready to Go?

Upload your résumé, outwit the AI, and see if you can go from **Zero-to-Hired**!
