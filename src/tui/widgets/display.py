from textual.message import Message
from textual.reactive import reactive
from textual.timer import Timer
from textual.widgets import Static

from src.core.config import Config


class TimerDisplay(Static):
	"""A widget to display the time."""

	time: reactive[int] = reactive(Config.TIMER_MINUTES * 60)  # in seconds

	class Completed(Message):
		"""Posted when timer reaches 0."""

	def on_mount(self) -> None:
		"""Event handler called when widget is added to the app."""
		self.interval_timer: Timer = self.set_interval(1, self.update_time, pause=True)

	def update_time(self) -> None:
		"""Called every second to update the time."""
		if self.time > 0:
			self.time -= Config.TIMER_DEDUCTION
		else:
			self.stop()
			self.post_message(self.Completed())
			if Config.AUTO_RESET:
				self.reset()
				self.start()

	def watch_time(self, time: int) -> None:
		"""Called when the time attribute changes."""
		minutes, seconds = divmod(time, 60)
		self.update(f"{minutes:02d}:{seconds:02d}")

	def start(self) -> None:
		if self.time <= 0:
			self.reset()

		self.interval_timer.resume()

	def stop(self) -> None:
		self.interval_timer.pause()

	def reset(self) -> None:
		self.time = Config.TIMER_MINUTES * 60
