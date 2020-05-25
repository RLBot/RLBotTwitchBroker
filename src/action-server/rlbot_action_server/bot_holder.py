from rlbot_action_server.bot_action_broker import BotActionBroker


print('initializing _broker as None')
_broker: BotActionBroker = None

def set_bot_action_broker(broker: BotActionBroker):
    global _broker
    print(f'setting broker to {broker}')
    _broker = broker

def get_bot_action_broker() -> BotActionBroker:
    return _broker
