from typing import Any

from textual.app import ComposeResult
from textual.containers import Center, Vertical
from textual.message import Message
from textual.widgets import Static

from src.tui.widgets.controls import TimerControls
from src.tui.widgets.display import TimerDisplay


class PomodoroTimer(Static):
	"""A self-contained Pomodoro timer widget."""

	class SessionCompleted(Message):
		"""Posted when a focus session successfully finishes."""

	def __init__(self, *args: Any, **kwargs: Any) -> None:
		super().__init__(*args, **kwargs)
		self.timer_display = TimerDisplay()
		self.timer_controls = TimerControls()

	def compose(self) -> ComposeResult:
		"""Child widgets for the component."""
		with Vertical():
			with Center():
				yield self.timer_display
			yield self.timer_controls

	def on_timer_controls_started(self, message: TimerControls.Started) -> None:
		"""Handle start button click from the internal controls."""
		self.timer_display.start()

	def on_timer_controls_paused(self, message: TimerControls.Paused) -> None:
		"""Handle pause button click from the internal controls."""
		self.timer_display.pause()

	def on_timer_controls_reset(self, message: TimerControls.Reset) -> None:
		"""Handle reset button click from the internal controls."""
		self.timer_display.reset()

	def on_timer_display_completed(self, message: TimerDisplay.Completed) -> None:
		self.app.notify("Session completed.", title="Success", severity="information")
		self.post_message(self.SessionCompleted())
