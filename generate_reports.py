import requests

# Function to fetch data from Hugging Face model hub and compile top 10 downloaded models
def fetch_top_downloaded_models():
    url = "https://huggingface.co/api/models" # Adjust the URL if necessary

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        top_downloaded_models = sorted(data, key=lambda x: x['downloads'], reverse=True)[:10]

        for model in top_downloaded_models:
            print(f"Model: {model['modelId']}, Downloads: {model['downloads']}")
    else:
        print("Failed to fetch data from Hugging Face model hub")
if _name_ == "_main_":
    fetch_top_downloaded_models()
