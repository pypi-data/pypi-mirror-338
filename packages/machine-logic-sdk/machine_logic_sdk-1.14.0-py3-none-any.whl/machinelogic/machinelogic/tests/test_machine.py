# pylint: disable=missing-function-docstring
# pylint: disable=protected-access
import unittest
from unittest.mock import MagicMock, patch

from machinelogic.ivention.exception import MachineException
from machinelogic.ivention.imachine import MachineOperationalState, MachineSafetyState
from machinelogic.machinelogic.machine import Machine


class TestMachine(unittest.TestCase):
    @patch("machinelogic.machinelogic.machine.Machine")
    def test_given_input_when_get_input_then_gets_correct_input(
        self, mock_machine: MagicMock
    ) -> None:
        # Arrange
        machine = mock_machine.return_value
        machine_motion_mock = MagicMock()
        input_mock = MagicMock()
        config_mock = MagicMock()

        input_mock.configuration = config_mock
        input_mock.configuration.uuid = "uuid"

        machine.list_machine_motions.return_value = [machine_motion_mock]
        machine._get_input_by_uuid.return_value = input_mock

        # Act
        found_input = machine._get_input_by_uuid("uuid")

        # Assert
        self.assertEqual(found_input, input_mock)

    @patch("machinelogic.machinelogic.machine.Machine")
    def test_given_output_when_get_output_then_gets_correct_output(
        self, mock_machine: MagicMock
    ) -> None:
        # Arrange
        machine = mock_machine.return_value
        machine_motion_mock = MagicMock()
        output_mock = MagicMock()
        config_mock = MagicMock()

        output_mock.configuration = config_mock
        output_mock.configuration.uuid = "uuid"

        machine.list_machine_motions.return_value = [machine_motion_mock]
        machine._get_output_by_uuid.return_value = output_mock

        # Act
        found_output = machine._get_output_by_uuid("uuid")

        # Assert
        self.assertEqual(found_output, output_mock)

    @patch("machinelogic.machinelogic.machine.Machine")
    def test_given_actuator_when_get_actuator_then_gets_correct_actuator(
        self, mock_machine: MagicMock
    ) -> None:
        # Arrange
        machine = mock_machine.return_value
        machine_motion_mock = MagicMock()
        actuator_mock = MagicMock()
        config_mock = MagicMock()

        actuator_mock.configuration = config_mock
        actuator_mock.configuration.uuid = "uuid"

        machine.list_machine_motions.return_value = [machine_motion_mock]
        machine._get_actuator_by_uuid.return_value = actuator_mock

        # Act
        found_actuator = machine._get_actuator_by_uuid("uuid")

        # Assert
        self.assertEqual(found_actuator, actuator_mock)

    def test_machine_reset_calls_api_try_clear_drive_errors(self) -> None:
        # Arrange
        with patch("machinelogic.machinelogic.machine.Api", MagicMock()), patch(
            "machinelogic.machinelogic.machine.MqttClient", MagicMock()
        ), patch("machinelogic.machinelogic.machine.Scene", MagicMock()), patch(
            "machinelogic.machinelogic.machine.MachineState", MagicMock()
        ):
            machine = Machine()
            api_mock = MagicMock()
            api_mock.try_clear_drive_errors = MagicMock()
            machine._api = api_mock

            # Act
            machine.reset()

            # Assert
            api_mock.try_clear_drive_errors.assert_called_once()

    def test_on_machine_state_update_exists_early_if_message_is_none(self) -> None:
        # Arrange
        with patch("machinelogic.machinelogic.machine.Api", MagicMock()), patch(
            "machinelogic.machinelogic.machine.MqttClient", MagicMock()
        ), patch("machinelogic.machinelogic.machine.Scene", MagicMock()), patch(
            "machinelogic.machinelogic.machine.MachineState", MagicMock()
        ):
            machine = Machine()
            machine._on_state_change_callback = MagicMock()
            mock_topic = "execution-engine/estop"
            mock_message = None
            # Act
            machine._on_machine_state_update(mock_topic, mock_message)

            # Assert
            machine._on_state_change_callback.assert_not_called()

    def test_on_machine_state_update_exists_early_if_on_state_change_callback_is_not_defined(
        self,
    ) -> None:
        # Arrange
        with patch("machinelogic.machinelogic.machine.Api", MagicMock()), patch(
            "machinelogic.machinelogic.machine.MqttClient", MagicMock()
        ), patch("machinelogic.machinelogic.machine.Scene", MagicMock()), patch(
            "machinelogic.machinelogic.machine.MachineState", MagicMock()
        ):
            machine = Machine()
            machine._on_state_change_callback = None
            mock_topic = "execution-engine/estop"
            mock_message = '{"estop": "Released", "areSmartDrivesReady": "true"}'
            # Act
            machine._on_machine_state_update(mock_topic, mock_message)

            # Assert
            if machine._on_state_change_callback is not None:
                machine._on_state_change_callback.assert_not_called()

    def test_on_machine_state_update_calls_on_state_change_callback_if_defined(
        self,
    ) -> None:
        # Arrange
        with patch("machinelogic.machinelogic.machine.Api", MagicMock()), patch(
            "machinelogic.machinelogic.machine.MqttClient", MagicMock()
        ), patch("machinelogic.machinelogic.machine.Scene", MagicMock()), patch(
            "machinelogic.machinelogic.machine.MachineState", MagicMock()
        ):
            machine = Machine()
            machine._on_state_change_callback = MagicMock()
            mock_topic = "execution-engine/estop"
            mock_message = '{"estop": "Released", "areSmartDrivesReady": "true"}'
            # Act
            machine._on_machine_state_update(mock_topic, mock_message)

            # Assert
            machine._on_state_change_callback.assert_called_once()

    def test_on_machine_state_update_calls_callback_with_normal_states(self) -> None:
        # Arrange
        with patch("machinelogic.machinelogic.machine.Api", MagicMock()), patch(
            "machinelogic.machinelogic.machine.MqttClient", MagicMock()
        ), patch("machinelogic.machinelogic.machine.Scene", MagicMock()), patch(
            "machinelogic.machinelogic.machine.MachineState", MagicMock()
        ):
            machine = Machine()
            machine._on_state_change_callback = MagicMock()
            mock_topic = "execution-engine/estop"
            mock_message = '{"estop": "Released", "areSmartDrivesReady": true}'
            # Act
            machine._on_machine_state_update(mock_topic, mock_message)

            # Assert
            machine._on_state_change_callback.assert_called_once_with(
                MachineOperationalState.NORMAL, MachineSafetyState.NORMAL
            )

    def test_on_machine_state_update_calls_callback_with_emergency_stop_state(
        self,
    ) -> None:
        # Arrange
        with patch("machinelogic.machinelogic.machine.Api", MagicMock()), patch(
            "machinelogic.machinelogic.machine.MqttClient", MagicMock()
        ), patch("machinelogic.machinelogic.machine.Scene", MagicMock()), patch(
            "machinelogic.machinelogic.machine.MachineState", MagicMock()
        ):
            machine = Machine()
            machine._on_state_change_callback = MagicMock()
            mock_topic = "execution-engine/estop"
            mock_message = '{"estop": "Triggered", "areSmartDrivesReady": false}'
            # Act
            machine._on_machine_state_update(mock_topic, mock_message)

            # Assert
            machine._on_state_change_callback.assert_called_once_with(
                MachineOperationalState.NON_OPERATIONAL,
                MachineSafetyState.EMERGENCY_STOP,
            )

    def test_on_machine_state_update_raises_exception_for_unknown_safety_state(
        self,
    ) -> None:
        # Arrange
        with patch("machinelogic.machinelogic.machine.Api", MagicMock()), patch(
            "machinelogic.machinelogic.machine.MqttClient", MagicMock()
        ), patch("machinelogic.machinelogic.machine.Scene", MagicMock()), patch(
            "machinelogic.machinelogic.machine.MachineState", MagicMock()
        ):
            machine = Machine()
            machine._on_state_change_callback = MagicMock()
            mock_topic = "execution-engine/estop"
            mock_message = '{"estop": "Unknown", "areSmartDrivesReady": true}'
            # Act & Assert
            with self.assertRaises(MachineException):
                machine._on_machine_state_update(mock_topic, mock_message)

    def test_on_system_state_change_registers_callback(self) -> None:
        # Arrange
        with patch("machinelogic.machinelogic.machine.Api", MagicMock()), patch(
            "machinelogic.machinelogic.machine.MqttClient", MagicMock()
        ), patch("machinelogic.machinelogic.machine.Scene", MagicMock()), patch(
            "machinelogic.machinelogic.machine.MachineState", MagicMock()
        ):
            machine = Machine()
            machine._on_state_change_callback = None
            machine.on_system_state_change(lambda x, y: None)
            # Act & Assert
            self.assertIsNotNone(machine._on_state_change_callback)


if __name__ == "__main__":
    unittest.main()
