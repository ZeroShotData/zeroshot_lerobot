from typing import Protocol


class MotorsBus(Protocol):
    def motor_names(self):
        ...

    def set_calibration(self):
        ...

    def apply_calibration(self):
        ...

    def revert_calibration(self):
        ...

    def read(self):
        ...

    def write(self):
        ...
