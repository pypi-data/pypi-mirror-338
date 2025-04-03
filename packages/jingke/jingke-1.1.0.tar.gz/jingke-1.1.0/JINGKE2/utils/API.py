import requests
import json
import os
from art import *
from JINGKE2.utils.user import User_creation

def verify_api_key(api_key):
    """
    Verify if the API key is valid by sending a POST request to the Next.js API route
    
    Args:
        api_key (str): The API key to verify
        
    Returns:
        dict: The response from the API
    """
    # API endpoint URL
    url = "https://jing-kev2.vercel.app/api/verify"
    
    # Request headers
    headers = {
        "Content-Type": "application/json"
    }
    
    # Request payload
    payload = {
        "apiKey": api_key
    }
    
    # Send the POST request
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    
    # Parse and return the response
    return response.json()


def Jingke_api_key(apikey):
    result = verify_api_key(apikey)
    if result.get("success"):
        return 200
    else:
        print(f"Error: {result.get('message')}")
        return 404
    
def get_api():
    dire = os.path.join(os.getcwd(),"settings")
    file = os.path.join(dire, "profile.json")
    try:
        with open(file,'r') as f:
            data = json.load(f)
            token = data.get("api")
            return token
    except:
        token = ""       
    if not token:
        print("\nAPI Key not available. (insert your user data) \n")
        User_creation.initialize()

def get_name():
    dire = os.path.join(os.getcwd(),"settings")
    file = os.path.join(dire, "profile.json")
    try:
        with open(file,'r') as f:
            data = json.load(f)
            name = data.get("name")
            return name
    except:
        return None       