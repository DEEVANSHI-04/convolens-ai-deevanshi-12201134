# convolens-ai-deevanshi-12201134

## Project Overview
**ConvoLens AI** is an intelligent emotion detection system designed to analyze text and conversations to identify the underlying emotions and sentiments.  
It aims to make communication more empathetic and meaningful by offering **clear, actionable insights** into the emotional tone of conversations.

---
## Problem Statement
In today’s digital world — whether it’s workplace communication, online education, or customer interaction — understanding the *emotional tone* behind messages is crucial.  
However, most systems fail to detect nuanced emotions effectively.  
**ConvoLens AI** bridges this gap by identifying emotions such as **joy, sadness, anger, fear, and happiness**, making interactions more human-aware and context-sensitive.

---
## Solution Summary
**ConvoLens AI** uses Natural Language Processing (NLP) and Machine Learning to predict emotions from text inputs.  
It features:
- A **FastAPI backend** for real-time predictions.  
- A **modern HTML-CSS-JS frontend** for interaction.  
- **Multilingual text translation** (Hindi, Punjabi, Chinese, Spanish, etc.) via Google Translator API.  
- A **dynamic UI** with emotion-based colors, emojis, and interactive charts.
  
---
## Tech Stack
- **Backend:** Python, FastAPI  
- **Frontend:** HTML, CSS, JavaScript, Chart.js  
- **Machine Learning:** Scikit-learn (Logistic Regression pipeline)  
- **Language Translation:** deep_translator (Google Translator)  
- **Visualization:** Chart.js for emotion probability charts  

---

## Project Structure
```
root/
├── static/
│ ├── index.html # Frontend UI + Styles 
├── Stored_model.pkl # Pre-trained emotion detection model
├── main.py # FastAPI backend
├── requirements.txt # Dependencies
└── README.md # Documentation
```

---
## Setup Instructions 
Follow these exact steps to run your project locally.
```bash
# 1. Clone the repository
git clone https://github.com/DEEVANSHI-04/convolens-ai-deevanshi-12201134.git
cd convolens
# 2. Create and activate environment
python -m venv env
env\Scripts\activate   # (use source env/bin/activate for macOS/Linux)

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the FastAPI server
uvicorn main:app --reload
```
---
## Deployment
Currently, the app can be run locally using the setup steps above.

---
## Demo Video 
**YouTube Link:**
https://youtu.be/5zeoV2fxh8Y

---
## ✨ Features

🌍 Multilingual Input Support — Users can enter text in Hindi, Punjabi, Chinese, Spanish,etc.

🧠 AI-Powered Emotion Analysis — Detects emotions like joy, anger, fear, and sadness using ML.

🎨 Dynamic UI Feedback — Changes color and emoji based on predicted emotion.

📊 Graphical Visualization — Pie chart of emotion probabilities using Chart.js.

⚡ Fast & Lightweight — Built with FastAPI for speed and responsiveness.

---
## User Interface:
<img width="704" height="387" alt="Screenshot 2025-10-26 044255" src="https://github.com/user-attachments/assets/a131cae5-ac96-419c-bb1c-370340632af5" />

---

## Input:
<img width="749" height="384" alt="Screenshot 2025-10-26 044430" src="https://github.com/user-attachments/assets/82c01ad4-e471-477a-8c4b-1a8678f630e2" />

---

## Output:
<img width="1074" height="971" alt="Screenshot 2025-10-26 044747" src="https://github.com/user-attachments/assets/df3c5cee-0332-409d-9fc2-8d71a07119c3" />
---

## 🧩 Technical Architecture
Here’s a simplified workflow of the system:
<img width="1536" height="1024" alt="flowchart image" src="https://github.com/user-attachments/assets/6b3555fa-ddf7-41af-81d5-2bd46a3a10d6" />

---

## 🧾 References
[FastAPI Documentation](https://fastapi.tiangolo.com/)

[Scikit-learn](https://scikit-learn.org/stable/)

[Deep Translator Library](https://pypi.org/project/deep-translator/)

[Chart.js](https://www.chartjs.org/)

---

## 🙌 Acknowledgements
Special thanks to the open-source contributors of FastAPI, Scikit-learn, and Deep Translator for enabling such fast development and deployment.
