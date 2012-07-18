from weakref import ReferenceError

from tbot._common import SimpleRouter
from mock import MagicMock

def test_event_fires():
    e = SimpleRouter()

    callback = MagicMock()

    e.register('foo', callback)
    e.fire('foo')

    assert callback.called, "Callback wasn't called"


def test_event_fires_with_data():
    e = SimpleRouter()

    callback = MagicMock()
    data = dict(foo='bar')

    e.register('foo',  callback)
    e.fire('foo', data)
    
    assert callback.called, "Callback wasn't called"
    assert callback.call_args[0][1] is data, "Data was somehow modified"


def test_event_data_copied():
    e = SimpleRouter()

    callback = MagicMock()
    data = dict(foo='bar')

    e.register('foo', callback)
    e.fire('foo', data,  copy=dict)
    
    assert callback.called, "Callback wasn't called"
    assert callback.call_args[0][1] is not data, "Data wasn't copied"


def test_event_callable_filter():
    e = SimpleRouter()

    callback = MagicMock()
    event = MagicMock(return_value=True)

    e.register(event, callback)
    e.fire('foo')
    assert callback.called, "Callback wasn't called"

    event.return_value = False
    e.fire('foo')
    assert callback.call_count == 1, "Callback was called even though filter returned False"


def test_callable_filter_two_callbacks():
    e = SimpleRouter()

    callback1 = MagicMock()
    callback2 = MagicMock()

    filter_ = lambda a, b: True

    e.register(filter_, callback1)
    e.register(filter_, callback2)

    e.fire('foo')

    assert callback1.called, "First callback not called"
    assert callback2.called, "Second callback not called"


def test_event_two_callbacks():
    e = SimpleRouter()

    callback1 = MagicMock()
    callback2 = MagicMock()

    e.register('foo', callback1)
    e.register('foo', callback2)

    e.fire('foo')

    assert callback1.called, "First callback not called"
    assert callback2.called, "Second callback not called"


def test_callback_weakref():
    import gc

    e = SimpleRouter()

    e.register('foo', lambda a, b: None, weak=True)

    gc.collect() # Ensure that that lambda is collected.
    
    try:
        e.fire('foo') # if no exception is raised, we properly handled weakref going away
    except ReferenceError:
        pytest.fail("SimpleRouter deos not properly handle weakrefs being collected")
