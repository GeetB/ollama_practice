import requests

response = requests.post("http://localhost:11434/api/generate", 
              json={"model": "mistral", "prompt": "What is Generartive AI", "stream": False}
              )

print("Response content:", type(response))

# Check if the response status code is 200 (OK)
if response.status_code == 200:    
    try:
        # Extract the JSON response
        response_json = response.json()

        # Access the "response" key and print it
        if "response" in response_json:
            print("Response:", response_json["response"])
        else:
            print("Error: 'response' key not found in the JSON response.")
    except ValueError:
        print("Error: The server response is not valid JSON.")
else:
    print(f"Error: Server returned status code {response.status_code}")