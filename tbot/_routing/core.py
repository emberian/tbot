"""Core event registration and firing.

The twisted event loop isn't appropriate here because of how callables are
handled, and the filtering that happens.
"""

import weakref

class EventRouter(object):
    """An event router."""
    events = {}
    event_filters = {}

    def register(self, event, callback, weak=False):
        """Register callback to be fired on event.

        callback must take one positional argument, which will be the event
        data.

        If event is callable, it must take two positional arguments: event, and
        data. If the callback should be fired for given event+data, it must
        return True, else, False. Otherwise, it should be a string.

        If weak is True, a weak reference to the callback is kept, and the
        registration will be removed when the callback is collected.
        """
        if weak:
            callback = weakref.proxy(callback)
        
        try: 
            if event.__call__:
                self.event_filters[event] = callback
                return
        except AttributeError:
            pass

        callbacks = self.events.get(event, [])
        if callback not in callbacks:
            callbacks.append(callback)

        self.events[event] = callbacks

    def fire(self, event, data=None, copy=lambda o: o):
        """Fire an event.

        event must be a string. data can be anything. If copy is passed in, it
        will be called on data before passing it to each callback, preventing
        callbacks from modifying each other's data, which is ugly action at a
        distance.
        """
        toss = [] # callbacks to drop because the reference went away

        callbacks = self.events.get(event, [])
        for callback in callbacks:
            try:
                callback(event, copy(data))
            except weakref.ReferenceError:
                toss.append(callback)
                continue

        for callback in toss:
            callbacks.remove(callback)

        for event_filter, callback in self.event_filters.iteritems():
            if event_filter(event, copy(data)):
                callback(copy(data))