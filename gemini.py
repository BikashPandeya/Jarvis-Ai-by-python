import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create the model
generation_config = {
  "temperature": 0,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
  system_instruction="You are a virtual assistance named jarvis skilled in general tasks like Alexa and Google cloud . Give short responses,please",
)
history = []
print("Bot ::  Hello ,How can I help you:")

while True:
    
    user_input = input("You:: ")
    
    chat_session = model.start_chat(
         history = history
    )
    
    response = chat_session.send_message(user_input)

    model_response = response.text
    
    print("Bot::",model_response)
    print()
    
    history.append({"role": "user" , "parts": [user_input]})
    history.append({"role": "model" , "parts" : [model_response]})
    print(type(model_response))