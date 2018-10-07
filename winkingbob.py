from time import sleep
import random
from espeak import espeak 
from gpiozero import Button
import subprocess

stories = ['excuse me what are you doing here?.',
           'your mum is a skeleton',
           'muah ha ha',
           'do a silly dance and you can have some sweets',
           'cackle cackle cackle',
           'happy halloween',
           'trick or treat! have some sweets',
           'listen or i will come back to haunt you forever',
           'your dad is a demon',
           'have a nice day',
           'high five the person nearest to you and you can have some sweets',
           'do you like my new hair style?',
           'listen and obey',
           'liking the outfit little dude',
           'ow stop poking me',
           'oi! what on earth are you doing on my property. this is ghost territory, only to be used by ghosts and the walking dead      ,especially the king of the dead, so leave!                                                                              wait you haven\'t got your sweets yet',                                                
           'hello how has your day been because it is probably going to start to be scary right about now. if you like sweets you betta hang around to get some. ha ha ha or i will posess your sole for eternity! ha ha ha ha ha!',
           'i am here to scare you and your cute little pets',       
           ]
button = Button(17)

espeak.synth("hello my name is Winking Bob and i am now alive")


while True:
    try:
        button.wait_for_press()
        espeak.synth("hello my name is Winking Bob")
        sleep(2)
        subprocess.Popen(["espeak", "-p 8 -s 1 -k 20 -ven mb-en1", "-stdout | aplay",(random.choice(stories))])    
        sleep(1)

    except KeyboardInterrupt:
        break
