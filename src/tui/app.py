from textual.app import App, ComposeResult
from textual.widgets import Footer, Header

from src.tui.widgets.controls import TimerControls
from src.tui.widgets.timer import Timer


class FocusApp(App):
	"""A Textual app to manage focus."""

	def compose(self) -> ComposeResult:
		"""Child widgets for the app."""
		yield Header()
		yield Timer()
		yield TimerControls()
		yield Footer()


if __name__ == "__main__":
	app = FocusApp()
	app.run()
