import random


def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hello Fellow Tafrinite!\nHope you have a good time!'

    if p_message == 'roll':
        return str(random.randint(1,6))

    if p_message == 'toss':
        return str(random.choice(['Odd','Even']))

    if p_message == '!help':
        return '`Type Hello for a Hello response\nRoll to roll a dice\nToss to toss a coin\nNone of the commands are Case Sensitive`'

    #return 'I didn\'t understand what you wrote. Try typing "!help".'
