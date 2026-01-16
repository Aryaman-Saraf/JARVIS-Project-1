from google import genai
import os

# Initialize the client
os.environ["GOOGLE_API_KEY"] = "AIzaSyAnl_mNslbUlQ2n9xRA3KvCbNzPAT_vsHM" 
client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])

def get_ai_response(user_query):
    try:
        # 'gemini-flash-latest' is an alias in your list that points to the 
        # current active Flash model (likely maintaining the Free Tier).
        response = client.models.generate_content(
            model="gemini-flash-latest", 
            contents=f"You are Jarvis, a helpful and witty virtual assistant. Keep your answers concise (under 2 sentences). User: {user_query}"
        )
        return response.text
    except Exception as e:
        print(f"AI Error: {e}")
        return "I'm sorry, I couldn't process that request."