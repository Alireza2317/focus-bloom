from abc import ABC, abstractmethod


class Character(ABC):
	"""Represents the user's virtual character base."""

	def __init__(self, name: str):
		self.name = name
		self.xp = 0
		self.level = 1

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
		# Simple scaling: 100 XP for lvl 2, 200 for lvl 3, etc.
		return self.level * 100

	@property
	def stage_index(self) -> int:
		"""Determines the current life stage index based on level."""
		if self.level < 2:
			return 0
		elif self.level < 4:
			return 1
		elif self.level < 6:
			return 2
		else:
			return 3

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
		"""Returns a list of strings representing animation frames for the current stage."""
		pass


class PlantCharacter(Character):
	"""A specific plant-based character implementation."""

	STAGE_NAMES = ["Seed", "Sprout", "Bud", "Flower"]

	ANIMATION_STAGES = [
		[
			"""\n \n \n      .\n \n \n        """,
			"""\n \n \n     ...\n \n \n        """,
			"""\n \n \n      .\n \n \n        """,
			"""\n \n \n     ...\n \n \n        """
		],
		[
			"""\n \n     🌱\n      |\n      |\n \n        """,
			"""\n \n    🌱\n     \\\n      |\n \n        """,
			"""\n \n     🌱\n      |\n      |\n \n        """,
			"""\n \n      🌱\n      /\n      |\n \n        """
		],
		[
			"""\n      🌿\n     \\|/\n      |\n      |\n \n        """,
			"""\n     🌿\n     /|/\n      |\n      |\n \n        """,
			"""\n      🌿\n     \\|/\n      |\n      |\n \n        """,
			"""\n       🌿\n     \\|\\\n      |\n      |\n \n        """
		],
		[
			"""\n      🌸\n     \\|/\n      |\n      |\n \n        """,
			"""\n     🌺\n     /|/\n      |\n      |\n \n        """,
			"""\n      🌸\n     \\|/\n      |\n      |\n \n        """,
			"""\n       🌺\n     \\|\\\n      |\n      |\n \n        """
		]
	]

	@property
	def stage_name(self) -> str:
		stage_idx = min(self.stage_index, len(self.STAGE_NAMES) - 1)
		return self.STAGE_NAMES[stage_idx]

	@property
	def icon(self) -> str:
		return "🌱"

	@property
	def current_animation_frames(self) -> list[str]:
		stage_idx = min(self.stage_index, len(self.ANIMATION_STAGES) - 1)
		return self.ANIMATION_STAGES[stage_idx]

