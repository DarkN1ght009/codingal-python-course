import base64
import requests
from config import HF_API_KEY

API_URL = "https://router.huggingface.co/v1/chat/completions"
HEADERS = {"Authorization": f"Bearer {HF_API_KEY}", "Content-Type": "application/json"}
MODELS = [
    "ZhipuAI/GLM-4V",
    "Qwen/Qwen2.5-VL-72B-Instruct",
    "Qwen/Qwen2.5-VL-32B-Instruct",
    "google/gemma-3-27b-it",
]

def data_url(b: bytes) -> str:
    return "data:image/jpeg;base64," + base64.b64encode(b).decode("utf-8")

def extract_err(r: requests.Response) -> str:
    try:
        j = r.json()
        return j.get("error", {}).get("message") or str(j)
    except Exception:
        return (r.text or "").strip() or r.reason or "Request failed."

def box(title: str, lines: list[str], icon: str):
    w = max(30, len(title) + 4, *(len(x) for x in lines))
    print("\n" + "┌" + "─" * (w + 2) + "┐")
    print(f"│ {icon} {title.ljust(w - 2)} │")
    print("├" + "─" * (w + 2) + "┤")
    for x in lines:
        print(f"│ {x.ljust(w)} │")
    print("└" + "─" * (w + 2) + "┘\n")

def caption_single_image():
    image_source = input("🖼️ Enter image filename (default: test.jpg): ").strip() or "test.jpg"
    try:
        with open(image_source, "rb") as f:
            img = f.read()
    except Exception as e:
        box("File Error", [f"Could not load: {image_source}", f"Reason: {e}"], "❌")
        return

    # Convert image to data URL format for the Vision API
    img_url = data_url(img)

    # Base payload structured for Hugging Face Chat Completions Vision API
    base_payload = {
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Describe this image in a short, clear sentence."},
                    {"type": "image_url", "image_url": {"url": img_url}}
                ]
            }
        ],
        "max_tokens": 60,
        "temperature": 0.2  # Fixed from 8.2 (which would cause extreme randomness/hallucinations)
    }
    
    print( \n"🤖 Querying HuggingFace Vision Models...\n")

    for model in MODELS:
        payload = dict(base_payload, model=model)
        try:
            r = requests.post(API_URL, headers=HEADERS, json=payload, timeout=120)
        except requests.RequestException as e:
            box(model, [f"Request failed: {e}"], "❌")
            continue
            
        if r.status_code != 200:
            err_msg = extract_err(r)
            box(model, [f"Error {r.status_code}: {err_msg}"], "❌")
            continue
            
        try:
            d = r.json()
            # Standard OpenAI-compatible response parsing
            caption = d["choices"][0]["message"]["content"].strip()
            box(model, [caption], "✨")
        except (KeyError, IndexError, ValueError) as e:
            box(model, [f"Failed to parse response: {e}"], "⚠️")

if __name__ == "__main__":
    caption_single_image()