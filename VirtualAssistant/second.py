# Import the necessary libraries
import webbrowser
import pyttsx3
import pygame
import time
import datetime
import random

import speech_recognition as sr

from VirtualAssistant.main import handle_command

# Initialize the speech engine
engine = pyttsx3import webbrowser
import pyttsx3
import os
import datetime
import speech_recognition as sr


engine = pyttsx3.init()

def speak(audio):
    newVoiceRate = 115
    engine.setProperty('rate', newVoiceRate)
    engine.say(audio)
    engine.runAndWait()

def listen():
  r = sr.Recognizer()
  with sr.Microphone() as source:
    print('Listening...')
    audio = r.listen(source)
  try:
    command = r.recognize_google(audio).lower()
    print(f'You said: {command}\n')
  except sr.UnknownValueError:
    speak('I am sorry, I could not understand what you said. Could you please try again?')
    command = listen()
  return command

def greet():
  hour = int(datetime.datetime.now().hour)

  if hour>=0 and hour<12:
    speak('Good Morning!')
  elif hour>=12 and hour<18:
    speak('Good Afternoon!')
  else:
    speak('Good Evening!')

def time():
  time = datetime.datetime.now().strftime("%I:%M %p")
  speak(f'The current time is {time}')

def date():
  year = int(datetime.datetime.now().year)
  month = int(datetime.datetime.now().month)
  day = int(datetime.datetime.now().day)
  speak(f'Today is {month}/{day}/{year}')

def weather():
  speak('I am not able to check the weather at this time.')

def music():
  speak('What type of music would you like to listen to?')
  music_type = listen()
  webbrowser.open(f'https://www.youtube.com/results?search_query={music_type}')

def search():
  speak('What would you like to search for?')
  search_term = listen()
  webbrowser.open(f'https://www.google.com/search?q={search_term}')

def virtual_assistant(command):
  if 'hello' in command:
    greet()
  elif 'time' in command:
    time()
  elif 'date' in command:
    date()
  elif 'weather' in command:
    weather()
  elif 'music' in command:
    music()
  elif 'search' in command:
    search()
  elif 'exit' in command:
    speak('Goodbye!')
    exit()
  else:
    speak('I am sorry, I did not understand your command. Could you please rephrase your request?')

speak('Hello, I am your virtual assistant. How can I help you today?')

while True:
  command = listen()
  virtual_assistant(command).init()

# Set the rate at which the text should be spoken
engine.setProperty('rate', 120)

# Create a function to say something
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Create a function to play music
def play_music(file):
    # Initialize the pygame mixer
    pygame.mixer.init()
    # Load the music file
    pygame.mixer.music.load(file)
    # Play the music
    pygame.mixer.music.play()

# Create a function to set a timer
def set_timer(duration):
    # Convert the duration to seconds
    duration = int(duration) * 60
    # Loop for the specified duration
    for i in range(duration):
        # Sleep for one minute
        time.sleep(60)
        # Calculate the time remaining
        minutes_remaining = duration - i - 1
        # Speak the time remaining
        speak(f"{minutes_remaining} minutes remaining.")
    # Speak "time's up" when the timer is finished
    speak("Time's up!")

# Create a function to tell the time
def tell_time():
    # Get the current time
    now = datetime.datetime.now()
    # Format the time as a string
    time_str = now.strftime("%I:%M %p")
    # Speak the time
    speak(f"The time is {time_str}.")

# Create a function to set a reminder
def set_reminder(time, message):
    # Convert the time to a datetime object
    reminder_time = datetime.datetime.strptime(time, "%I:%M %p")
    # Calculate the time difference
    time_difference = reminder_time - datetime.datetime.now()
    # Sleep for the time difference
    time.sleep(time_difference.total_seconds())
    # Speak the reminder message
    speak(message)

# Create a function to tell a joke
def tell_joke():
    # Define a list of jokes
    jokes = [
        "Why couldn't the bicycle stand up by itself? Because it was two-tired.",
        "Why did the tomato turn red? Because it saw the salad dressing!",
        "What do you get when you cross a snowman and a vampire? Frostbite.",
        "Why was the math book sad? Because it had too many problems.",
        "Why couldn't the leopard play hide and seek? Because he was always spotted.",
    ]
    # Choose a random joke from the list
    joke = random.choice(jokes)
    # Speak the joke
    speak(joke)

# Create a function to search the web
def search(query):
    # Open a new web browser tab and search for the query
    webbrowser.open(f"https://www.google.com/search?q={query}")
    # Speak the search results
    speak(f"Here are the search results for '{query}'.")
def greeting():
    # Create a list of greetings
    greetings = [
        "Hello! How can I help you today?",
        "Hi! What can I do for you?",
        "Hello!",
        "Hi! How are you?",
        "Hello there!",
        "Hi there!",
        "Hello there!"]
    # Choose a random greeting from the list
    greeting = random.choice(greetings)
    # Speak the greeting
    speak(greeting)
#create a function that listens for user input
def listen():
    # Initialize the speech recognizer
    r = sr.Recognizer()

    # Start listening and try to recognize the speech
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            # If speech is recognized, handle the command
            command = r.recognize_google(audio)
            handle_command(command)
        except sr.UnknownValueError:
            # If speech is not recognized, prompt the user to try again
            speak("I'm sorry, I could not understand what you said. Please try again.")

# Create an infinite loop
greeting()
while True:
    # Prompt the user to enter a command
    command = input("Enter a command: ")

    # Check if the user entered "time"
    if command == "time":
        tell_time()
    # Check if the user entered "joke"
    elif command == "joke":
        tell_joke()
    # Check if the user entered "music"
    elif command == "music":
        play_music("music.mp3")
    # Check if the user entered "timer"
    elif command.startswith("timer"):
        # Extract the duration from the command
        duration = command.split()[1]
        # Set the timer
        set_timer(duration)
    # Check if the user entered "reminder"
    elif command.startswith("reminder"):
        # Extract the time and message from the command
        time, message = command.split(" at ")[1], " ".join(command.split(" at ")[2:])
        # Set the reminder
        set_reminder(time, message)
    # Check if the user entered "search"
    elif command.startswith("search"):
        # Extract the query from the command
        query = " ".join(command.split("search")[1:])
        # Search the web
        search(query)
    # If the command is not recognized, speak an error message
    else:
        speak("Sorry, I didn't understand that.")
