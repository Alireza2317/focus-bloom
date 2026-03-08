from textual.app import ComposeResult
from textual.containers import Vertical
from textual.widgets import Label, ProgressBar, Static

from src.core.meter import FocusMeter


class FocusMeterWidget(Static):
	"""A widget to display the Focus Meter's charge and streak."""

	def __init__(self, focus_meter: FocusMeter, **kwargs):
		super().__init__(**kwargs)
		self.focus_meter = focus_meter

	def compose(self) -> ComposeResult:
		"""Child widgets for the component."""
		with Vertical():
			yield Label("Focus Meter", id="fmeter_label")
			yield ProgressBar(
				total=100, show_eta=False, id="fmeter_progress"
			)

	def update_progress(self) -> None:
		"""Update the progress bar and streak display."""
		progress_bar: ProgressBar = self.query_one("#fmeter_progress", ProgressBar)
		progress_bar.progress = self.focus_meter.charge

		label = self.query_one("#fmeter_label", Label)
		label.update(f"Focus Meter (Streak: {self.focus_meter.streak}x)")
