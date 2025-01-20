def get_rate(time, money):
    return money/time

def calc_damage(base_atk, atk_, weap_, crit_R, crit_D, bonus_enemy_):
    return base_atk*(1+atk_)*(1+weap_)*(1+crit_R*crit_D)*(1+bonus_enemy_)

base_atk = 250
#print(calc_damage(base_atk, atk_, weap_, crit_R, crit_D, bonus_enemy_))