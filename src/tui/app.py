from typing import Any

from textual.app import App, ComposeResult
from textual.widgets import Footer, Header

from src.core.character import PlantCharacter
from src.core.config import config
from src.tui.widgets.animation import PlantAnimation
from src.tui.widgets.pomodoro import PomodoroTimer
from src.tui.widgets.stats import CharacterStatsWidget


class FocusApp(App):
	"""A Textual app to manage focus."""

	def __init__(self, *args: Any, **kwargs: Any):
		super().__init__(*args, **kwargs)
		self.character = PlantCharacter(name="Plant 1")

	def compose(self) -> ComposeResult:
		"""Child widgets for the app."""
		yield Header()
		yield CharacterStatsWidget(character=self.character)
		yield PlantAnimation(character=self.character)
		yield PomodoroTimer()
		yield Footer()


	def on_pomodoro_timer_session_completed(
		self, message: PomodoroTimer.SessionCompleted
	) -> None:
		"""Handle successful completion of a focus session."""
		# Give configured XP per session
		leveled_up = self.character.add_xp(config.XP_PER_SESSION)

		# Update the stats UI
		self.query_one(CharacterStatsWidget).update_stats()

		# Update the animation UI
		self.query_one(PlantAnimation).update_art()

		if leveled_up:
			self.notify(
				f"Level Up! You reached level {self.character.level}!",
				title="Congratulations",
				severity="information",
			)
