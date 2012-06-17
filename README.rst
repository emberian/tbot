tbotframe (tbf)
===============

*A framework for writing extensible IRC bots in Python*

Rationale
---------

IRC bots are easy to write. So easy, that many newbies often roll their own
using ``irclib`` or, if they're feeling brave, ``socket``. These turn into
unmaintainable messy piles of code. Things like supybot or phenny have helped
in that realm. But (at least afaik), neither of those are maintained. Twisted
has IRC functionality, but I've found no bot frameworks for it.

Features
--------

+ Extensible module system
+ Centralized configuration
+ Module persistence and reloading

Module System
-------------

*Unimplemented*

Modules are a bit different in tbotframe than in Python. tbotframe is a simple
router that sits between a bunch of local processes and one (or more) IRC
servers. It acts as a server for the module clients. 

This may sound complex, but it's simple. Here's what a module looks like::

    import random
    import tbot
    
    @tbot.on_prefixed('ping')
    def ping(sender, **kwargs):
        return "{0}: pong!".format(sender)
    
That's not so bad! The tbotframe will have a global prefix (defaults to '!'),
so '!ping' would trigger that listener. There are more ways to create a
module, but that's the gist of it.

Centralized Configuration
-------------------------

*Unimplemented*

Configuration of modules can be a pain, so ``tbf`` centralizes it. If a module
ships with any ``.conf`` files, they will be added to 
``modules/module_name/foo.conf``, where you can then edit them. A module using
centralized configuration will automatically reload edited files.

Code (greeter.py)::

    import tbot

    @tbot.on_prefixed('hello')
    def greet(sender, **kwargs):
        return "{0}: hello, my name is {1}".format(sender, tbot.config['name'])

Configuration (greeter.conf)::

    name = "TBotPrime"

Module Persistence and Reloading
--------------------------------

*Unimplemented*

Modules should be updatable, replacable, and generally *modular*. In order to
accomplish this, modules should store all state they care about in
``tbot.state``. It will be persisted automatically, and will survive restarts.
It is a simple key-value store. For now, only strings, arrays, and dicts with
strings for keys and strings, dicts, or arrays as values are valid keys. The
only valid keys are strings.
