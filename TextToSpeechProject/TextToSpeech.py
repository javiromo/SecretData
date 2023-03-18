#Import package
import sys

try:
    #Try to import pyttsx3 package
    import pyttsx3
except ImportError:
    #If pyttsx3 isn't install, pip install it!
    print('The pyttsx3 module needs to be installed to run this')
    print('program. On Windows, open a Command Prompt and run:')
    print('pip install pyttsx3')
    sys.exit()

#Initialize the TTS engine.
tts = pyttsx3.init()

print('Text To Speech Talker')
print('Text-to-speech using the pyttsx3 module, which in turn uses')
print()
print('Enter the text to speak, or QUIT to quit')

#This is called a While Loop, basically it loops through until the if command is true.
#In this case, the if command is true if the user inputs QUIT, then it closes the loop
while True:
    text = input('> ')

    if text.upper() == 'QUIT':
        print('Goodbye')
        sys.exit()

    tts.say(text) #Add some text for tts engine to say
    tts.runAndWait() #Make the TTS engine say it