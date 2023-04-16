
import esper
import pygame

from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_velocity import CVelocity
from src.ecs.components.c_surface import CSurface
from src.ecs.components.tags.c_tag_bullet import CTagBullet

def system_screen_bounce_player(world:esper.World, screen:pygame.Surface):
    screen_rect = screen.get_rect()
    components = world.get_components(CTransform, CVelocity, CSurface, CTagBullet)

    c_t:CTransform
    c_s:CSurface
    for bullet_entity, (c_t, c_s, c_e) in components:
        cuad_rect = c_s.surf.get_rect(topleft=c_t.pos)
        if cuad_rect.left < 0 or cuad_rect.right > screen_rect.width:
            world.delete_entity(bullet_entity)
            cuad_rect.clamp_ip(screen_rect)
            
        if cuad_rect.top < 0 or cuad_rect.bottom > screen_rect.height:
            world.delete_entity(bullet_entity)
            cuad_rect.clamp_ip(screen_rect)
            