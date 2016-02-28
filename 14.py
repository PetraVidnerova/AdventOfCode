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

    def run(self):
        if self.resting:
            self.current_rest -= 1
            if self.current_rest == 0:
                self.resting = False
                self.current_rest = self.rest_time
        else:
            self.km += self.rate
            self.current_run -= 1
            if self.current_run == 0:
                self.resting = True
                self.current_run = self.run_time

    def award(self):
        self.points += 1


def max_dist(horses):
    """
    Find minimal distance, e.g. minimal horse.km. 
    """
    max = None
    for x in horses:
        if max == None or max < x.km:
            max = x.km
    return max


def award(horses, awarded_dist):
    """
    All horses who ran for awarded distance get one point. 
    """
    for x in horses:
        if x.km == awarded_dist:
            x.award()


horses = []
for line in open("input14.txt"):
    horses.append(Horse(line))

for t in range(2503):
    for x in horses:
        x.run()
    award(horses, max_dist(horses))

# find the horse with max points
max = None
for h in horses:
    if max == None or max < h.points:
        max = h.points

print(max)
