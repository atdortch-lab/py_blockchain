import time

from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback 




pnconfig = PNConfiguration()
pnconfig.subscribe_key = 'sub-c-a27bb07f-10d8-4dc8-90f9-1b14c95a71d7'
pnconfig.publish_key = 'pub-c-efaed2c3-2e24-4681-89bb-3e89a766088a'
pubnub = PubNub(pnconfig)

TEST_CHANNEL = 'TEST_CHANNEL'

class Listener(SubscribeCallback):
    def message(self, pubnub, message_object):
        print(f'\n-- IChannel: {message_object.channel} | Message: {message_object.message}')

class PubSub():
    """
    Handles the publish/subscribe layer of the application.
    Provides communication between the nodes of the blockchain network.
    """
    def __init__(self):
        self.pubnub = PubNub(pnconfig)
        self.pubnub.subscribe().channels([TEST_CHANNEL]).execute()
        self.pubnub.add_listener(Listener())

    def publish(self, channel, message):
        """
        Publish the message object to the channel.
        """
        self.pubnub.publish().channel(channel).message(message).sync()

def main():
    pubsub = PubSub()

    time.sleep(1)

    pubsub.publish(TEST_CHANNEL,{'foo':'bar'})

if __name__ == '__main__':
    main()