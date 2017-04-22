import time
import os
import sys
import configparser
config = configparser.ConfigParser()
config.readfp(open(r'config.txt'))
print('''###########################################
#           Welcome to Ryan               #
#   The Smart Mirror personal assistant   #
#     Created by Jamie Turner 2017        #
###########################################''')

time.sleep(0.3)
print('''
Setting up should only take a few minutes''')
time.sleep(0.3)
print('''
Installing dependencies''')
os.system("sudo pip install pyaudio speechrecognition audioop")
import pyaudio
import wave
import audioop
time.sleep(0.3)
print('''
Dependencies succsessfully installed''')
time.sleep(0.3)
conf = input('Enter Name:')
config['Info']['Name'] = ('"' + str(conf) + '"')
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
               channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)
input1 = input('''Next we need to take an audio sample of silence

Press enter and be as quiet as possible while we listen''')
print('Listening...')

rms = 0
rms2 = 0
for x in range(4):
    for x in range(100):
        data = stream.read(CHUNK)
        rms = audioop.rms(data,2)
    rms2 = rms + rms2
conf = rms2/4
print('''Finished listening
Silence set to ''' + str(conf) + ' in config file')

config['Audio']['Silent Volume'] = ('"' + str(conf) + '"')

input1 = input('''Next we need to take an audio sample of speaking

Press enter and repeat the sentence on screen until we have finished listening''')
print ('''Repeat:
The quick brown fox jumped over the lazy dog''')

print('Listening...')

rms = 0
rms2 = 0
for x in range(20):
    for x in range(20):
        data = stream.read(CHUNK)
        rms = audioop.rms(data,2)
    rms2 = rms + rms2
conf = rms2/20
print('''Finished listening
Speaking set to ''' + str(conf) + ' in config file''')
config['Audio']['Speaking Volume'] = ('"' + str(conf) + '"')


input1 = input('''Change Ryan's name [Y/N]''')
conf = 'Ryan'
if input1 == 'Y' or input1 == 'y':
    name = input('''What would you like to Ryan's name too''')
    print('''Changing Ryan's name to ''' + conf + ' in config file')
config['Ai']['Name'] = ('"' + str(conf) + '"')
with open('config.txt', 'w') as configfile:
    config.write(configfile)
print('''Basic Config Setup''')







    
