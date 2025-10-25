from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel
import pickle
from deep_translator import GoogleTranslator

# Load model
with open("Stored_model.pkl", "rb") as f:
    model = pickle.load(f)

# # Initialize translator
# translator = Translator()

# Initialize FastAPI app
app = FastAPI(title="Emotion Detection App (Multilingual)")

# Mount static files (HTML, CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Request schema
class TextInput(BaseModel):
    text: str

@app.get("/")
async def serve_ui():
    """Serve the frontend UI."""
    return FileResponse("static/index.html")

@app.post("/predict")
async def predict_emotion(data: TextInput):
    """Predict emotion, auto-translating non-English text."""
    text = data.text.strip()

    if not text:
        return JSONResponse({"error": "Please enter some text."}, status_code=400)

    try:
        # 🌍 Translate text to English for model prediction
        translated_text = GoogleTranslator(source='auto', target='en').translate(text)
        english_text = translated_text
        source_lang = "auto-detected"

    except Exception as e:
        return JSONResponse({"error": f"Translation failed: {str(e)}"}, status_code=500)

    # 🧠 Predict using model
    try:
        prediction = model.predict([english_text])[0]

        # If the model supports predict_proba, get probabilities
        if hasattr(model, "predict_proba"):
            probabilities = model.predict_proba([english_text])[0]
            labels = model.classes_
            probs = dict(zip(labels, [float(round(p, 3)) for p in probabilities]))
        else:
            labels = list(model.classes_) if hasattr(model, "classes_") else []
            probs = {label: 0.0 for label in labels}
            probs[prediction] = 1.0

        return {
            "original_text": text,
            "translated_text": english_text,
            "source_language": source_lang,
            "emotion": prediction,
            "probabilities": probs
        }

    except Exception as e:

        return JSONResponse({"error": f"Prediction failed: {str(e)}"}, status_code=500)
