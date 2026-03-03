from textual.reactive import reactive
from textual.widgets import Static


class Timer(Static):
	"""A widget to display the time."""

	time: reactive[int] = reactive(25 * 60)  # 25 minutes in seconds

	def on_mount(self) -> None:
		"""Event handler called when widget is added to the app."""
		self.set_interval(1, self.update_time)

	def update_time(self) -> None:
		"""Called every second to update the time."""
		self.time -= 1

	def watch_time(self, time: int) -> None:
		"""Called when the time attribute changes."""
		minutes, seconds = divmod(int(time), 60)
		self.update(f"{minutes:02d}:{seconds:02d}")
