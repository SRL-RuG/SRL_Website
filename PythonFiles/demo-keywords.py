from autobahn.twisted.component import Component, run
from twisted.internet.defer import inlineCallbacks
from autobahn.twisted.util import sleep

@inlineCallbacks
def main(session, details):
	question = "Is Paul a good prof?"
	keywords = ["yes", "sure", "yeah", "super", "best", "definitely"]
	global sess
	sess = session

	@inlineCallbacks
	def on_keyword(frame):
		global sess
		c = frame["data"]["body"]["certainty"]
		print("certainty ",c, ": ",frame)
		if ("certainty" in frame["data"]["body"] and
			frame["data"]["body"]["certainty"] > 0.45):
				yield sess.call("rie.dialogue.say_animated",
						text="I agree, Paul is a good prof")
				yield sess.call("rom.optional.behavior.play", name="BlocklyHappy")

	yield session.call("rie.dialogue.config.language", lang="en")
	yield session.call("rie.dialogue.keyword.language", lang="en")
	yield session.call("rie.dialogue.say_animated",
						text=question)
	yield session.call("rie.dialogue.keyword.add",
						keywords=keywords) #["yes", "definitely"])
	yield session.subscribe(on_keyword, "rie.dialogue.keyword.stream")
	yield session.call("rie.dialogue.keyword.stream")

	# wait 20 seconds for we close the stream
	yield sleep(20)
	yield session.call("rie.dialogue.say", text="Time's up. I'm leaving")
	yield session.call("rie.dialogue.keyword.close")
	yield session.call("rie.dialogue.keyword.clear")

	session.leave() # Close the connection with the robot

wamp = Component(
	transports=[{
		"url": "ws://wamp.robotsindeklas.nl",
		"serializers": ["msgpack"],
		"max_retries": 0
	}],
	realm="rie.6621350994f6248b6e0d18f0",
)

wamp.on_join(main)

if __name__ == "__main__":
	run([wamp])