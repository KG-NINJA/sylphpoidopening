import os  #KGNINJA
import pygame  #KGNINJA
from . import config  #KGNINJA
from .renderer import draw_grid  #KGNINJA

def render_mock_sequence(width, height, total_frames, fps, grid=False):  #KGNINJA
    os.makedirs("frames", exist_ok=True)  #KGNINJA
    for frame in range(total_frames):  #KGNINJA
        surface = pygame.Surface((width, height))  #KGNINJA
        surface.fill((0, 0, 0))  #KGNINJA
        if grid:  #KGNINJA
            draw_grid(surface, config.GRID_OVERLAY_SPACING)  #KGNINJA
        pygame.image.save(surface, os.path.join("frames", f"frame_{frame:04d}.png"))  #KGNINJA
        print(f"[Mock] Saved frame {frame}")  #KGNINJA
