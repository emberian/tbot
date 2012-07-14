from tbot._routing.core import EventRouter
from mock import MagicMock

def test_event_fires():
    e = EventRouter()

    callback = MagicMock()

    e.register('foo', callback)
    e.fire('foo')

    assert callback.called

def test_event_fires_with_data():
    e = EventRouter()

    callback = MagicMock()
    data = dict(foo='bar')

    e.register('foo',  callback)
    e.fire('foo', data)
    
    assert callback.called
    assert callback.call_args[0][1] is data

def test_event_data_copied():
    e = EventRouter()

    callback = MagicMock()
    data = dict(foo='bar')

    e.register('foo', callback)
    e.fire('foo', data,  copy=dict)
    
    assert callback.called
    assert callback.call_args[0][1] is not data

def test_event_callable_filter():
    e = EventRouter()

    callback = MagicMock()
    event = MagicMock(return_value=True)

    e.register(event, callback)
    e.fire('foo')
    assert callback.called

    event.return_value = False
    e.fire('foo')
    assert callback.call_count == 1

def test_event_two_callbacks():
    e = EventRouter()

    callback1 = MagicMock()
    callback2 = MagicMock()

    e.register('foo', callback1)
    e.register('foo', callback2)

    e.fire('foo')

    assert callback1.called and callback2.called

def test_callback_weakref():
    e = EventRouter()

    e.register('foo', lambda a, b: None, True)

    e.fire('foo') # properly handled weakref going away
