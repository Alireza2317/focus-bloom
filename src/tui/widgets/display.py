from textual.message import Message
from textual.reactive import reactive
from textual.timer import Timer
from textual.widgets import Digits

from src.core.config import config


class TimerDisplay(Digits):
	"""A widget to display the time using large digits."""

	time: reactive[int] = reactive(0)

	class Completed(Message):
		"""Posted when timer reaches 0."""

	def __init__(self, *args, **kwargs) -> None:
		"""Initialize the TimerDisplay."""
		super().__init__(*args, **kwargs)
		# Set the time here to read the config at instantiation time
		self.time = config.TIMER_MINUTES * 60  # seconds

	def on_mount(self) -> None:
		"""Event handler called when widget is added to the app."""
		self.interval_timer: Timer = self.set_interval(1, self.update_time, pause=True)

	def update_time(self) -> None:
		"""Called every second to update the time."""
		if self.time > 0:
			self.time -= config.TIMER_DEDUCTION
		else:
			self.pause()
			self.post_message(self.Completed())
			if config.AUTO_RESET:
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

	def pause(self) -> None:
		self.interval_timer.pause()

	def reset(self) -> None:
		self.time = config.TIMER_MINUTES * 60
