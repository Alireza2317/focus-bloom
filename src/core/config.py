class Config:
	"""Centralized configuration for the application."""

	DEBUG_MODE = True

	if DEBUG_MODE:
		# Rapid testing settings
		TIMER_MINUTES = 1
		TIMER_DEDUCTION = 30
		AUTO_RESET = True
		XP_PER_SESSION = 100
	else:
		# Production Pomodoro settings
		TIMER_MINUTES = 25
		TIMER_DEDUCTION = 1
		AUTO_RESET = False
		XP_PER_SESSION = 50
