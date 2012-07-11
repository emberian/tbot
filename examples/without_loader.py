# By default, the tbot master runs a loader around your tbot, to reduce
# boilerplate. Here is that boilerplate.

import tbot

tbot.connect('ipc:///tmp/tbot_master', 'without_loader')

@tbot.listen(event='message')
def log(event):
    print("{0}: {1}".format(event.sender, event.body))

tbot.mainloop()
# And now we spin in an infinite loop, waiting for events and responding to
# them. Not a lot of boilerplate, I will admit, but it takes the focus away
# from writing awesome IRC bots.
