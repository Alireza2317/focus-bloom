class _Config:
	"""
	A singleton-like class to hold all configuration settings.
	An instance of this is created and exported as `config`.
	"""

	def __init__(self):
		self.set_production_mode()

	def set_production_mode(self):
		"""Sets the configuration for a standard Pomodoro session."""
		self.DEBUG_MODE = False
		self.TIMER_MINUTES = 25
		self.TIMER_DEDUCTION = 1
		self.AUTO_RESET = False
		self.XP_PER_SESSION = 50

	def set_debug_mode(self):
		"""Sets the configuration for rapid testing and debugging."""
		self.DEBUG_MODE = True
		self.TIMER_MINUTES = 1
		self.TIMER_DEDUCTION = 60
		self.AUTO_RESET = True
		self.XP_PER_SESSION = 100


config = _Config()
