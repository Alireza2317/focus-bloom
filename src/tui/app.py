from typing import Any

from textual.app import App, ComposeResult
from textual.binding import BindingType
from textual.containers import Horizontal, Vertical
from textual.widgets import Button, Footer, Header

from src.core.character import PlantCharacter
from src.core.config import config
from src.core.meter import FocusMeter
from src.tui.widgets.animation import CharacterAnimation
from src.tui.widgets.controls import TimerControls
from src.tui.widgets.display import TimerDisplay
from src.tui.widgets.focusmeter import FocusMeterWidget
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
		self.focus_meter = FocusMeter()

	def on_mount(self) -> None:
		"""Set up a poller to charge the focus meter."""
		# Update the focus meter every 1% of the timer duration
		self.set_interval((config.TIMER_MINUTES * 60) // 100, self.update_focus_meter)

	def update_focus_meter(self) -> None:
		"""If the timer is running, charge up the focus meter."""
		timer_display: TimerDisplay = self.query_one(TimerDisplay)
		if timer_display.is_running:
			self.focus_meter.charge_up(1)
			self.query_one(FocusMeterWidget).update_progress()

	def compose(self) -> ComposeResult:
		"""Child widgets for the app."""
		yield Header()

		with Horizontal(id="main_container"):
			with Vertical():
				yield CharacterStatsWidget(character=self.character)
				yield CharacterAnimation(character=self.character)

			with Vertical():
				yield PomodoroTimer()
				yield FocusMeterWidget(focus_meter=self.focus_meter)

		yield Footer()

	def action_pressbtn(self, btn_id: str) -> None:
		"""Trigger a button press by its ID."""
		self.query_one(btn_id, Button).press()

	def on_timer_controls_reset(self, message: TimerControls.Reset) -> None:
		"""Reset the focus meter and streak if the user abandons the session."""
		self.focus_meter.reset_streak()
		self.focus_meter.reset()
		self.query_one(FocusMeterWidget).update_progress()
		# self.notify(
		# 	"Session abandoned. Focus Streak has been reset.",
		# 	title="Streak Broken",
		# 	severity="warning",
		# )

	def on_pomodoro_timer_session_completed(
		self, message: PomodoroTimer.SessionCompleted
	) -> None:
		"""Handle successful completion of a focus session."""
		base_xp: int = config.XP_PER_SESSION
		bonus_xp: int = self.focus_meter.calculate_xp_bonus(base_xp)
		total_xp_to_add: int = base_xp + bonus_xp

		leveled_up: bool = self.character.add_xp(total_xp_to_add)

		# Sync stats and animation with new character state
		self.query_one(CharacterStatsWidget).update_stats()
		self.query_one(CharacterAnimation).update_art()

		# Determine if the session was focused enough to maintain the streak
		if self.focus_meter.charge >= 80:
			self.focus_meter.increment_streak()
		else:
			self.focus_meter.reset_streak()

		# Reset the meter for the next session
		self.focus_meter.reset()
		self.query_one(FocusMeterWidget).update_progress()

		if leveled_up:
			self.notify(
				f"Level Up! You reached level {self.character.level}!",
				title="Congratulations",
				severity="information",
			)
		else:
			self.notify("Session completed.", title="Success", severity="information")
