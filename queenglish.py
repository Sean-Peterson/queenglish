import os
import openai
# Import the required module for text
# to speech conversion
from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os

openai.organization = "org-MbdHE411imWBGbOfYcvOw21T"
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message)



# The text that you want to convert to audio
userText = input('Enter your lyrics\n')

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=userText, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("queenglish.mp3")

# Playing the converted file
os.system("mpg321 queenglish.mp3")
