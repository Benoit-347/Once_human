"""def get_phy_damage(base_, attack_, weaponn_dmg_, weakspot_dmg_bonus,crit_rate, crit_damage, enemy_dmg_bonus, bullet_dmg_bonus, vulnerability, weakspot = False):
    if weakspot:
        return base_*(1+attack_)*(1+weaponn_dmg_)*(1+crit_rate*crit_damage)*(1+weakspot_dmg_bonus)*(1 + enemy_dmg_bonus)*(1+bullet_dmg_bonus)*(1 + vulnerability)
    else:
        return base_*(1+attack_)*(1+weaponn_dmg_)*(1+crit_rate*crit_damage)*(1 + enemy_dmg_bonus)*(1+bullet_dmg_bonus)*(1 + vulnerability)
"""

# weap and set effects
weapon_base_atk = 2238
weakspot_dmg_bonus = 0.8
crit_rate = 0.02 + 0.05 + 0.15  #make this 0 at end to remove crit effect
crit_dmg = 0.3
attack = 0

weapon_dmg_bonus = 0.1
enemy_dmg_bonus = 0
bullet_dmg_bonus = 0.05 # ammo budd

# calib
crit_rate += 0.062+0.078


"""
Damage sources:
Bullet type y
Damage type 
Weapon calib y
Weapon self y
Cradle y
Mods 
Sets y
substats
"""
# bullseye
vulnerability = 0
bullseye = 1

if bullseye:
    vulnerability = 0.16


# mods
enemy_dmg_bonus += 0.08 + 0.06 + 0.08
weapon_dmg_bonus += 0.06 + 0.024 + 0.048 + 0.2
crit_dmg += 0.15 + 0.12 + 0.12 + 0.15 + 0.15
weakspot_dmg_bonus += 0

# bounce effect
# Mods:
bounce_dmg_bonus = 0.06 + 0.06 + 0.15*2
bounce_crit_dmg_bonus = 0.1 + 0.25
bounce_dmg_bonus += 1.25/3  # every 3rd shot + 125% bouce dmg (every 7th, but HAMR's sharp blade triggers 2 bounces)


# lone wolf
crit_dmg += 0.08*2


# cradle:
weapon_dmg_bonus += 0.15    # when using snipers
weapon_dmg_bonus += 0.15 * (4/9)    # affects only first 4 bullets      
bounce_dmg_bonus += 0.25 * (5/6.75)  # buff triggers after first bounce trigger (5.75/6.75)
weakspot_dmg_bonus += 0.2   # targets marked with bullseye
bounce_dmg_bonus += 0.05*(5/2)  # max 5,  triggers every time bounce triggers. (skips first one, hence 5.75/2)

# print(f"The crit damage is: {crit_dmg*100:.2f}%\ncrit rate is: {crit_rate*100:.2f}")

flag_weakspot = 1
# damage = get_phy_damage(weapon_base_atk, attack, weapon_dmg_bonus, weakspot_dmg_bonus, crit_rate, crit_dmg, enemy_dmg_bonus, bullet_dmg_bonus, vulnerability, flag_weakspot)
# result = 8572
# print(f"The Single wk/toggle damage is: {damage:.2f} \nAbove Match ratio:   {damage/result*100:.0f}%\n" ,sep = '', end = '')


# MAIN PHY DMG DONE, INCLUDING BOUNCE:


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

#Given for HAMR
bounce_chance = 0.73    # changing to observed -2, theory: 75
bounce_hits = 4

#calc
Total_per_hit = get_bounce_damage(bounce_chance, bounce_hits, bounce_dmg_bonus, bounce_crit_dmg_bonus, weapon_base_atk, attack, weapon_dmg_bonus, weakspot_dmg_bonus, crit_rate, crit_dmg, enemy_dmg_bonus, bullet_dmg_bonus, vulnerability, flag_weakspot)

# full done.




# testing
# database of manual per hit tests:
result = ((348 + 293 + 457 + 492 + 421 + 450 + 358 + 562 + 450 + 366 + 355)*1000/11 - 15000) / 9 # Non cradle ((250 + 285 + 369 + 385 + 299 + 341 + 267 + 356)*1000/8 - 14000) / 9
print(f"\nPer shot dmg is: {Total_per_hit:.2f}\t\tManual: {result}\nTheory's Match ratio:   {Total_per_hit/result*100:.0f}%\n")



# bounce weakspot data
"""
wk =        2 + 1 + 2 + 2 + 2 + 0 + 4 + 1 + 2 + 4 + 1 + 1 + 1 + 1 + 1 + 4 + 2 + 0 + 1 + 2 + 2 + 4 + 2 + 2 + 0 + 3 + 2 + 2 + 3 + 3 + 1 + 3 + 0 + 4
normal =    2 + 3 + 2 + 2 + 2 + 4 + 0 + 3 + 2 + 0 + 3 + 3 + 3 + 3 + 3 + 0 + 2 + 4 + 3 + 2 + 2 + 0 + 2 + 2 + 4 + 1 + 2 + 2 + 1 + 1 + 3 + 1 + 4 + 0
print(f"Chance of bounce wk is: {wk/(wk+normal):.2f}%")"""