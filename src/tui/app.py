from typing import Any

from textual.app import App, ComposeResult
from textual.widgets import Footer, Header

from src.core.character import Character
from src.tui.widgets.pomodoro import PomodoroTimer
from src.tui.widgets.stats import CharacterStatsWidget


class FocusApp(App):
	"""A Textual app to manage focus."""

	def __init__(self, *args: Any, **kwargs: Any):
		super().__init__(*args, **kwargs)
		self.character = Character(name="Plant 1")

	def compose(self) -> ComposeResult:
		"""Child widgets for the app."""
		yield Header()
		yield CharacterStatsWidget(character=self.character)
		yield PomodoroTimer()
		yield Footer()

	def on_pomodoro_timer_session_completed(
		self, message: PomodoroTimer.SessionCompleted
	) -> None:
		"""Handle successful completion of a focus session."""
		# Give 50 XP per session
		leveled_up = self.character.add_xp(50)

		# Update the stats UI
		self.query_one(CharacterStatsWidget).update_stats()

		if leveled_up:
			self.notify(
				f"Level Up! You reached level {self.character.level}!",
				title="Congratulations",
				severity="information",
			)


if __name__ == "__main__":
	app = FocusApp()
	app.run()
