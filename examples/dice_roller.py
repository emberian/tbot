# This will listen for lines starting with '!roll', and roll dice.

import random
import re

from tbot.bot import listen

pattern = "(\d+)d(\d+)"

def diceroll(number, sides):
    return [random.randint(1, sides) for _ in range(number)]

@listen(trigger='roll')
def roll(event):
    # event.message does not include any leading whitespace or the '!roll'
    msg = event.message
    matches = re.findall(pattern, msg)
    # Returning a non-string is fine if it can be str()'d
    return [diceroll(int(num), int(sides)) for num, sides in matches]
