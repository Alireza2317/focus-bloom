from textual.containers import Horizontal
from textual.message import Message
from textual.widgets import Button, Static


class TimerControls(Static):
	"""A widget to hold the Start, Pause, and Reset buttons."""

	class Started(Message):
		"""Posted when the Start button is clicked."""

	class Paused(Message):
		"""Posted when the Pause button is clicked."""

	class Reset(Message):
		"""Posted when the Reset button is clicked."""

	def on_button_pressed(self, event: Button.Pressed) -> None:
		"""Event handler called when a button is pressed."""
		if event.button.id == "timer_start":
			self.post_message(self.Started())
		elif event.button.id == "timer_pause":
			self.post_message(self.Paused())
		elif event.button.id == "timer_reset":
			self.post_message(self.Reset())

	def compose(self):
		"""Create child widgets for the component."""
		with Horizontal():
			yield Button("Start", id="timer_start", variant="success")
			yield Button("Pause", id="timer_pause", variant="error")
			yield Button("Reset", id="timer_reset")
