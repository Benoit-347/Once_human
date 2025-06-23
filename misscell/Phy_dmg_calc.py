def get_phy_damage(base_, attack_, weaponn_dmg_, weakspot_dmg_bonus,crit_rate, crit_damage, enemy_dmg_bonus, bullet_dmg_bonus, vulnerability, weakspot = False):
    if weakspot:
        return base_*(1+attack_)*(1+weaponn_dmg_)*(1+crit_rate*crit_damage)*(1+weakspot_dmg_bonus)*(1 + enemy_dmg_bonus)*(1+bullet_dmg_bonus)*(1 + vulnerability)
    else:
        return base_*(1+attack_)*(1+weaponn_dmg_)*(1+crit_rate*crit_damage)*(1 + enemy_dmg_bonus)*(1+bullet_dmg_bonus)*(1 + vulnerability)
    
weapon_base_atk = 2591
weakspot_dmg_bonus = 0.95
crit_rate = 0   #0.02
crit_dmg = 0.26
attack = -0.1

weakspot_dmg_bonus += 1
weapon_dmg_bonus = 0
enemy_dmg_bonus = 0
vulnerability = 0.16
bullet_dmg_bonus = 0.0554   # INACCURACY 1

"""
Damage sources:
Bullet type
Damage type
Weapon calib
Weapon self
Cradle
Mods
Sets
substats
"""

flag_weakspot = 1
damage = get_phy_damage(weapon_base_atk, attack, weapon_dmg_bonus, weakspot_dmg_bonus, crit_rate, crit_dmg, enemy_dmg_bonus, bullet_dmg_bonus, vulnerability, flag_weakspot)
result = 8422
print(f"The damage is: {damage:.2f} \nMatch ratio: {damage/result*100:.0f}%\n" ,sep = '', end = '')