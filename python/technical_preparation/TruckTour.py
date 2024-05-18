"""
Suppose there is a circle. There are N petrol pumps on that circle.
 Petrol pumps are numbered 0 to (N-1) (both inclusive). You have
two pieces of information corresponding to each of the petrol pump:
(1) the amount of petrol that particular petrol pump will give, and (2)
the distance from that petrol pump to the next petrol pump.
Initially, you have a tank of infinite capacity carrying no petrol. You can
start the tour at any of the petrol pumps. Calculate the first point from
where the truck will be able to complete the circle. Consider that the
truck

"""


def truckTour(petrolpumps):
    sortedd = list(petrolpumps)
    sortedd.sort(reverse=True)
    column_val = [x[0] for x in petrolpumps]

    for i in range(len(petrolpumps)):
        solved = 0
        index = column_val.index(sortedd[i][0])

        pump = 0
        for j in range(index, len(petrolpumps)):

            pump += petrolpumps[j][0]
            pump -= petrolpumps[j][1]
            if pump < 1:
                solved = 0
                break

            elif j == len(petrolpumps) - 1:
                solved = 1

        for e in range(0, index):
            pump += e[0]
            pump -= e[1]
            if pump < 1:
                solved = 0
                break
            elif j == len(petrolpumps) - 1:
                return index


if __name__ == "__main__":

    n = int(input().strip())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)
