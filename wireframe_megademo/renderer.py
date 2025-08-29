import pygame  #KGNINJA
from . import config  #KGNINJA

class Renderer:  #KGNINJA
    def __init__(self, width, height):  #KGNINJA
        self.width = width  #KGNINJA
        self.height = height  #KGNINJA
        self._grid_overlay = False  #KGNINJA

    def run(self, timeline, force_mock=False, grid=False):  #KGNINJA
        self._grid_overlay = grid  #KGNINJA
        if force_mock:  #KGNINJA
            if grid:  #KGNINJA
                print("[Mock] Grid overlay enabled")  #KGNINJA
            for frame, _ in enumerate(timeline):  #KGNINJA
                print(f"[Mock] Frame {frame}")  #KGNINJA
            return  #KGNINJA
        pygame.init()  #KGNINJA
        screen = pygame.display.set_mode((self.width, self.height))  #KGNINJA
        clock = pygame.time.Clock()  #KGNINJA
        for frame, _ in enumerate(timeline):  #KGNINJA
            for event in pygame.event.get():  #KGNINJA
                if event.type == pygame.QUIT:  #KGNINJA
                    return  #KGNINJA
            screen.fill((0, 0, 0))  #KGNINJA
            if grid:  #KGNINJA
                draw_grid(screen, config.GRID_OVERLAY_SPACING)  #KGNINJA
            pygame.display.flip()  #KGNINJA
            clock.tick(config.MOCK_FRAME_RATE)  #KGNINJA
        pygame.quit()  #KGNINJA

def draw_grid(surface, spacing):  #KGNINJA
    w, h = surface.get_size()  #KGNINJA
    overlay = pygame.Surface((w, h), pygame.SRCALPHA)  #KGNINJA
    for x in range(0, w, spacing):  #KGNINJA
        pygame.draw.line(overlay, (0, 255, 0, 242), (x, 0), (x, h), 1)  #KGNINJA
        pygame.draw.line(overlay, (0, 255, 0, 46), (x + spacing // 2, 0), (x + spacing // 2, h), 2)  #KGNINJA
    for y in range(0, h, spacing):  #KGNINJA
        pygame.draw.line(overlay, (0, 255, 0, 242), (0, y), (w, y), 1)  #KGNINJA
        pygame.draw.line(overlay, (0, 255, 0, 46), (0, y + spacing // 2), (w, y + spacing // 2), 2)  #KGNINJA
    surface.blit(overlay, (0, 0))  #KGNINJA
