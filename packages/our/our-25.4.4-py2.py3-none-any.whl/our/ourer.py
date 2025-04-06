
import requests

BASE_URL = "https://rawpasteme.vercel.app/api/pastes"

def upload(content, extension=".txt", description=None, owner=None):
    url = f"{BASE_URL}"

    data = {
        "content": content,
        "extension": extension
    }

    if description:
        data["description"] = description
    if owner:
        data["owner"] = owner

    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()

        paste_data = response.json()
        paste_id = paste_data["id"]
        paste_url = paste_data["url"]

        print(f"Success, the content urI: {paste_url}")
        return paste_id

    except requests.exceptions.RequestException as e:
        print(f"Error uploading content: {e}")
        return None
    except ValueError as e:
        print("error Cannot decode JSON:", e)
        print("Text:", response.text) 
        return None

def get(paste_id):
    url = f"https://rawpasteme.vercel.app/api/pastes?id={paste_id}"

    try:
        response = requests.get(url)
        response.raise_for_status()

        paste_data = response.json()
        return paste_data["content"]

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None
    except ValueError as e:
        print("Cannot Decode JSON:", e)
        print("Text:", response.text)
        return None