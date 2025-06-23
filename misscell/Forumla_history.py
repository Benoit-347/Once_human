# version history during building of formula:

def get_phy_damage(base_, attack_, weaponn_dmg_, weakspot_dmg_,crit_rate, crit_damage, weakspot = False):
    if weakspot:
        return base_*(1+attack_)*(1+weaponn_dmg_)*(1+crit_rate*crit_damage)*(1+weakspot_dmg_)
    else:
        return base_*(1+attack_)*(1+weaponn_dmg_)*(1+crit_rate*crit_damage)
    

def get_phy_damage_2(base_, attack_, weaponn_dmg_, weakspot_multiplier, weakspot_dmg_bonus,crit_rate, crit_damage, weakspot = False):
    if weakspot:
        return base_*(1+attack_)*(1+weaponn_dmg_)*(1+crit_rate*crit_damage)*(1+weakspot_multiplier*(1+weakspot_dmg_bonus))
    else:
        return base_*(1+attack_)*(1+weaponn_dmg_)*(1+crit_rate*crit_damage)
    

def get_phy_damage_3(base_, attack_, weaponn_dmg_, weakspot_multiplier, weakspot_dmg_bonus,crit_rate, crit_damage, enemy_dmg_bonus = 0, weakspot = False):
    if weakspot:
        return base_*(1+attack_)*(1+weaponn_dmg_)*(1+crit_rate*crit_damage)*(1+weakspot_multiplier*(1+weakspot_dmg_bonus))*(1 + enemy_dmg_bonus)
    else:
        return base_*(1+attack_)*(1+weaponn_dmg_)*(1+crit_rate*crit_damage)*(1 + enemy_dmg_bonus)


def get_phy_damage_4(base_, attack_, weaponn_dmg_, weakspot_dmg_bonus,crit_rate, crit_damage, enemy_dmg_bonus, bullet_dmg_bonus, vulnerability, weakspot = False):
    if weakspot:
        return base_*(1+attack_)*(1+weaponn_dmg_)*(1+crit_rate*crit_damage)*(1+weakspot_dmg_bonus)*(1 + enemy_dmg_bonus)*(1+bullet_dmg_bonus)*(1 + vulnerability)
    else:
        return base_*(1+attack_)*(1+weaponn_dmg_)*(1+crit_rate*crit_damage)*(1 + enemy_dmg_bonus)*(1+bullet_dmg_bonus)*(1 + vulnerability)


# Bounce
def get_bounce_normal_damage(bounce_dmg_bonus, bounce_crit_dmg_bonus, base_, attack_, weaponn_dmg_, weakspot_dmg_bonus,crit_rate, crit_damage, enemy_dmg_bonus, bullet_dmg_bonus, vulnerability, weakspot = False):

    bounce = 0.4*base_*(1+attack_)*(1+weaponn_dmg_)*(1+crit_rate*(crit_damage+bounce_crit_dmg_bonus))*(1 + enemy_dmg_bonus)*(1+bounce_dmg_bonus)*(1+bullet_dmg_bonus)*(1 + vulnerability)

    return bounce

def get_bounce_damage(bounce_chance, bounce_hits, bounce_dmg_bonus, bounce_crit_dmg_bonus, base_, attack_, weaponn_dmg_, weakspot_dmg_bonus,crit_rate, crit_damage, enemy_dmg_bonus, bullet_dmg_bonus, vulnerability, weakspot = False):
    if weakspot:
        damage = base_*(1+attack_)*(1+weaponn_dmg_)*(1+crit_rate*crit_damage)*(1+weakspot_dmg_bonus)*(1 + enemy_dmg_bonus)*(1+bullet_dmg_bonus)*(1 + vulnerability)
    else:
        damage = base_*(1+attack_)*(1+weaponn_dmg_)*(1+crit_rate*crit_damage)*(1 + enemy_dmg_bonus)*(1+bullet_dmg_bonus)*(1 + vulnerability)

    one_bounce = 0.4*base_*(1+attack_)*(1+weaponn_dmg_)*(1+crit_rate*(crit_damage+bounce_crit_dmg_bonus))*(1 + enemy_dmg_bonus)*(1+bounce_dmg_bonus)*(1+bullet_dmg_bonus)*(1 + vulnerability)
    bounce_hits_per_shot = bounce_chance*bounce_hits
    one_bounce_weakspot_avg = one_bounce*(0.52 + 0.48*(1+ weakspot_dmg_bonus))    # obv data is 52, 48      #theory: 50, 50
    avg_bounce = bounce_hits_per_shot*one_bounce_weakspot_avg

    Total_hit_dmg = damage + avg_bounce
    
    return Total_hit_dmg
