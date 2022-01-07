from enum import Enum


class Signal(str, Enum):
    red = "red"
    green = "green"
    orange = "orange"


def test_signal():
    brain_detected_colour = "red"
    brain_detected_colour == Signal.red  # direct comparison
