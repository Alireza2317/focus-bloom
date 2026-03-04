from typing import Any

from textual.reactive import reactive
from textual.widgets import Static

from src.core.character import Character

# Define stages as lists of frames for animation
ASCII_STAGES = [
    [
        """
 
 
      .
 
 
        """,
        """
 
 
     ...
 
 
        """,
        """
 
 
      .
 
 
        """,
        """
 
 
     ...
 
 
        """
    ],
    [
        """
 
     🌱
      |
      |
 
        """,
        """
 
    🌱
     \\
      |
 
        """,
        """
 
     🌱
      |
      |
 
        """,
        """
 
      🌱
      /
      |
 
        """
    ],
    [
        """
      🌿
     \\|/
      |
      |
 
        """,
        """
     🌿
     /|/
      |
      |
 
        """,
        """
      🌿
     \\|/
      |
      |
 
        """,
        """
       🌿
     \\|\\
      |
      |
 
        """
    ],
    [
        """
      🌸
     \\|/
      |
      |
 
        """,
        """
     🌺
     /|/
      |
      |
 
        """,
        """
      🌸
     \\|/
      |
      |
 
        """,
        """
       🌺
     \\|\\
      |
      |
 
        """
    ]
]

class PlantAnimation(Static):
    """A widget to display the character's animated growth stage."""

    art_display: reactive[str] = reactive("")

    def __init__(self, character: Character, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.character = character
        self.frame_index = 0

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
        """Fetch the correct ASCII art frame based on the character's stage."""
        stage_idx = min(self.character.stage_index, len(ASCII_STAGES) - 1)
        frames = ASCII_STAGES[stage_idx]

        # Ensure frame_index loops around safely
        current_frame = frames[self.frame_index % len(frames)]

        self.art_display = current_frame

    def watch_art_display(self, new_art: str) -> None:
        """When the art_display string changes, update the widget text."""
        self.update(new_art)
