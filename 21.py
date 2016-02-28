import itertools


class Player:

    def __init__(self, hitpoints, damage, armor):
        self.hitpoints = hitpoints
        self.damage = damage
        self.armor = armor

    def hit(self, damage):
        self.hitpoints -= max(damage, 1) - self.armor

    def addEquipment(self, equipment):
        self.damage = 0
        self.armor = 0
        for item in equipment:
            self.damage += item[2]
            self.armor += item[3]

    def printme(self):
        print("Hitpoints:", self.hitpoints, ", Damage:",
              self.damage, " Armor:", self.armor)


me = Player(100, 0, 0)
enemy = Player(109, 8, 2)

# 'a',0,0,0  stands for no armer
weapons = [('w', 8, 4, 0), ('w', 10, 5, 0), ('w', 25, 6, 0),
           ('w', 40, 7, 0), ('w', 74, 8, 0)]
armor = [('a', 0, 0, 0), ('a', 13, 0, 1), ('a', 31, 0, 2),
         ('a', 53, 0, 3), ('a', 75, 0, 4), ('a', 102, 0, 5)]
rings = [('r', 25, 1, 0),  ('r', 50, 2, 0), ('r', 100, 3, 0),
         ('r', 20, 0, 1), ('r', 40, 0, 2), ('r', 80, 0, 3)]


def delete(eqlist, type):
    # delete from eqlist all items of type 'type'
    # return the cost of deleted items
    cost = 0
    for item in eqlist:
        if item[0] == type:
            cost += item[1]
            eqlist.remove(item)
    return cost


def fight(me, enemy):
    # return True if me wins
    turn = 0
    while me.hitpoints > 0 and enemy.hitpoints > 0:
        if turn % 2 == 0:
            enemy.hit(me.damage)
        else:
            me.hit(enemy.damage)
        turn += 1
    if me.hitpoints > 0:
        return True
    else:
        return False


equipment = []
cost = 0
wincosts = []
for w in weapons:
    # do for each weapon (only one weapon aload)
    cost -= delete(equipment, 'w')
    equipment.append(w)
    cost += w[1]
    for i in [0, 1]:
        # do for zero or one armor
        cost -= delete(equipment, 'a')
        for a in armor:
            cost -= delete(equipment, 'a')
            equipment.append(a)
            cost += a[1]
            for j in range(3):
                # do for 0 to 2 rings
                for ringset in itertools.combinations(rings, j):
                    cost -= delete(equipment, 'r')
                    for r in ringset:
                        equipment.append(r)
                        cost += r[1]
                    # now equipment is ready
                    print(equipment, cost)
                    me.addEquipment(equipment)
                    me.hitpoints = 100
                    enemy.hitpoints = 109
                    me.printme()
                    enemy.printme()
                    if fight(me, enemy):
                        print("WIN")
                        wincosts.append(cost)
                    else:
                        print(":(")


print(wincosts)
print(min(wincosts))
