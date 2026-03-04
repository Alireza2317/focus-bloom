class Character:
	"""Represents the user's virtual plant character."""

	def __init__(self, name: str = "Focus Plant"):
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
	def stage(self) -> str:
		"""Determines the current life stage based on level."""
		if self.level < 5:
			return "Seed"
		elif self.level < 10:
			return "Sprout"
		elif self.level < 15:
			return "Bud"
		else:
			return "Flower"
