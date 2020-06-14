
class Node:

    def __init__(self, name):
        self.name      = name
        self.neighbors = {}
        self.parent    = None
        self.glob      = 1000000
        self.local     = 1000000

class Astar:

    def __init__(self, start, end):
        start.local      = 0
        self.start       = start
        self.end         = end
        self.openSet     = [start]
        self.closedSet   = []

    def miniCostToEnd(self):
        print([i.name for i in sorted(self.openSet, key=lambda node: node.local)])
        return sorted(self.openSet, key=lambda node: node.local)[0] #check most be node.glob

    @property
    def run(self):
        while len(self.openSet) > 0:
            current = self.miniCostToEnd()

            print("visiting :", current.name)

            if current == self.end:

                prev = self.end
                self.path = [prev]
                while prev.parent != None:
                    self.path.insert(0, prev.parent)
                    prev = prev.parent
                break

            self.openSet.remove(current)
            self.closedSet.append(current)

            for neighbor, cost in current.neighbors.items():

                if current.local + cost < neighbor.local:
                    neighbor.local = current.local + cost
                    neighbor.parent = current
                    if neighbor not in self.openSet:
                        self.openSet.append(neighbor)

        return {i.name: i.local for i in self.path}

# create our nodes
a, b, e, f, c, d = Node("A"), Node("B"), Node("E"), Node("F"), Node("C"), Node("D")

# add neighbors path cost for each node
a.neighbors = {b:2, e:1, f:3     }
b.neighbors = {a:2, c:1          }
e.neighbors = {a:1, c:1, f:5, d:5}
f.neighbors = {a:3, e:1, d:1     }
c.neighbors = {b:1, e:1, d:2     }
d.neighbors = {c:2, e:5, f:1     }

obj = Astar(a, d)
print(obj.run) # result is {A, E, F, D}

