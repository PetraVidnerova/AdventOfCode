from random import randint
import itertools
import queue
import copy


class Spell:

    def __init__(self, name, cost=0, turns=0, damage=0, armor=0, mana=0, heal=0):
        self.name = name
        self.cost = cost
        self.turns = turns
        self.damage = damage
        self.armor = armor
        self.mana = mana
        self.heal = heal

    def toString(self):
        return self.name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

spells = [Spell(name="Missile", cost=53, damage=4),  Spell(name="Drain", cost=73, damage=2, heal=2),
          Spell(name="Shield", cost=113, turns=6, armor=7),  Spell(
              name="Poison", cost=173, turns=6, damage=3),
          Spell(name="Recharge", cost=229, turns=5, mana=101)]


class Player:

    def __init__(self, name, hits, mana=0, damage=0, armor=0):
        self.name = name
        self.hits = hits
        self.mana = mana
        self.damage = damage
        self.armor = armor

    def toString(self):
        return self.name + " hits:" + str(self.hits) + " mana:" + str(self.mana) + " damage:" + str(self.damage) + " armor:" + str(self.armor)


class Game:

    def __init__(self, me, boss):
        self.me = me
        self.boss = boss

        self.effects = []
        self.rules = []
        self.mana_spent = 0

    def __lt__(self, rhs):
        return self.mana_spent < rhs.mana_spent

    def __gt__(self, rhs):
        return self.mana_spent > rhs.mana_spent

    def __le__(self, rhs):
        return self.mana_spent <= rhs.mana_spent

    def __ge__(self, rhs):
        return self.mana_spent >= rhs.mana_spent


def doEffects(g):
    game = copy.deepcopy(g)
    for e in game.effects:
        game.boss.hits -= e.damage
        game.me.mana += e.mana
        e.turns -= 1
        if (e.turns == 0):
            game.me.armor -= e.armor
    game.effects = [x for x in game.effects if not x.turns == 0]
    return game


def next_turn(game, spell):
    # One turn of player and one turn of boss.
    #    game = copy.deepcopy(g)
    # very first  (only part2)
    game.me.hits -= 1
    if game.me.hits <= 0:
        return None  # I lose
    # first do effects
    game = doEffects(game)
    if game.boss.hits <= 0:
        return game  # I won

    #  cast spell
    game.me.mana -= spell.cost
    game.mana_spent += spell.cost
    game.rules.append(spell)
    if game.me.mana < 0:
        #        print("NO money",game.rules,spell)
        return None  # not allowed

    if spell.turns == 0:  # it is instant spell
        game.boss.hits -= spell.damage
        game.me.armor += spell.armor
        game.me.hits += spell.heal
        if game.boss.hits <= 0:
            return game  # I won
    else:
        # it is an effect
        for e in game.effects:
            if spell.name == e.name:
                #                print("NO effects",game.rules,spell)
                return None
        game.me.armor += spell.armor
        game.effects.append(spell)

    # BOSS TURN
    # first do effects
    game = doEffects(game)
    if game.boss.hits <= 0:
        return game  # I won
    # hit me
    game.me.hits -= max(1, game.boss.damage - game.me.armor)
    if game.me.hits <= 0:
     #       print("NO lifes",game.rules,spell)
        return None  # boss won
    return game  # nobody won


def randomGame(game):
    global spells
    while True:
        rand = randint(0, len(spells) - 1)
        game = next_turn(game, spells[rand])
        if not game or game.me.hits <= 0:
            return None
        elif game.boss.hits <= 0:
            return game
        else:
            continue

#g = Game(Player("me",10, 250), Player("boss",14,damage=8) )
min = None
while (True):
    g = Game(Player("me", 50, 500), Player("boss", 58, damage=9))
    g = randomGame(g)
    if g:
        if min == None or g.mana_spent < min:
            min = g.mana_spent
        print(min, g.mana_spent, g.rules)


quit()
"""
g = next_turn(g, Spell(name="Recharge", cost=229, turns=5, mana=101))
print( g.boss.hits, g.me.hits, g.mana_spent, g.rules)
g = next_turn(g, Spell(name="Shield", cost=113, turns=6, armor=7))
print( g.boss.hits, g.me.hits, g.mana_spent, g.rules)
g = next_turn(g, Spell(name="Drain", cost=73, damage=2, heal=2))
print( g.boss.hits, g.me.hits, g.mana_spent, g.rules)
g = next_turn(g, Spell(name="Poison", cost=173, turns=6, damage=3))
print( g.boss.hits, g.me.hits, g.mana_spent, g.rules)
g = next_turn(g, Spell(name="Missile", cost=53, damage=4))
print( g.boss.hits, g.me.hits, g.mana_spent, g.rules)
quit() 
"""

# Games with least number of boss's hits go first.
q = queue.PriorityQueue()
q.put((g.mana_spent, g.boss.hits,  g))

while True:
    if q.empty():
        print("empty queue")
        break
    hits, manaspent, g = q.get()
#    print( g.boss.hits, g.mana_spent, g.rules)
    if (g.boss.hits <= 0):
        break
    for spell in spells:
        nextg = next_turn(g, spell)
        if nextg:
            q.put((nextg.mana_spent, nextg.mana_spent, nextg))
