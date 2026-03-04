from textual.containers import Horizontal
from textual.message import Message
from textual.widgets import Button, Static


class TimerControls(Static):
	"""A widget to hold the Start, Stop, and Reset buttons."""

	class Started(Message):
		"""Posted when the Start button is clicked."""

	class Stopped(Message):
		"""Posted when the Stop button is clicked."""

	class Reset(Message):
		"""Posted when the Reset button is clicked."""

	def on_button_pressed(self, event: Button.Pressed) -> None:
		"""Event handler called when a button is pressed."""
		if event.button.id == "timer_start":
			self.post_message(self.Started())
		elif event.button.id == "timer_stop":
			self.post_message(self.Stopped())
		elif event.button.id == "timer_reset":
			self.post_message(self.Reset())

	def compose(self):
		"""Create child widgets for the component."""
		with Horizontal():
			yield Button("Start", id="timer_start", variant="success")
			yield Button("Stop", id="timer_stop", variant="error")
			yield Button("Reset", id="timer_reset")
