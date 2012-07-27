from mock import MagicMock

from tbot._common import EventRouter, IRCEvent

# The following two 
def test_routing_matched_event():
    e = IRCEvent("foo", None, None)

    er = EventRouter()

    cb = MagicMock()

    er.register(cb, {'type': 'foo'})
    er.fire(e)

    assert cb.called, "Callback not fired"

def test_routing_unmatched_event():
    e = IRCEvent(None, None, None)

    er = EventRouter()
    cb = MagicMock()

    er.register(cb, {'type': "not empty"})
    er.fire(e)

    assert not cb.called, "Callback fired when event doesn't match filter"

def test_routing_true_callable():
    e = IRCEvent(None, None, None)

    er = EventRouter()

    event_filter = MagicMock(return_value=True)
    cb = MagicMock()

    er.register(cb, event_filter)
    er.fire(e)

    assert event_filter.called, "Event filter not called"
    assert cb.called, "Callback not fired"

def test_routing_false_callable():
    e = IRCEvent(None, None, None)

    er = EventRouter()

    event_filter = MagicMock(return_value=False)
    cb = MagicMock()
   
    er.register(cb, event_filter)
    er.fire(e)

    assert not cb.called, "Callback fired when event_filter is false"

def test_routing_true_event_callables():
    e = IRCEvent(None, None, None)

    er = EventRouter()
    cb = MagicMock()
    filter_ = MagicMock(return_value=True)

    er.register(cb, {'type': filter_})
    er.fire(e)

    assert cb.called, "Callback not fired"
    assert filter_.called, "Filter not called"

def test_routing_false_event_callables():
    e = IRCEvent(None, None, None)

    er = EventRouter()
    cb = MagicMock()
    filter_ = MagicMock(return_value=False)

    er.register(cb, {'type': filter_})
    er.fire(e)

    assert not cb.called, "Callback fired when filter doesn't match"
    assert filter_.called, "Filter not called"
