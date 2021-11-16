"""
Chapitre 11.1

Classes pour représenter un personnage.
"""


import random

import utils


class Weapon:
	"""
	Une arme dans le jeu.

	:param name: Le nom de l'arme
	:param power: Le niveau d'attaque
	:param min_level: Le niveau minimal pour l'utiliser
	"""
	UNARMED_POWER = 20

	def __init__(self, name, power, minimum_level):
		self.name = name
		self.power = power
		self.minimum_level = minimum_level

	def sufficient_level(self, level):
		return level >= self.minimum_level

	def make_unarmed():
		return Weapon("Unarmed", 20, 0)


class Character:
	"""
	Un personnage dans le jeu

	:param name: Le nom du personnage
	:param max_hp: HP maximum
	:param attack: Le niveau d'attaque du personnage
	:param defense: Le niveau de défense du personnage
	:param level: Le niveau d'expérience du personnage
	"""

	def __init__(self, name, max_hp, attack, defense, level, weapon=None):
		self.name = name
		self.max_hp = max_hp
		self.attack = attack
		self.defense = defense
		self.level = level
		if(weapon is None):
			self.weapon = Weapon.make_unarmed()
		elif(not weapon.sufficient_level(level)):
			raise ValueError
		else:
			self.weapon = weapon
		self.hp = max_hp
	
	def compute_damage(self, defender, crit_modifier):
		modifier = (random.random() * 15 + 85)/100 * crit_modifier
		damage = ( (2/5 * self.level + 2) * self.weapon.power * 
				self.attack / defender.defense /50 + 2 ) * modifier
		defender.hp -= damage
		if defender.hp < 0:
			defender.hp = 0
		return damage

	def is_dead(self):
		self.hp = utils.clamp(self.hp, 0, self.max_hp)
		return self.hp <= 0


def deal_damage(attacker, defender):
	# TODO: Calculer dégâts
	crit_chance = 1/6
	crit = random.random() <= crit_chance
	crit_modifier = 2 if crit else 1
	
	damage = attacker.compute_damage(defender, crit_modifier)

	print(f"{attacker.name} used {attacker.weapon.name}")
	if crit:
		print("  Critical hit!")
	print(f"  {defender.name} took {damage} dmg")

def run_battle(c1, c2):
	# TODO: Initialiser attaquant/défendeur, tour, etc.
	attacker = c1
	defender = c2
	turn = 0
	print(f"{attacker.name} starts a battle with {defender.name}!")
	while True:
		turn+=1
		# TODO: Appliquer l'attaque
		deal_damage(attacker, defender)
		# TODO: Si le défendeur est mort
		if(defender.is_dead()):
			print(f"{defender.name } is sleeping with the fishes.")
			break
		# Échanger attaquant/défendeur
		attacker, defender = defender, attacker
	# TODO: Retourner nombre de tours effectués
	return turn