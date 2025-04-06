# Released under GPLv3+ License
# Danial Behzadi <dani.behzi@ubuntu.com>, 2024.
"""
Unit tests for db
"""

import unittest
from unittest.mock import patch, MagicMock
from tractor import control


class SendSignal(unittest.TestCase):
    """
    test case for send_signal
    """

    @patch("tractor.control._get_controller")
    def test_send_signal_term(self, mock_get_controller, *_):
        """
        send defined signals
        """
        # Arrange
        mock_controller = MagicMock()
        mock_get_controller.return_value = mock_controller
        # Act & Assert
        control.send_signal("term")
        mock_controller.signal.assert_called_once_with("TERM")

    @patch("tractor.control._get_controller")
    def test_send_signal_newnym(self, mock_get_controller, *_):
        """
        send defined signals
        """
        # Arrange
        mock_controller = MagicMock()
        mock_get_controller.return_value = mock_controller
        # Act & Assert
        control.send_signal("newnym")
        mock_controller.signal.assert_called_once_with("NEWNYM")

    @patch("tractor.control._get_controller", return_value=True)
    def test_send_signal_fail(self, *_):
        """
        undefined signal
        """
        with self.assertRaises(ValueError):
            control.send_signal("kill")


class GetListener(unittest.TestCase):
    """
    test case for get_listener
    """

    @patch("tractor.control._get_controller")
    def test_get_listener_success(self, mock_get_controller, *_):
        """
        get listener of any type
        """
        # Arrange
        mock_controller = MagicMock()
        mock_controller.get_listeners.return_value = [9052]
        mock_get_controller.return_value = mock_controller
        # Act
        result = control.get_listener("socks")
        # Assert
        mock_get_controller.assert_called_once()
        mock_controller.get_listeners.assert_called_once_with("socks")
        self.assertEqual(result, 9052)

    @patch("tractor.control._get_controller", return_value = False)
    def test_get_listener_fail(self, *_):
        """
        get listener of any type
        """
        # Act & Assert
        with self.assertRaises(ValueError):
            control.get_listener("ftp")


class GetPid(unittest.TestCase):
    """
    test case for get_pid
    """

    @patch("tractor.control._get_controller")
    def test_get_pid_success(self, mock_get_controller, *_):
        """
        Test get_pid returns a valid PID when controller is available.
        """
        # Arrange
        mock_controller = MagicMock()
        mock_controller.get_pid.return_value = 5678
        mock_get_controller.return_value = mock_controller
        # Act
        result = control.get_pid()
        # Assert
        self.assertEqual(result, 5678)

    @patch("tractor.control._get_controller", return_value = False)
    def test_get_pid_fail(self, *_):
        """
        Test get_pid returns 0 when no controller is returned.
        """
        # Act
        result = control.get_pid()
        # Assert
        self.assertEqual(result, 0)
