import pygame

pygame.init()
font = pygame.font.Font(None, 30)


def debug(info, y=10, x=10):
    dispay_surface = pygame.display.get_surface()
    debug_surf = font.render(str(info), True, 'White')
    debug_rect = debug_surf.get_rect(topleft=(x, y))
    pygame.draw.rect(dispay_surface, 'Black', debug_rect)
    dispay_surface.blit(debug_surf, debug_rect)
