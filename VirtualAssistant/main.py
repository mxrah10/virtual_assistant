import webbrowser
import pyttsx3
import os
import datetime
import pygame
import speech_recognition as sr
import time
import pyaudio
import random
import openai

engine = pyttsx3.init()
openai.api_key = "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"
def speak(audio):
    newVoiceRate = 150
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
def virtual_assistant(command):
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=command,
    temperature=0,
    max_tokens=100,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop=["\n"]
  )
  speak(response.choices[0].text)
  print(response)

speak('Hello, I am your virtual assistant. How can I help you today?')

while True:
  command = listen()
  virtual_assistant(command)
