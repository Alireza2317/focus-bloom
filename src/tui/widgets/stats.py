from typing import Any

from textual.reactive import reactive
from textual.widgets import Static

from src.core.character import Character


class CharacterStatsWidget(Static):
	"""A widget to display character progress."""

	# We make the display string reactive so it updates automatically
	stats_display: reactive[str] = reactive("")

	def __init__(self, character: Character, *args: Any, **kwargs: Any) -> None:
		super().__init__(*args, **kwargs)
		self.character = character

	def on_mount(self) -> None:
		"""Update the display initially."""
		self.update_stats()

	def update_stats(self) -> None:
		"""Format the character's stats into a string."""
		self.stats_display = (
			f"{self.character.icon} {self.character.name} | "
			+ f"Stage: {self.character.stage_name.title(): >8} | "
			+ f"Level: {self.character.level: >2} | "
			+ f"XP: {self.character.xp: >3}/{self.character.xp_for_next_level: >3}"
		)

	def watch_stats_display(self, new_stats: str) -> None:
		"""When the stats_display string changes, update the widget text."""
		self.update(new_stats)
