def damage(base_, attack_, weaponn_dmg_, weakspot_dmg_, weakspot = False):
    if weakspot:
        return base_*(1+attack_)*(1+weaponn_dmg_)*(1+weakspot_dmg_)
    else:
        return base_*(1+attack_)*(1+weaponn_dmg_)
print(damage())