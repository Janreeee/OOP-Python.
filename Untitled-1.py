class hero():
    def __init__(self,name,role,dmg_type,health,auto_atk_dmg):
        self.name = name
        self.role = role
        self.dmg_type = dmg_type
        self.health = health
        self.auto_atk_dmg = auto_atk_dmg
    
    def describe(self):
        return f"{self.name} is a {self.role} with a {self.dmg_type} power"

hero_mm1 = hero("Claude", "Marksman", "Attack damage", 100, 30)
hero_fighter1 = hero("Freya", "Fighter", "Attack damage", 100 , 30)
hero_mage1 = hero("Valentina", "Mage", "Ability " ,100, 10)
hero_jungler1 = hero("Ling", "Jungler", "Attack Damage", 100 , 50)
hero_roamer1 = hero("Floryn", "Support", "Hybrid" ,100, 10)

print(f'''
{hero_mm1.name}
{hero_mm1.role}
{hero_mm1.dmg_type}
{hero_mm1.health} HP
{hero_mm1.auto_atk_dmg} basic attact damage
{hero_mm1.describe()} 

{hero_fighter1.name}
{hero_fighter1.role}
{hero_fighter1.dmg_type}
{hero_fighter1.health} HP
{hero_fighter1.auto_atk_dmg} basic attact damage
{hero_fighter1.describe()}


{hero_mage1.name}
{hero_mage1.role}
{hero_mage1.dmg_type}
{hero_mage1.health} HP
{hero_mage1.auto_atk_dmg} basic attact damage
{hero_mage1.describe()}


{hero_jungler1.name}
{hero_jungler1.role}
{hero_jungler1.dmg_type}
{hero_jungler1.health} HP
{hero_jungler1.auto_atk_dmg} basic attact damage
{hero_jungler1.describe()}


{hero_roamer1.name}
{hero_roamer1.role}
{hero_roamer1.dmg_type}
{hero_roamer1.health} HP
{hero_roamer1.auto_atk_dmg} basic attact damage
{hero_roamer1.describe()}
''')