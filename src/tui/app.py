from typing import Any

from textual.app import App, ComposeResult
from textual.binding import BindingType
from textual.containers import Horizontal, Vertical
from textual.widgets import Button, Footer, Header

from src.core.character import PlantCharacter
from src.core.config import config
from src.tui.widgets.animation import CharacterAnimation
from src.tui.widgets.pomodoro import PomodoroTimer
from src.tui.widgets.stats import CharacterStatsWidget


class FocusApp(App):
	"""A Textual app to manage focus."""

	CSS_PATH = "styles.tcss"

	# Global keybindings that trigger the pressbtn action with button IDs
	BINDINGS: list[BindingType] = [
		("s", "pressbtn('#timer_start')", "Start"),
		("p", "pressbtn('#timer_pause')", "Pause"),
		("r", "pressbtn('#timer_reset')", "Reset"),
		("q", "quit", "Quit"),
	]

	def __init__(self, *args: Any, **kwargs: Any):
		super().__init__(*args, **kwargs)
		self.character = PlantCharacter(name="Plant 1")

	def compose(self) -> ComposeResult:
		"""Child widgets for the app."""
		yield Header()
		with Horizontal(id="main_container"):
			with Vertical():
				yield CharacterStatsWidget(character=self.character)
				yield CharacterAnimation(character=self.character)
			yield PomodoroTimer()
		yield Footer()

	def action_pressbtn(self, btn_id: str) -> None:
		"""Trigger a button press by its ID."""
		self.query_one(btn_id, Button).press()

	def on_pomodoro_timer_session_completed(
		self, message: PomodoroTimer.SessionCompleted
	) -> None:
		"""Handle successful completion of a focus session."""
		# Give configured XP per session
		leveled_up = self.character.add_xp(config.XP_PER_SESSION)

		# Sync stats and animation with new character state
		self.query_one(CharacterStatsWidget).update_stats()
		self.query_one(CharacterAnimation).update_art()

		if leveled_up:
			self.notify(
				f"Level Up! You reached level {self.character.level}!",
				title="Congratulations",
				severity="information",
			)
