# Released under GPLv3+ License
# Danial Behzadi <dani.behzi@ubuntu.com>, 2024.
"""
Things to do with control socket
"""

from os.path import join

from gi.repository import GLib
from stem import Signal
from stem.connection import connect
from stem.control import Controller


def _get_controller() -> Controller:
    """
    Return the control socket
    """
    socket = join(GLib.get_user_config_dir(), "tractor", "control.sock")
    controller = connect(control_socket=socket)
    return controller


def send_signal(signal: str) -> None:
    """
    Send a signal to the tor process
    """
    controller = _get_controller()
    if controller:
        match signal:
            case "term":
                controller.signal(Signal.TERM)
            case "newnym":
                controller.signal(Signal.NEWNYM)
            case _:
                raise ValueError(f"Wrong signal '{signal}'.")


def get_listener(listener_type: str) -> int:
    """
    Get configuration from control socket
    """
    controller = _get_controller()
    if controller:
        value = controller.get_listeners(listener_type)
        return value[0]
    raise ValueError("No listener.")


def get_pid() -> int:
    """
    Get pid of the tor process
    """
    controller = _get_controller()
    if controller:
        return controller.get_pid()
    return 0


def get_bridge() -> str:
    """
    Get the current using bridges
    """
    controller = _get_controller()
    if controller:
        if controller.get_conf("UseBridges"):
            return controller.get_conf("Bridge")
    return ""
