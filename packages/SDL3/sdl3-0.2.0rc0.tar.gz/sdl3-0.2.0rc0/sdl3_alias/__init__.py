"""An alias package for PySDL3."""

__version__ = "0.2.0rc0"

from sdl3 import *

SDL_LOGGER.Log(SDL_LOGGER.Warning, "You are using an alias module, please use the 'sdl3' module instead.")