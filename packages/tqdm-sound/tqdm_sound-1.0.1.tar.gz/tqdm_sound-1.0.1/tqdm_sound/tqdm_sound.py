import logging
import random
import time
from typing import Optional, Iterator

import pygame
from importlib import resources
from pynput import mouse, keyboard
from tqdm import tqdm

# Configure logging
logging.basicConfig(level=logging.CRITICAL)
logger = logging.getLogger(__name__)


class TqdmSound:
    """Container class for sound-enabled progress bars."""

    def __init__(
            self,
            theme: str = "ryoji_ikeda",
            volume: int = 100,
            background_volume: int = 50,
            activity_mute_seconds: Optional[int] = None,
    ):
        """Initialize the TqdmSound container.

        Args:
            theme: Theme name for sound files.
            volume: Foreground volume percentage (0-100).
            background_volume: Background volume percentage (0-100).
            activity_mute_seconds: Duration to mute sounds after user activity.
        """
        # Validate foreground volume
        if not 0 <= volume <= 100:
            raise ValueError("Volume must be between 0 and 100")

        # Validate background volume
        if not 0 <= background_volume <= 100:
            raise ValueError("Background volume must be between 0 and 100")

        # Initialize pygame mixer
        if not pygame.mixer.get_init():
            pygame.mixer.init()

        # Convert volumes from percentages (0-100) to normalized values (0-1)
        self.volume = volume / 100.0
        self.background_volume = background_volume / 100.0

        # Store original values for reference
        self.theme = theme
        self.activity_mute_seconds = activity_mute_seconds

        # Initialize sounds
        self.sounds = {}
        self.click_sounds = []
        self._load_sounds()

        # Initialize activity tracking
        self.last_activity_time = time.time()
        self._setup_activity_monitors()

    def _setup_activity_monitors(self):
        """Set up mouse and keyboard listeners to track user activity."""
        self.mouse_listener = mouse.Listener(
            on_move=self._update_activity,
            on_click=self._update_activity,
            on_scroll=self._update_activity
        )
        self.keyboard_listener = keyboard.Listener(on_press=self._update_activity)

        # Start the listeners
        self.mouse_listener.start()
        self.keyboard_listener.start()

        # Set initial activity time
        if self.activity_mute_seconds:
            self.last_activity_time = time.time() - self.activity_mute_seconds

    def _update_activity(self, *args, **kwargs):
        """Update the last activity timestamp."""
        self.last_activity_time = time.time()

    def _load_sounds(self):
        """Load all required sounds from the theme directory."""
        # Get the base path for sounds
        sounds = resources.files('tqdm_sound').joinpath('sounds')
        self.theme_path = sounds / self.theme

        if not self.theme_path.exists():
            raise FileNotFoundError(f"Theme directory {self.theme_path} not found")

        # Load click sounds
        self.click_sounds = [pygame.mixer.Sound(str(s)) for s in self.theme_path.glob('click_*.wav')]

        # Load main sounds
        sound_files = {
            "start": "start_tone.wav",
            "semi_major": "semi_major.wav",
            "mid": "mid_tone.wav",
            "end": "end_tone.wav",
            "background": "background_tone.wav",
            "program_end": "program_end_tone.wav"
        }

        for name, filename in sound_files.items():
            file_path = self.theme_path / filename
            if file_path.exists():
                self.sounds[name] = pygame.mixer.Sound(str(file_path))
            else:
                raise FileNotFoundError(f"Sound file not found: {file_path}")

        # Set initial volumes (using normalized values)
        self.set_volume(self.volume, mute=False, background_volume=self.background_volume)

    def set_volume(self, volume: float, mute: bool = False, background_volume: Optional[float] = None):
        """Set the volume for all sounds using normalized values (0-1).

        Args:
            volume: Foreground volume (normalized 0-1).
            mute: Whether to mute all sounds.
            background_volume: Optional override for background volume (normalized 0-1).
        """
        # Update stored normalized volume values
        self.volume = 0.0 if mute else volume
        if background_volume is not None:
            self.background_volume = 0.0 if mute else background_volume

        # Apply volumes to sounds
        for name, sound in self.sounds.items():
            if name == "background":
                sound.set_volume(self.background_volume)
            else:
                sound.set_volume(self.volume)

        # Apply to click sounds
        for sound in self.click_sounds:
            sound.set_volume(self.volume)

    def play_random_click(self):
        """Play a random click sound from available click sounds."""
        if self.click_sounds:
            random.choice(self.click_sounds).play()

    def play_sound(self, sound_name: str, loops: int = 0):
        """Play a specific sound by name.

        Args:
            sound_name: Name of the sound to play.
            loops: Number of times to loop the sound.
        """
        if sound_name in self.sounds:
            self.sounds[sound_name].play(loops=loops)

    def play_final_end_tone(self, volume: int = 100):
        """Play the final end tone sound using an external volume percentage.

        Args:
            volume: Volume percentage (0-100) to temporarily use.
        """
        if "program_end" in self.sounds:
            original_vol = self.sounds["program_end"].get_volume()
            # Convert external percentage to normalized value
            temp_vol = volume / 100.0

            self.sounds["program_end"].set_volume(temp_vol)
            self.sounds["program_end"].play()

            pygame.time.wait(int(self.sounds["program_end"].get_length() * 1000))
            self.sounds["program_end"].set_volume(original_vol)

    def play_sound_file(self, file_name: str, volume: Optional[int] = None) -> None:
        """
        Play a specific sound file with an optional volume override.

        Args:
            file_name: The name of the sound file.
            volume: Optional volume percentage (0-100) to override the default.
        """
        sound_path = self.theme_path / file_name
        sound = pygame.mixer.Sound(str(sound_path))

        # Use provided percentage override (converted to normalized) or the instance's normalized volume
        vol: float = volume / 100.0 if volume is not None else self.volume
        sound.set_volume(vol)
        sound.play()

        pygame.time.wait(int(sound.get_length() * 1000))

    @staticmethod
    def sleep(duration: float):
        pygame.time.wait(duration * 1000)

    def progress_bar(
            self,
            iterable,
            desc: str,
            volume: Optional[int] = None,
            background_volume: Optional[int] = None,
            end_wait: float = 0.04,
            ten_percent_ticks: bool = False,
            **kwargs
    ):
        """Create a sound-enabled progress bar.

        Args:
            iterable: The iterable to wrap.
            desc: Description for the progress bar.
            volume: Foreground volume override (0-100).
            background_volume: Background volume override (0-100).
            end_wait: Time to wait after finishing.
            ten_percent_ticks: If true, sound a tone at each 10% of the total steps.
            **kwargs: Additional arguments for tqdm.

        Returns:
            A sound-enabled progress bar.
        """
        # Convert external percentage overrides to normalized values (0-1)
        vol = self.volume if volume is None else volume / 100.0
        bg_vol = self.background_volume if background_volume is None else background_volume / 100.0

        # Return a new SoundProgressBar with normalized volumes
        return SoundProgressBar(
            iterable,
            desc=desc,
            volume=vol,
            background_volume=bg_vol,
            end_wait=end_wait,
            ten_percent_ticks=ten_percent_ticks,
            sound_manager=self,
            **kwargs
        )

    def close(self):
        """Close listeners and clean up resources."""
        # Stop listeners
        if hasattr(self, 'mouse_listener') and self.mouse_listener.running:
            self.mouse_listener.stop()
        if hasattr(self, 'keyboard_listener') and self.keyboard_listener.running:
            self.keyboard_listener.stop()

        # Stop any playing sounds
        pygame.mixer.stop()


