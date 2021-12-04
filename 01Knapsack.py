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

def printPQ(pq):
    pqueue = []
    for i in pq:
        pqueue.append(i.level + 1)
    
    print("Priority queue:", pqueue)

class Node:
    def __init__(self, l, p, w):
        self.level = l
        self.profit = p
        self.weight = w

    def printStr(self, mp, pq):
        print("Node level: " + str(self.level + 1))
        print("Node profit: $" + str(self.profit))
        print("Node weight: " + str(self.weight))
        print("Node bound: $" + str(self.bound))
        print("Max profit: $" + str(mp))
        printPQ(pq) # weird because it used to be separate
        print()

def bound(u):
    if u.weight >= W:
        return 0 # return 0 for bound if node is unpromising
    else:
        result = u.profit
        j = u.level + 1
        #print("j = " + str(j))
        totweight = u.weight
        while(j <= n-1) and (totweight + w[j] <= W):
            totweight += w[j] # Grab as many items as possible
            result += p[j]
            j += 1
    k = j # use k for consistency with formula in text
    if k <= (n - 1):
        result += (W - totweight) * p[k] / w[k] # grab fraction of kth item
    return result


def knapsack3(n, p, w, W):
    pq = [] # initialize pq to be empty
    v = Node(-1, 0, 0) # initialize v to the root
    maxProfit = 0
    v.bound = bound(v)
    #counter = 0

    pq.append(v)
    v.printStr(maxProfit, pq)
    pq.sort(key=lambda x: x.bound, reverse=True) # sorts priority queue in decreasing order (highest bound first)
    
    while len(pq): # while pq is not empty
        #print(counter)
        #counter += 1
        #printPQ(pq)
        v = pq.pop() # remove node with the best bound
        
        if v.bound > maxProfit: # check if node is stil promising
            
            # left child
            u = Node(0, 0, 0)
            u.level = v.level + 1
            u.weight = v.weight + w[u.level]
            u.profit = v.profit + p[u.level]
            if (u.weight <= W) and (u.profit > maxProfit):
                maxProfit = u.profit
            u.bound = bound(u)
            if u.bound > maxProfit:
                pq.append(u)
                u.printStr(maxProfit, pq)
                pq.sort(key=lambda x: x.bound, reverse=True) # sorts priority queue in decreasing order (highest bound first)
             
            # right child
            u2 = Node(u.level, v.profit, v.weight)
            u2.bound = bound(u2)
            if u2.bound > maxProfit:
                pq.append(u2)
                pq.sort(key=lambda x: x.bound, reverse=True) # sorts priority queue in decreasing order (highest bound first)
#            u.weight = v.weight
#            u.profit = v.profit
#            u.bound = bound(u) 
#            if u.bound > maxProfit:
#                pq.append(u)
#                u.printStr(maxProfit, pq)
    
    return maxProfit





W = 16 # capacity
#total = 0
p = [] # profit
w = [] # weight
nn = [] # node number
maxProfit = 0
#profitperunit = [] # take a wild guess

with open('01Knapsack-input.txt') as f:
    n = int(next(f)) # first number is amount of items
    for x in next(f).split(): # first row is profit
        p.append(int(x))
        nn.append(0)
    for x in next(f).split(): # second row is weights
        w.append(int(x))

#print(p)
#print(w)

maxProfit = knapsack3(len(p), p, w, W)
print("maxprofit = ", str(maxProfit))

'''
capacity = 7
total = 0
items = 4
profit = [1,4,5,7]
weight = [1,3,4,5]
arr = []

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
print(usedWeight)'''