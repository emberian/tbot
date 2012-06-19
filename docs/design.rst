Architecture
============

Basically, a ``tbot`` can connect to any given IRC server. A tbot instance
registers event handlers for certain things it wants to listen to. The
tbot will connect to the configured IRC servers.

A ``tbot`` is intended, and works best, when you have multiple small,
separate ``tbot``'s behind a bouncer like ZNC. This way, reloading single
modules becomes a *lot* easier.

Persistence, as seen by a tbot in ``self.state``, is provided (for now) by
the shelve module. Configuration uses the ConfigParser module. If possible,
tbot will update configuration while running (as seen by in ``self.config``)
if the config file is changed. Changes are detected using pyinotify if it is
available.
