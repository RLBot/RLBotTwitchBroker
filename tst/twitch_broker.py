from pathlib import Path

from rlbot_twitch_broker.run import run_twitch_broker
from rlbot_twitch_broker_client.defaults import STANDARD_TWITCH_BROKER_PORT

if __name__ == '__main__':

    run_twitch_broker(STANDARD_TWITCH_BROKER_PORT, Path(__file__).parent / 'overlay')
