class Horse:

    def __init__(self, line):
        words = line.split()
        self.rate = int(words[3])
        self.run_time = int(words[6])
        self.rest_time = int(words[13])

        self.km = 0
        self.resting = False
        self.current_rest = self.rest_time
        self.current_run = self.run_time
        self.points = 0

    def __str__(self):
        return "(rate " + str(self.rate) + " run_time " + str(self.run_time) + " rest_time " + str(self.rest_time) + ")"

    def run():
        if resting:
            current_rest -= 1
            if current_rest == 0:
                resting = False
                current_rest = rest_time
        else:
            km += rate
            current_run -= 1
            if current_run == 0:
                resting = True
                current_run = run_time

    def award():
        points += 1


def min_dist(horses):
    """
    Find minimal distance, e.g. minimal horse.km.
    """
    min = None
    for x in horses:
        if min == None or min > x.km: min = x.km
    return min


def award(horses, awarded_dist):
    """
    All horses who ran for awarded distance get one point.
    """
    for x in horses:
        if x.km == awarded_dist:
            x.points += 1


horses = []
for line in open("input14.txt"):
    horses.append(Horse(line))

for t in range(2503):
    map(run, horses)
    award(horses, min_dist(horses)

# find the horse with max points
max=None
for h in horses:
    if max == None or max < h.points:
          max=h.points

print(max)
