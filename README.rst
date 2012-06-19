tbot
====

*A library to make writing IRC bots easier and more fun*

- License: Modified BSD

Rationale
---------

Writing IRC bots is easy enough that beginners often pull it off to some
success. But writing extensible, maintainable, IRC bots that are abstracted
from the details of the protocol is difficult. ``twisted.words.protocols.irc``
makes that a wee bit easier, but you still need to deal with some things you
probably don't care about, like 'factories' or 'protocols' and such things.
There are also some harder problems like persistence of state, configuration,
and module reloading that don't have obvious solutions.

``tbot`` tries to make that simpler, letting you focus on what you care about:
doing cool things in IRC.
