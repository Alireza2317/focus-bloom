from textual.app import ComposeResult
from textual.widgets import Static

from src.tui.widgets.controls import TimerControls
from src.tui.widgets.display import TimerDisplay


class PomodoroTimer(Static):
	"""A self-contained Pomodoro timer widget."""

	def compose(self) -> ComposeResult:
		"""Child widgets for the component."""
		yield TimerDisplay()
		yield TimerControls()

	def on_timer_controls_started(self, message: TimerControls.Started) -> None:
		"""Handle start button click from the internal controls."""
		self.query_one(TimerDisplay).start()

	def on_timer_controls_stopped(self, message: TimerControls.Stopped) -> None:
		"""Handle stop button click from the internal controls."""
		self.query_one(TimerDisplay).stop()

	def on_timer_controls_reset(self, message: TimerControls.Reset) -> None:
		"""Handle reset button click from the internal controls."""
		self.query_one(TimerDisplay).reset()
