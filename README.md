# Pumpkin Pi

Simple Python scaffold for Raspberry Pi projects with a CLI and a safe simulation fallback when GPIO is not available.

## Quick Start

### Local (without Docker)

- Requires Python 3.9+
- Install dev deps and run tests:

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e .[dev]
pre-commit run --all-files
pytest -q
```

### Dockerized Development

Build the image and drop into a shell with the project mounted:

```bash
docker compose build
docker compose run --rm dev
```

Inside the container the dependencies are installed; run the same checks:

```bash
pre-commit run --all-files
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

## GitHub Actions

The workflow at `.github/workflows/ci.yml` runs on every push and pull request and has two jobs:

1. **lint-test** – runs `pre-commit` and `pytest` on an Ubuntu runner with pip caching.
2. **hardware-test** – executes the tests on the Raspberry Pi self-hosted runner, also using pip caching.

Ensure your Pi runner is online and labeled `raspberrypi`.

## Notes

- The code auto-detects availability of `gpiozero`. If not available or `--simulate` is provided, it prints simulated blink events instead of controlling hardware.
- Default pin is BCM 17; adjust with `--pin`.
