from typing import Any

from textual.reactive import reactive
from textual.widgets import Static

from src.core.character import Character


class CharacterAnimation(Static):
	"""A widget to display the character's animated growth stage."""

	art_display: reactive[str] = reactive("")

	def __init__(self, character: Character, *args: Any, **kwargs: Any) -> None:
		super().__init__(*args, **kwargs)
		self.character = character
		self.frame_index: int = 0

	def on_mount(self) -> None:
		"""Set up an interval to cycle through animation frames."""
		self.update_art()
		# Change frame every 0.5 seconds for a smooth animation
		self.set_interval(0.5, self.next_frame)

	def next_frame(self) -> None:
		"""Advance to the next frame in the animation sequence."""
		self.frame_index += 1
		self.update_art()

	def update_art(self) -> None:
		"""Fetch the correct ASCII art frame from the character object."""
		frames: list[str] = self.character.current_animation_frames

		# Ensure frame_index loops around safely
		self.art_display = frames[self.frame_index % len(frames)]

	def watch_art_display(self, new_art: str) -> None:
		"""When the art_display string changes, update the widget text."""
		self.update(new_art)
