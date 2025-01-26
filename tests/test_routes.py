import requests

BASE_URL = "http://localhost:8000"

def add_texts(texts):
    response = requests.post(f"{BASE_URL}/add_texts/", json={"texts": texts})
    return response.json()

def search(query):
    response = requests.get(f"{BASE_URL}/search/", params={"query": query})
    return response.json()

if __name__ == "__main__":
    # Example usage
    print(add_texts(["Hello", "World"]))
    print(search("Hello"))
