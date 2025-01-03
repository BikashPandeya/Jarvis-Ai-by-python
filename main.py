import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os
import time
import os
import google.generativeai as genai
# from elevenlabs import generate, play
import os
# from elevenlabs import ElevenLabs
# from playsound import playsound

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "c09972acf0e643c48112f9b70e5b9102"

def speak_old(text):
    engine.say(text)
    engine.runAndWait()
    
def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')
    

    # Initialize pygame mixer
    pygame.mixer.init()
    # Load the mp3 file
    pygame.mixer.music.load("temp.mp3")
    # Play the music
    pygame.mixer.music.play()

    # Keep the program running while the music plays
    while pygame.mixer.music.get_busy():
                time.sleep(0.1)  # Add a slight delay to reduce CPU usage
    pygame.mixer.music.unload()
    os.remove('temp.mp3')
   

# # Set your Eleven Labs API key
# os.environ["ELEVEN_API_KEY"] = "sk_01274f2f77870c69e98ad93f8b0c228878e686b68ea7a668"

# # Initialize ElevenLabs API with your API key
# elevenlabs = ElevenLabs(api_key=os.getenv("ELEVEN_API_KEY"))

# # Function to generate and play speech
# def speak(text):
#     # Generate the audio (choose voice, model, etc.)
#     audio = elevenlabs.generate_audio(text=text, voice="Bella")  # Choose voice
#     audio.save("output_audio.mp3")  # Save the audio to a file
    
#     # Play the generated audio
#     playsound("output_audio.mp3")

# # Test the speak function
# speak("Hello, I am your Eleven Labs assistant.")

   
        
    
# def aiprocess(command):
#     client = OpenAI(
#         api_key="YOUR_API_KEY"
#     )

#     completion = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[
#             {"role": "system", "content": "You are a virtual assistance named jarvis skilled in general tasks like Alexa and Google cloud . Give short responses,please"},
#             {
#                 "role": "user",
#                 "content": command
#             }
#         ]
#     )

#     return print(completion.choices[0].message)   
    
def aiprocess(command):

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
   

    while True:
        
        user_input = command
        
        chat_session = model.start_chat(
            history = history
        )
        
        response = chat_session.send_message(user_input)

        model_response = response.text
        
        print()
        
        history.append({"role": "user" , "parts": [user_input]})
        history.append({"role": "model" , "parts" : [model_response]})
        
        return model_response   
    
     
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com") 
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)       
    elif "news" in c.lower():
        r = requests.get("https://newsapi.org/v2/top-headlines?country=np&apiKey=c09972acf0e643c48112f9b70e5b9102")
       
        # Check if the request was successful
        if r.status_code == 200:
            data = r.json()  # Parse the JSON response
            articles = data.get("articles", [])  # Get the list of articles

            # Extract titles into a list
            titles = [article.get("title", "No title") for article in articles]

            # Print the list of titles
            print(titles)
            speak(titles)
        else:
            print(f"Error: {r.status_code}") 
            
    else:
        #Let openai handle the request 
        output = aiprocess(c) 
        print(output)
        speak(output)
        pass      
        
if __name__ == "__main__":
    speak("..Initializing Jarvis....")
    while True:
        #Listen for the wake "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
        print("Recognizing..")
        
        # recognize speech using Sphinx
        try:
            with sr.Microphone() as source:
                print("Listening")
                audio = r.listen(source , timeout=10, phrase_time_limit=5)
            word = r.recognize_google(audio)
            if (word.lower()=="jarvis"):
                speak("Yes , How can I help you?")
                #listen for command
            
                with sr.Microphone() as source:
                    print("  Jarvis Active....")
                    audio = r.listen(source,timeout=10, phrase_time_limit=5)
                    
                    command = r.recognize_google(audio)
                    
                    processCommand(command)
        except Exception as e:
            print("Error; {0}".format(e))