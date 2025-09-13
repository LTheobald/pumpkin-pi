# Pumpkin Pi

Simple Python scaffold for Raspberry Pi projects with a CLI and a safe simulation fallback when GPIO is not available.

## Quick Start

- Requires Python 3.9+
- Install dev deps and run tests:

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e . pytest
pytest -q
```

## Run the CLI

Simulation mode (default if GPIO not available):

```bash
python -m pumpkin_pi --simulate --count 3 --interval 0.5 --pin 17
```

On a Raspberry Pi with a real LED on BCM pin 17 (requires `gpiozero`):

```bash
pip install .[rpi]
python -m pumpkin_pi --count 3 --interval 0.5 --pin 17
```

## Project Structure

- `src/pumpkin_pi/` – Python package
  - `__main__.py` – CLI entry point
  - `blinker.py` – Hardware abstraction with simulation fallback
- `tests/` – Minimal pytest tests
- `.github/workflows/ci.yml` – CI workflow targeting a self-hosted runner

## GitHub Actions (Self-Hosted Runner)

The included workflow runs on `runs-on: self-hosted`. Make sure your runner has:

- Access to the repository
- Python installed (workflow uses `actions/setup-python` to install 3.11)

If your runner uses additional labels (e.g., `self-hosted`, `linux`, `arm64`), you can adjust the job like:

```yaml
runs-on: [self-hosted, linux, arm64]
```

## Notes

- The code auto-detects availability of `gpiozero`. If not available or `--simulate` is provided, it prints simulated blink events instead of controlling hardware.
- Default pin is BCM 17; adjust with `--pin`.

