import webbrowser
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
  virtual_assistant(command)
