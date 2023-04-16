
import esper
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_transform import CTransform
from src.ecs.components.tags.c_tag_enemy import CTagEnemy
from src.ecs.components.tags.c_tag_bullet import CTagBullet

def system_collision_bullet_enemy(world: esper.World):
    components_enemy = world.get_components(CSurface, CTransform, CTagEnemy)
    components_bullet = world.get_components(CSurface, CTransform, CTagBullet)

    for enemy_entity, (c_e_s, c_e_t, _) in components_enemy:
        ene_rect = c_e_s.surf.get_rect(topleft = c_e_t.pos)
        for bullet_entity, (c_b_s, c_b_t, _) in components_bullet:
            bull_rect = c_b_s.surf.get_rect(topleft = c_b_t.pos)
            if ene_rect.colliderect(bull_rect):
                world.delete_entity(enemy_entity)
                world.delete_entity(bullet_entity)