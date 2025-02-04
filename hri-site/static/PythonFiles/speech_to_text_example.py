from autobahn.twisted.component import Component, run
from twisted.internet.defer import inlineCallbacks
from autobahn.twisted.util import sleep
from time import time

import cv2 as cv
import numpy as np
import wave
import os

from alpha_mini_rug.speech_to_text import SpeechToText


audio_processor = SpeechToText() # create an instance of the class

# don't change these values
audio_processor.silence_time = 0.5 # parameter set to indicate when to stop recording
audio_processor.silence_threshold2 = 100 # any sound recorded bellow this value is considered silence
 
audio_processor.logging = False # set to true if you want to see all the output


@inlineCallbacks
def STT_continuous(session):
    info = yield session.call("rom.sensor.hearing.info")
    print(info)
   
    yield session.call("rom.sensor.hearing.sensitivity", 1650)

    yield session.call("rie.dialogue.config.language", lang="en")
    yield session.call("rie.dialogue.say", text="Say something")
    
    print("listening to audio")
    yield session.subscribe(audio_processor.listen_continues, "rom.sensor.hearing.stream")
    yield session.call("rom.sensor.hearing.stream")

    while True:
        if not audio_processor.new_words:
            yield sleep(0.5)  # VERY IMPORTANT, OTHERWISE THE PROGRAM WILL CRASH
            if time() % 50 == 0:  # every 25 seconds it stops recording
                audio_processor.do_speech = False
                yield session.call("rie.dialogue.say", text="Say something")
                audio_processor.do_speech_recognition = True # start recording again
        else:
            word_array = audio_processor.give_me_words()
            print(word_array[-3:])  # print last 3 sentences

        audio_processor.loop()


@inlineCallbacks
def main(session, details):
    # Define the file path
    output_dir = "output"
    output_file = os.path.join(output_dir, "output.wav")

    # Create the directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Create the file if it doesn't exist
    if not os.path.exists(output_file):
        with open(output_file, "wb") as f:
            f.write(b"")  # Write an empty byte string to create the file

    yield STT_continuous(session)

    session.leave()


wamp = Component(
    transports=[
        {
            "url": "ws://wamp.robotsindeklas.nl",
            "serializers": ["msgpack"],
            "max_retries": 0,
        }
    ],
    realm="rie.67a1cded85ba37f92bb12d56",
)


wamp.on_join(main)

if __name__ == "__main__":
    run([wamp])
