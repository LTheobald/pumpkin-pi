import re

from pumpkin_pi import Blinker


def test_simulated_blink_outputs(capsys):
    b = Blinker(pin=22, simulate=True)
    assert b.is_simulated
    b.blink(count=2, interval=0)
    out = capsys.readouterr().out
    # Expect two on and two off messages for pin 22
    assert len(re.findall(r"Simulated LED on \(pin 22\)", out)) == 2
    assert len(re.findall(r"Simulated LED off \(pin 22\)", out)) == 2


def test_invalid_args():
    b = Blinker(simulate=True)
    try:
        b.blink(count=-1)
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError for negative count")

