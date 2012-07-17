"""Common IRC and event dispatching for both master and individual mode.

The connection to IRC and event dispatching is identical between a master and an
individual tbot. This core functionality is provided here."""

from router import EventRouter

class Event(object):
    """An IRC Event.

    Tracks various information about an IRC event, such as what it is (a
    privmsg, notice, nick change, etc), who sent it, and when it was received.
    """
    pass
