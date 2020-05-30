from pathlib import Path

from rlbot_twitch_broker.twitch_broker import run_twitch_broker, TwitchAuth
from rlbot_twitch_broker_client.defaults import STANDARD_TWITCH_BROKER_PORT

if __name__ == '__main__':

    # Follow https://dev.twitch.tv/docs/irc/guide/ to get an oauth token, and just save it in a file
    # in this same directory.
    with open(Path(__file__).parent / 'twitch.oauth.txt', 'r') as oauth_file:
        oauth = oauth_file.read()

    run_twitch_broker(STANDARD_TWITCH_BROKER_PORT, Path(__file__).parent / 'overlay',
                      TwitchAuth('tarehart', oauth, '#tarehart'))
