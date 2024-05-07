from autobahn.twisted.component import Component, run
from twisted.internet.defer import inlineCallbacks

@inlineCallbacks
def main(session, details):
    yield session.call("rom.optional.behavior.play", name="BlocklyStand")
    
    # Command the robot to perform the waving movement with the right arm
    yield session.call("rom.actuator.motor.write",
        frames=[
            # Right arm wave motion
            #! NOTE: The elements of the 'data' dictionary have to always be the same for all the frames even if the value is the same(eg. we have to always have "body.arms.right.upper.pitch" and "body.arms.right.lower.roll" in the dictionary even if the value is the same for all the frames)
            {"time": 0, "data": {"body.arms.right.upper.pitch": -2.5, "body.arms.right.lower.roll": 3,"body.arms.left.upper.pitch": -2.5, "body.arms.left.lower.roll": 3}},
            {"time": 2000, "data": {"body.arms.right.upper.pitch": -2.5, "body.arms.right.lower.roll": 2, "body.arms.left.upper.pitch": -2.5, "body.arms.left.lower.roll": 2}},
            {"time": 2200, "data": {"body.arms.right.upper.pitch": -2.5, "body.arms.right.lower.roll": -1, "body.arms.left.upper.pitch": -2.5, "body.arms.left.lower.roll": -1}},
            {"time": 3200, "data": {"body.arms.right.upper.pitch": -2.5, "body.arms.right.lower.roll": 2, "body.arms.left.upper.pitch": -2.5, "body.arms.left.lower.roll": 2}},
            {"time": 4200, "data": {"body.arms.right.upper.pitch": -2.5, "body.arms.right.lower.roll": -1, "body.arms.left.upper.pitch": -2.5, "body.arms.left.lower.roll": -1}},
            {"time": 5200, "data": {"body.arms.right.upper.pitch": -2.5, "body.arms.right.lower.roll": 2, "body.arms.left.upper.pitch": -2.5, "body.arms.left.lower.roll": 2}},
            {"time": 6200, "data": {"body.arms.right.upper.pitch": -2.5, "body.arms.right.lower.roll": -1, "body.arms.left.upper.pitch": -2.5, "body.arms.left.lower.roll": -1}},
            {"time": 7200, "data": {"body.arms.right.upper.pitch": -2.5, "body.arms.right.lower.roll": 2, "body.arms.left.upper.pitch": -2.5, "body.arms.left.lower.roll": 2}},
            
        ],
        force=True,
        sync=True
    )
    
    yield session.call("rom.optional.behavior.play", name="BlocklyStand")

    session.leave() # Close the connection with the robot
    
 
 
wamp = Component(
    transports=[{
        "url": "ws://wamp.robotsindeklas.nl",
        "serializers": ["msgpack"],
        "max_retries": 0
    }],
    realm="rie.65e5bacfd9eb6cfb396e451c",
)

wamp.on_join(main)

if __name__ == "__main__":
    run([wamp])
