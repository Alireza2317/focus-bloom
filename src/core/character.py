from abc import ABC, abstractmethod
from typing import TypedDict


class CharacterData(TypedDict):
	"""Type definition for character JSON data structure."""

	icon: str
	stages: list[str]
	frames: list[list[str]]


class Character(ABC):
	"""Represents the user's virtual character base."""

	def __init__(self, name: str):
		self.name = name
		self.xp = 0
		self.level = 1
		# Animation frame list in the order of its stages
		self._animations: list[list[str]] = []

	def add_xp(self, amount: int) -> bool:
		"""Adds XP to the character. Returns True if leveled up, False otherwise."""
		self.xp += amount
		return self._check_levelup()

	def _check_levelup(self) -> bool:
		"""Internal method to handle leveling up if XP threshold is met."""
		leveled_up = False
		while self.xp >= self.xp_for_next_level:
			self.xp -= self.xp_for_next_level
			self.level += 1
			leveled_up = True
		return leveled_up

	@property
	def xp_for_next_level(self) -> int:
		"""Calculates the XP required to reach the next level."""
		# Simple scaling: 10 XP for lvl 2, 20 for lvl 3, etc.
		return self.level * 10

	@property
	@abstractmethod
	def stage_index(self) -> int:
		"""Determines the current life stage index based on level."""
		pass

	@property
	@abstractmethod
	def stage_name(self) -> str:
		"""Returns the name of the current stage."""
		pass

	@property
	@abstractmethod
	def icon(self) -> str:
		"""Returns a string icon representing the character type."""
		pass

	@property
	@abstractmethod
	def current_animation_frames(self) -> list[str]:
		"""
		Returns a list of strings representing animation frames for the current stage.
		"""
		pass


class JSONCharacter(Character):
	"""A base character that loads animations from a JSON file."""

	JSON_FILENAME: str = ""

	ICON: str = ""
	STAGE_NAMES: list[str] = []

	def __init__(self, name: str, filename: str):
		super().__init__(name)
		self.JSON_FILENAME = filename
		self._load_json_file()

	def _load_json_file(self) -> None:
		import json
		from pathlib import Path

		# Assuming src is the parent directory of this file's parent
		src_directory: Path = Path(__file__).parent.parent
		filepath: Path = src_directory / "assets" / self.JSON_FILENAME

		content: CharacterData = json.loads(filepath.read_text())

		self.ICON = content["icon"]
		self.STAGE_NAMES = content["stages"]
		self._animations = content["frames"]

	@property
	def stage_index(self) -> int:
		"""Return the stage index, capped at the last available stage."""
		level_cutoffs: list[int] = [
			cutoff
			for cutoff in range(1, len(self.STAGE_NAMES) * 2 + 1)
			if cutoff % 2 == 0
		]

		index: int = 0
		for cutoff in level_cutoffs:
			if self.level < cutoff:
				return min(len(self.STAGE_NAMES) - 1, index)
			index += 1

		return len(self.STAGE_NAMES) - 1

	@property
	def stage_name(self) -> str:
		stage_idx = min(self.stage_index, len(self.STAGE_NAMES) - 1)
		return self.STAGE_NAMES[stage_idx]

	@property
	def icon(self) -> str:
		return self.ICON

	@property
	def current_animation_frames(self) -> list[str]:
		if not self._animations:
			self._load_json_file()

		try:
			return self._animations[self.stage_index]

		except IndexError:
			return ["Missing Art Asset!"]
