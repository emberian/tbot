Design
======

Architecture
------------

A ``tbot`` connects to either a ``tbot master`` (thus becoming a ``slave``),
or an IRC server (becomming a ``tbot``).

A ``tbot`` is intended, and works best, when you have multiple small, separate
``tbot slaves`` behind a ``tbot master``. However, a ``tbot`` can be
connected directly to an IRC server, for ease of deploying. This is, however,
unreccomended, and makes for slower iterative development, as the tbot master
will be unable to reload the module dynamically.

A ``tbot master`` acts as a proxy between ``slaves`` and the IRC server. A
``slave`` registers the events it is interested in with the ``master``. The
``master`` then forwards the events to the interested ``slaves`` when they
occur, reducing overhead for the slaves.

Persistence
-----------

Persistence, as seen by a tbot in ``tbot.bot.state``, is provided (for now) by
the shelve module. ``tbot.bot.state.commit()`` can be called to manually save
changed state, or ``tbot.bot.state.autocommit_changelimit`` can be set to a
numeric indicating how many state changes to wait for before committing.
``tbot.bot.state.autocommit_timeout`` can be set to a numeric indicating how
many minutes will pass before state is commited. Both of these default to
``None``. They only come into affect if ``tbot.bot.state.autocommit`` is True.
This is only suggest when state changes are relatively infrequent. Heavy
modification of state should manually call ``tbot.bot.state.commit()``. All
state changes before a commit should be considered temporary and may not
necessarily be persisted.


Configuration uses the ConfigParser module. If possible, configuration will be
updated while running (as seen by in ``tbot.bot.config``) if the config file is
changed. Changes are detected using pyinotify if it is available.
