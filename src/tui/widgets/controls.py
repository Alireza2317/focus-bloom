from textual.containers import Horizontal
from textual.widgets import Button, Static


class TimerControls(Static):
	"""A widget to hold the Start, Stop, and Reset buttons."""

	def compose(self):
		"""Create child widgets for the component."""
		with Horizontal():
			yield Button("Start", id="timer_start", variant="success")
			yield Button("Stop", id="timer_stop", variant="error")
			yield Button("Reset", id="timer_reset")
