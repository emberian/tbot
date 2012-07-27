"""Core event registration and firing.

The twisted event loop isn't appropriate here because of how callables are
handled, and the filtering that happens.
"""

import logging
from collections import defaultdict
from datetime import datetime

def IRCEvent(type_, sender, message, timestamp=None, **kwargs):
    """An IRC event.

    All IRC events share type, sender, message, and timestamp in common, so
    this enforces that they exist.
    """

    if timestamp is None:
        timestamp = datetime.now()

    return defaultdict(type=type_,  sender=sender, message=message,
                 timestamp=timestamp, **kwargs)

def add_callback(event, callback, registry):
    """Adds the callback to a registry.

    If the callback is already registered, it isn't added again, and a warning
    is printed.
    """

    callbacks = registry.get(event, [])
    if callback not in callbacks:
        callbacks.append(callback)
    else:
        logging.warn("A callback was added twice for the same event!")

    registry[event] = callbacks

class EventRouter(object):
    """An event router."""

    dict_registry = {}
    callable_registry = {}

    def register(self, callback, event_filter):
        """Register callback to be fired on event.

        callback must take one positional argument, which will be the event.

        If filter is callable, it also takes on positional argument: the event.
        If the callback should be fired for the given event, it must return
        True, else, False.

        If filter is not callable, it should be a dict-like object where the
        keys are strings, and the values are either strings which will be
        checked for equality with the value of the same key, or a callable
        which will be called with the value. When an event is fired, the
        following pseudocode is roughly followed:

            for key, value in filter.iteritems():
                if event[key] == value:
                    callback(event)
                elif filter[key] is callable and filter[key](event[key]):
                    callback(event)
        """

        if hasattr(event_filter, '__call__'):
            add_callback(event_filter, callback, self.callable_registry)
        else:
            event_filter = frozenset(event_filter.iteritems())
            add_callback(event_filter, callback, self.dict_registry)

    def fire(self, event, copy=lambda o: o):
        """Fire an event.

        event must be a dict-like object. If copy is passed in, it will be
        called on event before passing it to each callback or filter,
        preventing callbacks/filters from affecting each other, which is ugly
        action at a distance.
        """

        for event_filter, callbacks in self.dict_registry.iteritems():
            call = True
            for key, value in event_filter:
                if hasattr(value, '__call__'):
                    if not value(copy(event[key])):
                        call = False
                        break
                else:
                    if value != event[key]:
                        call = False
                        break
            if call:
                for c in callbacks:
                    c(copy(event))

        for event_filter, callbacks in self.callable_registry.iteritems():
            if event_filter(copy(event)):
                for callback in callbacks:
                    callback(copy(event))
