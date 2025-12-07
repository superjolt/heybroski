def request_wispr(session, apikey, audio):
    response = session.post(
        "https://api.flowvoice.ai/api/v1/dash/api",
        headers={
            "Authorization": f"Bearer {apikey}",
            "Content-Type": "application/json"
        },
        json={
            "audio": audio,
            "properties": {}
        }
    )
    
    # Check status code
    if response.status_code != 200:
        print(f"API error: {response.status_code}")
        print(f"Response: {response.text}")
        response.raise_for_status()
    
    # Check if response has content
    if not response.text:
        print("API returned empty response")
        return {"error": "Empty response from API"}
    
    try:
        return response.json()
    except Exception as e:
        print(f"Failed to parse JSON: {e}")
        print(f"Response text: {response.text}")
        return {"error": str(e), "raw_response": response.text}
