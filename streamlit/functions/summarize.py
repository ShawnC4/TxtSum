import requests

def call_summarize_endpoint(text):
    url = "http://127.0.0.1:8000/predict"
    params = {"text": text}
    headers = {"accept": "application/json"}
    response = requests.post(url, params=params, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        return {"Err": f"{response.status_code} - {response.text}"}