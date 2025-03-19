from autobahn.twisted.component import Component, run
from twisted.internet.defer import inlineCallbacks
from autobahn.twisted.util import sleep
import os

from alpha_mini_rug.save_speech import SaveSpeech


audio_recorder = SaveSpeech()


@inlineCallbacks
def record_audio_example(session):
    # Configure the hearing sensor
    info = yield session.call("rom.sensor.hearing.info")
    print("Sensor info:", info)

    # Adjust sensitivity if needed
    yield session.call("rom.sensor.hearing.sensitivity", 1650)
    sensitivity = yield session.call("rom.sensor.hearing.sensitivity")
    print("Current sensitivity:", sensitivity)

    # Ensure output directory exists
    os.makedirs("recordings", exist_ok=True)

    # Example 1: Record for 5 seconds
    yield session.call("rie.dialogue.say", text="I will record for 5 seconds starting now")
    audio_recorder.record_audio("recordings/timed_recording5s.wav", duration=5)

    # Subscribe to audio stream and start recording
    yield session.subscribe(audio_recorder.process_frame, "rom.sensor.hearing.stream")
    yield session.call("rom.sensor.hearing.stream")

    # Wait until recording is complete
    while audio_recorder.recording:
        yield sleep(0.1)

    yield session.call("rie.dialogue.say", text="First recording complete")
    yield sleep(1)

    # Example 2: Record until silence
    yield session.call("rie.dialogue.say", text="Now speak, and I will record until you are silent for 3 seconds")
    audio_recorder.record_audio("recordings/silence_based_recording.wav")

    # Wait until recording is complete
    while audio_recorder.recording:
        yield sleep(0.1)

    yield session.call("rie.dialogue.say", text="Second recording complete")

    # Clean up and exit
    session.leave()


def main(session, details):
    record_audio_example(session)


wamp = Component(
    transports=[
        {
            "url": "ws://wamp.robotsindeklas.nl",
            "serializers": ["msgpack"],
            "max_retries": 0,
        }
    ],
    realm="rie.67daa82a540602623a34bf38",  # Replace with your realm
)

wamp.on_join(main)

if __name__ == "__main__":
    run([wamp])
