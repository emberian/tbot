"""Common IRC and event dispatching for both master and individual mode.

The connection to IRC and event dispatching is identical between a master and an
individual tbot. This core functionality is provided here."""

from router import EventRouter
