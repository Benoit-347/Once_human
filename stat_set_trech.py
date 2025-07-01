# weap and set effects
weapon_base_atk = 2238
weakspot_dmg_bonus = 0.8
crit_rate = 0.02 + 0.05 + 0.15  #at end make this 0 to remove crit effect
crit_dmg = 0.3
attack = 0
weapon_dmg_bonus = 0
#trech set:
weapon_dmg_bonus += 0.22

enemy_dmg_bonus = 0
bullet_dmg_bonus = 0.05 # ammo budd

# calib
crit_rate += 0.062+0.078

# bullseye
vulnerability = 0
bullseye = 1
if bullseye:
    vulnerability = 0.16

# mods
enemy_dmg_bonus += 0.06 + 0.06 + 0.08
weapon_dmg_bonus += 0.06 + 0.024 + 0.048 + 0.2  #0.2-covered advance
crit_dmg += 0.15 + 0.12 + 0.12 + 0.15 + 0.15
weakspot_dmg_bonus += 0

# bounce effect
#Given for HAMR
base_bounce_chance = 0.73    # changing to observed -2, theory: 75
bounce_chance = base_bounce_chance
bounce_hits = 4

# Mods:
bounce_dmg_bonus = 0.06 + 0.048
bounce_crit_dmg_bonus = 0.25 + 0.20
bounce_dmg_bonus += 1.25/3  # every 3rd shot + 125% bouce dmg (every 7th, but HAMR's sharp blade triggers 2 bounces)
                            # targeted strike was 8.5% worse (42863.60/46840.11)
bounce_weakspot_bonus = 0
bounce_crit_rate_bonus = 0 + 0.1
bounce_chance += base_bounce_chance*0.048


# cradle:
weapon_dmg_bonus += 0.15    # when using snipers
weapon_dmg_bonus += 0.15 * (4/9)    # affects only first 4 bullets      
bounce_dmg_bonus += 0.25 * (5/6.75)  # buff triggers after first bounce trigger (5.75/6.75)
weakspot_dmg_bonus += 0.2   # targets marked with bullseye
bounce_dmg_bonus += 0.05*(5/2)  # max 5,  triggers every time bounce triggers. (skips first one, hence 5.75/2)

# print(f"The crit damage is: {crit_dmg*100:.2f}%\ncrit rate is: {crit_rate*100:.2f}")

flag_weakspot = 1

# MAIN PHY DMG DONE, INCLUDING BOUNCE:


def get_bounce_damage(bounce_chance, bounce_hits, bounce_dmg_bonus, bounce_crit_rate_bonus, bounce_crit_dmg_bonus, bounce_weakspot_bonus, base_, attack_, weaponn_dmg_, weakspot_dmg_bonus,crit_rate, crit_damage, enemy_dmg_bonus, bullet_dmg_bonus, vulnerability, weakspot = False):
    if weakspot:
        damage = base_*(1+attack_)*(1+weaponn_dmg_+bullet_dmg_bonus)*(1+crit_rate*crit_damage)*(1+weakspot_dmg_bonus)*(1 + enemy_dmg_bonus)*(1 + vulnerability)
    else:
        damage = base_*(1+attack_)*(1+weaponn_dmg_+bullet_dmg_bonus)*(1+crit_rate*crit_damage)*(1 + enemy_dmg_bonus)*(1 + vulnerability)

    one_bounce = 0.4*base_*(1+attack_)*(1+weaponn_dmg_+bullet_dmg_bonus)*(1+(crit_rate + bounce_crit_rate_bonus)*(crit_damage+bounce_crit_dmg_bonus))*(1 + enemy_dmg_bonus)*(1+bounce_dmg_bonus)*(1 + vulnerability)
    bounce_hits_per_shot = (bounce_chance)*bounce_hits
    one_bounce_weakspot_avg = one_bounce*(0.52 + 0.48*(1+ weakspot_dmg_bonus + bounce_weakspot_bonus))    # obv data is 52, 48      #theory: 50, 50
    avg_bounce = bounce_hits_per_shot*one_bounce_weakspot_avg

    Total_hit_dmg = damage + avg_bounce
    
    return Total_hit_dmg


#calc
Total_per_hit = get_bounce_damage(bounce_chance, bounce_hits, bounce_dmg_bonus, bounce_crit_rate_bonus, bounce_crit_dmg_bonus, bounce_weakspot_bonus, weapon_base_atk, attack, weapon_dmg_bonus, weakspot_dmg_bonus, crit_rate, crit_dmg, enemy_dmg_bonus, bullet_dmg_bonus, vulnerability, flag_weakspot)

# full done.




# testing
# database of manual per hit tests:
result = ((600)*1000/1 - 15000) / 9 # Non cradle ((250 + 285 + 369 + 385 + 299 + 341 + 267 + 356)*1000/8 - 14000) / 9      # ((348 + 293 + 457 + 492 + 421 + 450 + 358 + 562 + 450 + 366 + 355)*1000/11 - 15000) / 9
print(f"\nPer shot dmg is: {Total_per_hit:.2f}\t\tManual: {result:.2f}\nTheory's Match ratio:   {Total_per_hit/result*100:.0f}%\n")

# new damage:

