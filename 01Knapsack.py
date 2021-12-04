'''
Task #2 – 0/1 Knapsack Problem                                                  (65 Points)

Use the Best-First search with Branch-and-Bound algorithm to solve 0/1 knapsack problem.

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
counter = [1] # for counting nodes
def printPQ(pqu):
    pqueue = [] # so we can print an array of nodes
    for i in pqu:
        pqueue2 = []
        pqueue2.append(i.level + 1) # level is 1 behind "actual" node level
        pqueue2.append(i.number)
        pqueue.append(pqueue2)
    
    print("Priority queue:", pqueue)

def addNew(node):
    i = 0
    while i < len(pq):
        if pq[i].nbound > node.nbound:
            break
        i += 1
    pq.insert(i, node)


class Node:
    def __init__(self, l, p, w):
        self.level = l
        self.profit = p
        self.weight = w
        # nbound defined elsewhere
        
    def printStr(self, mp, pq):
        # account for which node number this is
        # (counts how many nodes on the level we've visited)
        nn[self.level] += 1
        self.number = nn[self.level]

        # count how many nodes we've visited
        print(counter[0])
        counter[0] += 1

        print("Current node: (" + str(self.level + 1) + ", " + str(self.number) + ")")
        print("Node profit: $" + str(self.profit))
        print("Node weight: " + str(self.weight))
        print("Node bound: $" + str(self.nbound))
        print("Max profit: $" + str(mp))

        printPQ(pq) # weird because it used to be separate
        print()

def bound(u):
    if u.weight >= W:
        return 0 # return 0 for bound if node is unpromising
    else:
        result = u.profit
        j = u.level + 1
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
    v = Node(-1, 0, 0) # initialize v to the root (-1 to make array traversal easier)
    maxProfit = 0
    v.nbound = bound(v)

    addNew(v)
    v.printStr(maxProfit, pq)
    
    while len(pq): # while pq is not empty
        v = pq.pop() # remove node with the best bound
        
        if v.nbound > maxProfit: # check if node is stil promising
            
            # left child
            #print("left")
            u = Node(0, 0, 0)
            u.level = v.level + 1
            u.weight = v.weight + w[u.level]
            u.profit = v.profit + p[u.level]
            if (u.weight <= W) and (u.profit > maxProfit):
                maxProfit = u.profit
            u.nbound = bound(u)
            u.printStr(maxProfit, pq)
            if u.nbound > maxProfit:
                addNew(u)
             
            # right child
            #print("right")
            u2 = Node(u.level, v.profit, v.weight)
            u2.nbound = bound(u2)
            u2.printStr(maxProfit, pq)
            if u2.nbound > maxProfit:
                addNew(u2)
    
    return maxProfit





W = 16 # capacity
p = [] # profit
w = [] # weight
nn = [] # node number
maxProfit = 0
pq = [] # initialize pq to be empty

with open('01Knapsack-input.txt') as f:
    for x in next(f).split(): # first row is profit
        p.append(int(x))
        nn.append(0)
    for x in next(f).split(): # second row is weights
        w.append(int(x))
    n = len(p)
nn[-1] = -1
#print(p)
#print(w)

maxProfit = knapsack3(len(p), p, w, W)
print("Max profit: $", str(maxProfit))