# A logger will log messages
from __future__ import print_function

from tbot.bot import listen

@listen(event='message')
def log(event):
    print "{0}: {1}".format(event.sender, event.body)

# Wasn't that easy?
