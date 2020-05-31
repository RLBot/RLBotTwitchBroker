from pathlib import Path

from rlbot_twitch_broker_client.defaults import STANDARD_TWITCH_BROKER_PORT

from .src.twitch_broker import TwitchAuth, MutableBrokerSettings, TwitchBroker

if __name__ == '__main__':

    # Follow https://dev.twitch.tv/docs/irc/guide/ to get an oauth token, and just save it in a file
    # in this same directory.
    with open(Path(__file__).parent / 'twitch.oauth.txt', 'r') as oauth_file:
        oauth = oauth_file.read()
    settings = MutableBrokerSettings(num_old_menus_to_honor=2, pause_on_menu=True)

    # Open up http://127.0.0.1:7307/static/chat_form.html if you want to send test commands without
    # connecting to twitch.
    # Open the overlay (the html file in overlay_folder to see what actions you can enter in chat.
    # You can open it via IntelliJ's html preview, or an OBS scene, both of these start a little mini server
    # so it can access the json successfully. Opening the overlay file directly in a web browser won't work.
    twitch_broker = TwitchBroker(Path(__file__).parent / 'overlay', TwitchAuth('tarehart', oauth, '#tarehart'), settings)
    twitch_broker.run_loop_with_chat_buffer(STANDARD_TWITCH_BROKER_PORT)
