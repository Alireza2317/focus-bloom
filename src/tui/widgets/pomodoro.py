from typing import Any

from textual.app import ComposeResult
from textual.widgets import Static

from src.tui.widgets.controls import TimerControls
from src.tui.widgets.display import TimerDisplay


class PomodoroTimer(Static):
	"""A self-contained Pomodoro timer widget."""

	def __init__(self, *args: Any, **kwargs: Any) -> None:
		super().__init__(*args, **kwargs)
		self.timer_display = TimerDisplay()
		self.timer_controls = TimerControls()

	def compose(self) -> ComposeResult:
		"""Child widgets for the component."""
		yield self.timer_display
		yield self.timer_controls

	def on_timer_controls_started(self, message: TimerControls.Started) -> None:
		"""Handle start button click from the internal controls."""
		self.timer_display.start()

	def on_timer_controls_stopped(self, message: TimerControls.Stopped) -> None:
		"""Handle stop button click from the internal controls."""
		self.timer_display.stop()

	def on_timer_controls_reset(self, message: TimerControls.Reset) -> None:
		"""Handle reset button click from the internal controls."""
		self.timer_display.reset()
