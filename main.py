import argparse

from src.core.config import config
from src.tui.app import FocusApp


def setup_cli_args():
	"""Parse command-line arguments and set up configuration."""
	parser = argparse.ArgumentParser(
		description="Focus Bloom - A Pomodoro-based focus app."
	)
	parser.add_argument(
		"--debug",
		action="store_true",
		help="Enable debug mode with rapid testing settings.",
	)
	args = parser.parse_args()

	if args.debug:
		config.set_debug_mode()


if __name__ == "__main__":
	setup_cli_args()

	app = FocusApp()
	app.run()
