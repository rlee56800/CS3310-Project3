'''
Task #2 – 0/1 Knapsack Problem                                                  (65 Points)

Use the Best-First  search with Branch-and-Bound algorithm to solve 0/1 knapsack problem.

INPUT:
    Positive integer W (knapsack capacity) and an input.txt file that contains the weights
    and profits of n objects. (The first line of this file should contain profits and the
    second line should include respective weights of n objects; use colon or space to
    separate values.)

OUTPUT:
    Visited node, profit, weight, bound, maximum profit and updated Priority queue at each step.
    An integer maximum profit that is the sum of the profits of an optimal set and objects of
    that optimal set.

Note: you can use the example explained in the class as your reference.
'''
class Node:
    def __init__(self, l, p, w):
        self.level = l
        self.profit = p
        self.weight = w
        self.bound = None

    def toString():
        print("Node profit: " + profit)
        print("Node weight: " + weight)


def bound(u, n, p, w, W):
    if(u.weight >= W):
        return 0
    if(u.weight >= W):
        return 0 # return 0 for bound if node is unpromising
    else:
        result = u.profit
        j = u.level + 1
        totweight = u.weight
        while(j <= n) and (totweight + w[j] <= W):
            totweight += w[j] # Grab as many items as possible
            result += p[j]
            j += 1
    k = j # use k for consistency with formula in text
    if k <= n:
        result += (W - totweight) * p[k] / w[k] # or //?
        # grab fraction of kth item
    return result


def knapsack3(n, p, w, W, maxProfit):
    pq = [] # initialize pq to be empty
    v = Node(0, 0, 0) # initialize v to the root
    maxProfit = 0
    v.bound = bound(v)
    pq.append(v)
    while not pq: # while pq is not empty
        pq.pop(v) # remove node with the best bound (call sort???)
        pq.sort(key=lambda x: x.bound, reverse=True) # does True mean increasing

        if v.bound > maxProfit: # check if node is stil promising
            u = Node(v.level + 1, v.weight + w[u.level], v.profit + p[u.level])
                # set u to child that includes next item
            if(u.weight <= W) and (u.profit > maxProfit):
                maxProfit = u.profit
                u.bound = bound(u) # or is this outside the if
            if u.bound > maxProfit:
                pq.append(u)
                # set u to child that does not include next item (placement...)
                u.weight = v.weight # inside if?
                u.profit = v.profit # ^
                u.bound = bound(u) # ^
                if u.bound > maxProfit: # ^
                    pq.append(u)





#capacity = int(input("Please enter value for capacity: "))
capacity = 20#7 # testing
total = 0
profit = []
weight = []
arr = []
usedProfit = []
usedWeight = []

with open('input.txt') as f:
    items = int(next(f)) # first number is amount of items
    for x in next(f).split(): # first row is profit
        profit.append(int(x))
    for x in next(f).split(): # second row is weights
        weight.append(int(x))
#print(profit)
#print(weight)

'''
capacity = 7
total = 0
items = 4
profit = [1,4,5,7]
weight = [1,3,4,5]
arr = []'''

for i in range(items + 1):
    arr1 = []
    for j in range(capacity+1):
        arr1.append(0)
    arr.append(arr1)


#fill()

#for i in range(len(arr)):
#    print(arr[i])

print("Max Profit: " + str(arr[items][capacity]))
print("Items used (profit, then weight):")
print(usedProfit)
print(usedWeight)