class SoundProgressBar(tqdm):
    """Progress bar that plays sounds at key moments."""

    def __init__(
            self,
            iterable,
            desc: str,
            volume: float,
            background_volume: float,
            end_wait: float,
            ten_percent_ticks: bool,
            sound_manager: TqdmSound,
            **kwargs
    ):
        """Initialize the sound progress bar.

        Args:
            iterable: The iterable to wrap.
            desc: Description for the progress bar.
            volume: Foreground volume (normalized 0-1).
            background_volume: Background volume (normalized 0-1).
            end_wait: Time to wait after finishing.
            ten_percent_ticks: If true, sound a tone at each 10% of the total steps.
            sound_manager: The sound manager to use.
            **kwargs: Additional arguments for tqdm.
        """
        self.sound_manager = sound_manager
        self.volume = volume
        self.background_volume = background_volume
        self.end_wait = end_wait
        self.ten_percent_ticks = ten_percent_ticks
        self.mid_sound_played = False

        # Initialize the tqdm progress bar
        super().__init__(iterable, desc=desc, **kwargs)

    def _update_volume(self):
        """Update sound volume based on recent user activity."""
        mute = False
        if self.sound_manager.activity_mute_seconds and (
                time.time() - self.sound_manager.last_activity_time < self.sound_manager.activity_mute_seconds):
            mute = True

        self.sound_manager.set_volume(self.volume, mute, self.background_volume)

    def __iter__(self) -> Iterator:
        """Iterate over items with sound effects."""
        # Play start sounds
        self.sound_manager.play_sound("start")
        self.sound_manager.play_sound("background", loops=-1)

        # Track which percentage marks we've played sounds for
        played_percentages = {0, 50, 100}  # Skip start (0%), mid (50%), and end (100%)

        try:
            # Iterate with progress and sounds
            for i, item in enumerate(super().__iter__()):
                self._update_volume()
                self.sound_manager.play_random_click()

                # Calculate current progress percentage
                if self.total:
                    current_percentage = int((i + 1) / self.total * 100)

                    # Play mid-sound at 50% progress
                    if not self.mid_sound_played and current_percentage >= 50:
                        self.sound_manager.play_sound("mid")
                        self.mid_sound_played = True

                    # Play semi_major sound at every 10% mark (except 0%, 50%, 100%)
                    if self.ten_percent_ticks:
                        current_ten_percent = (current_percentage // 10) * 10
                        if current_ten_percent not in played_percentages and current_percentage >= current_ten_percent:
                            self.sound_manager.play_sound("semi_major")
                            played_percentages.add(current_ten_percent)

                yield item
        finally:
            # Finalize progress
            self.sound_manager.play_sound("end")
            if "background" in self.sound_manager.sounds:
                self.sound_manager.sounds["background"].stop()

            pygame.time.wait(int(self.end_wait * 1000))
