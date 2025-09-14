from __future__ import annotations

import argparse
import sys

from .blinker import Blinker


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="pumpkin-pi",
        description="Pumpkin Pi: simple Raspberry Pi scaffold with simulated GPIO",
    )
    p.add_argument(
        "--pin", type=int, default=17, help="GPIO pin number (BCM). Default: 17"
    )
    p.add_argument(
        "--count", type=int, default=3, help="Number of blink cycles. Default: 3"
    )
    p.add_argument(
        "--interval",
        type=float,
        default=0.5,
        help="Seconds between on/off. Default: 0.5",
    )
    p.add_argument(
        "--simulate",
        action="store_true",
        help="Force simulation even if GPIO libraries are present",
    )
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    blinker = Blinker(pin=args.pin, simulate=args.simulate)
    mode = "simulation" if blinker.is_simulated else "hardware"
    print(
        f"[pumpkin-pi] Starting blink on pin {args.pin} in {mode} mode: "
        f"count={args.count}, interval={args.interval}s"
    )

    try:
        blinker.blink(count=args.count, interval=args.interval)
    except KeyboardInterrupt:
        print("[pumpkin-pi] Interrupted.")
        return 130
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