new_wk = weakspot_dmg_bonus + 0.09
new_wp = weapon_dmg_bonus + 0.06
new_crit_dmg = crit_dmg + 0.15
new_crit_rate = crit_rate + 0.05
new_bounce_dmg = bounce_dmg_bonus + 0.06
new_bounce_crit = bounce_crit_dmg_bonus + 0.25
new_enemy_dmg_bonus = enemy_dmg_bonus + 0.06
new_bounce_wk = bounce_weakspot_bonus + 0.15
new_bounce_trigger_chance = bounce_chance + 0.06*base_bounce_chance

wk = get_bounce_damage(bounce_chance, bounce_hits, bounce_dmg_bonus, bounce_crit_rate_bonus, bounce_crit_dmg_bonus, bounce_weakspot_bonus,  weapon_base_atk, attack, weapon_dmg_bonus, new_wk, crit_rate, crit_dmg, enemy_dmg_bonus, bullet_dmg_bonus, vulnerability, flag_weakspot)
wp = get_bounce_damage(bounce_chance, bounce_hits, bounce_dmg_bonus, bounce_crit_rate_bonus, bounce_crit_dmg_bonus, bounce_weakspot_bonus, weapon_base_atk, attack, new_wp, weakspot_dmg_bonus, crit_rate, crit_dmg, enemy_dmg_bonus, bullet_dmg_bonus, vulnerability, flag_weakspot)
cd = get_bounce_damage(bounce_chance, bounce_hits, bounce_dmg_bonus, bounce_crit_rate_bonus, bounce_crit_dmg_bonus, bounce_weakspot_bonus, weapon_base_atk, attack, weapon_dmg_bonus, weakspot_dmg_bonus, crit_rate, new_crit_dmg, enemy_dmg_bonus, bullet_dmg_bonus, vulnerability, flag_weakspot)
cr = get_bounce_damage(bounce_chance, bounce_hits, bounce_dmg_bonus, bounce_crit_rate_bonus, bounce_crit_dmg_bonus, bounce_weakspot_bonus, weapon_base_atk, attack, weapon_dmg_bonus, weakspot_dmg_bonus, new_crit_rate, crit_dmg, enemy_dmg_bonus, bullet_dmg_bonus, vulnerability, flag_weakspot)
bounce = get_bounce_damage(bounce_chance, bounce_hits, new_bounce_dmg, bounce_crit_rate_bonus, bounce_crit_dmg_bonus, bounce_weakspot_bonus, weapon_base_atk, attack, weapon_dmg_bonus, weakspot_dmg_bonus, crit_rate, crit_dmg, enemy_dmg_bonus, bullet_dmg_bonus, vulnerability, flag_weakspot)
bounce_crit = get_bounce_damage(bounce_chance, bounce_hits, bounce_dmg_bonus, bounce_crit_rate_bonus, new_bounce_crit, bounce_weakspot_bonus, weapon_base_atk, attack, weapon_dmg_bonus, weakspot_dmg_bonus, crit_rate, crit_dmg, enemy_dmg_bonus, bullet_dmg_bonus, vulnerability, flag_weakspot)
bounce_wk = get_bounce_damage(bounce_chance, bounce_hits, bounce_dmg_bonus, bounce_crit_rate_bonus, bounce_crit_dmg_bonus, new_bounce_wk, weapon_base_atk, attack, weapon_dmg_bonus, weakspot_dmg_bonus, crit_rate, crit_dmg, enemy_dmg_bonus, bullet_dmg_bonus, vulnerability, flag_weakspot)
bounce_chance_1 = get_bounce_damage(new_bounce_trigger_chance, bounce_hits, bounce_dmg_bonus, bounce_crit_rate_bonus, bounce_crit_dmg_bonus, bounce_weakspot_bonus, weapon_base_atk, attack, weapon_dmg_bonus, weakspot_dmg_bonus, crit_rate, crit_dmg, enemy_dmg_bonus, bullet_dmg_bonus, vulnerability, flag_weakspot)
enemy_dmg = get_bounce_damage(bounce_chance, bounce_hits, bounce_dmg_bonus, bounce_crit_rate_bonus, bounce_crit_dmg_bonus, bounce_weakspot_bonus, weapon_base_atk, attack, weapon_dmg_bonus, weakspot_dmg_bonus, crit_rate, crit_dmg, new_enemy_dmg_bonus, bullet_dmg_bonus, vulnerability, flag_weakspot)

dict_new_dmgs = {"wk\t":wk, "wp\t": wp, "cd\t":cd, "cr\t": cr, "bounce": bounce, "bounce crit": bounce_crit, "bounce_wk": bounce_wk, "bounce_chance_1": bounce_chance_1, "enemy_dmg": enemy_dmg}

# sorting from google, at desending order (too lazy to this on my own, saving 15 min):
sorted_items_desc = sorted(dict_new_dmgs.items(), key=lambda item: item[1], reverse=True)
sorted_dict_desc = dict(sorted_items_desc)

i = 0
for key in sorted_dict_desc:
    i+=1
    damage = sorted_dict_desc[key]
    print(f"Number {i}: {key}\tRatio Increase: {damage/Total_per_hit*100-100:.2f}%\tdamage: {damage:.0f}")

print(f"wk: {new_wk*100:.0f}%\twp: {new_wp*100:.0f}%\t\tcrit: {new_crit_dmg*100:.0f}%\tcr: {new_crit_rate*100:.0f}%\t\tbounce: {new_bounce_dmg*100:.0f}%\tbounce crit: {new_bounce_crit*100:.0f}%\tenemy: {new_enemy_dmg_bonus*100:.0f}%")