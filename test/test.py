import requests
import json

def test_ask():
    url = "http://localhost:8000/api/ask"
    
    data = {
        "text": "What's Social Media “relationships” with customers?",
        "chat_history": []  # 空列表作为初始对话历史
    }
    
    headers = {
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.post(url, json=data, headers=headers)
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print("Answer:", result.get("answer"))
            print("Sources:", result.get("sources"))
        else:
            print(f"Error: {response.text}")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_ask()