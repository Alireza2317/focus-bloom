from textual.reactive import reactive
from textual.timer import Timer
from textual.widgets import Static

TIMER_MINUTES: int = 25


class TimerDisplay(Static):
	"""A widget to display the time."""

	time: reactive[int] = reactive(TIMER_MINUTES * 60)  # in seconds

	def on_mount(self) -> None:
		"""Event handler called when widget is added to the app."""
		self.interval_timer: Timer = self.set_interval(1, self.update_time, pause=True)

	def update_time(self) -> None:
		"""Called every second to update the time."""
		self.time -= 1

	def watch_time(self, time: int) -> None:
		"""Called when the time attribute changes."""
		minutes, seconds = divmod(time, 60)
		self.update(f"{minutes:02d}:{seconds:02d}")

	def start(self) -> None:
		self.interval_timer.resume()

	def stop(self) -> None:
		self.interval_timer.pause()

	def reset(self) -> None:
		self.time = TIMER_MINUTES * 60
