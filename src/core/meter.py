class FocusMeter:
	"""Tracks focus charge and session streaks for bonus XP."""

	STREAK_MULTIPLIERS: dict[int, float] = {
		1: 1.0,
		2: 1.5,
		3: 2.0,
		4: 2.5,
	}

	def __init__(self):
		self._charge: int = 0
		self._streak: int = 1

	@property
	def charge(self) -> int:
		return self._charge

	@property
	def streak(self) -> int:
		return self._streak

	def charge_up(self, amount: int) -> None:
		"""Increase the meter's charge, capping at 100 percent."""
		self._charge = min(100, self._charge + amount)

	def calculate_xp_bonus(self, base_xp: int) -> int:
		"""Calculate bonus XP based on charge and streak multiplier."""
		# Get the multiplier, defaulting to the max if streak is higher
		multiplier: float = self.STREAK_MULTIPLIERS.get(
			self._streak, max(self.STREAK_MULTIPLIERS.values())
		)

		# Bonus is proportional to charge, then multiplied by streak
		bonus_xp: int = int((self._charge / 100) * base_xp * multiplier)

		return bonus_xp

	def reset(self) -> None:
		"""Reset the charge for a new session."""
		self._charge = 0

	def increment_streak(self) -> None:
		"""Increment the session streak."""
		self._streak += 1

	def reset_streak(self) -> None:
		"""Reset the streak counter to 1."""
		self._streak = 1
