
from math import floor
from collections import namedtuple
import warnings
from matplotlib import pyplot as plt

Item = namedtuple("Item", ['index', 'value', 'weight', 'ValueDensity'])

class Node():
    def __init__(self, Taken, Parent):
        self.Taken = Taken
        self.Parent = Parent

        if self.Parent != None:
            if self.Taken:
                self.TakenList = self.Parent.TakenList.copy()
                self.TakenList.append(True)
                self.CalculateIndex()
                self.CalculateCapacity()
                self.CalculateValue()
                self.CalculateUpperBound()
            else:
                self.TakenList = self.Parent.TakenList.copy()
                self.TakenList.append(False)
                self.CalculateIndex()
                self.Capacity = self.Parent.Capacity
                self.Value = self.Parent.Value
                self.CalculateUpperBound()
        else:
            self.TakenList = []
            self.Index = -1
            self.Capacity = 0
            self.Value = 0
            self.UpperBound = calculate_relaxed_integer_upperbound(items.copy(),capacity)

        self.Left = None
        self.Right = None

    # def __del__(self):
    #     print('Deleted')

    def CalculateCapacity(self):
        tempCapacity = 0
        for index, item in enumerate(self.TakenList):
            if item:
                tempCapacity += items[index].weight
        self.Capacity = tempCapacity

        # tempCapacity = 0
        # tempNode = self
        # while tempNode.Index != -1:
        #     if tempNode.Taken:
        #         tempCapacity += items[tempNode.Index].weight
        #     tempNode = tempNode.Parent
        # self.Capacity = tempCapacity

    def CalculateValue(self):
        tempValue = 0
        for index, item in enumerate(self.TakenList):
            if item:
                tempValue += items[index].value
        self.Value = tempValue
        # tempValue = 0
        # tempNode = self
        # while tempNode.Index != -1:
        #     if tempNode.Taken:
        #         tempValue += items[tempNode.Index].value
        #     tempNode = tempNode.Parent
        # self.Value = tempValue

    def CalculateUpperBound(self):
        if self.Taken:
            self.UpperBound = self.Parent.UpperBound
        else:
            tempUpperBound = 0
            tempItems = items.copy()
            for index, val in reversed(list(enumerate(self.TakenList))):
                if not val:
                    tempItems.pop(index)
                    continue
                continue

#
            # tempCapacity = 0
            # tempNode = self
            # tempItems = items.copy()
            # while tempNode.Index != -1:
            #     if not tempNode.Taken:
            #         tempItems.pop(tempNode.Index)
            #     tempNode = tempNode.Parent

            self.UpperBound = calculate_relaxed_integer_upperbound(tempItems, capacity)

    def CalculateIndex(self):
        self.Index = self.Parent.Index + 1

    def GetItemsSelected(self):
        tempItemsSelected = []
        for index, val in enumerate(self.TakenList):
            if val:
                tempItemsSelected.append(index)

        return tempItemsSelected
        # tempNode = self
        # tempItemsSelected = []
        # while tempNode.Index != -1:
        #     if tempNode.Taken:
        #         tempItemsSelected.append(tempNode.Index)
        #
        #     tempNode = tempNode.Parent
        #
        # tempItemsSelected.reverse()
        # return tempItemsSelected

    def PrintNodeTotalList(self):
        tempItems = []
        for index in range(len(items)):
            if index <= (len(self.TakenList)-1):
                if self.TakenList[index]:
                    tempItems.append(1)
                else:
                    tempItems.append(0)
            else:
                tempItems.append(0)

        print(tempItems)

    def PrintNodeList(self):
        tempItemsSelected = self.GetItemsSelected()
        print('Items Selected: ')
        for tempitem in tempItemsSelected:
            print("Index: ", tempitem, ", Value: ", items[tempitem].value, ', Weight: ', items[tempitem].weight)

    def PrintNodeStats(self):
        print('Value: ', self.Value, ', Capacity: ', self.Capacity, ', UpperBound: ', self.UpperBound)

    def PrintNode(self):
        print("-----Node-----")
        self.PrintNodeStats()
        self.PrintNodeList()

class Tree():
    def __init__(self):
        self.Head = None
        self.MaxNode = None
        self.UnexpandedNodes = []
        # self.MaxUpperBound = 0

    def AddNode(self, Taken):
        tempNode = Node(Taken, self.Head)
        if Taken:
            self.Head.Left = tempNode
        else:
            self.Head.Right = tempNode
            # if tempNode.UpperBound > self.MaxUpperBound:
            #     self.MaxUpperBound = tempNode.UpperBound

        self.Head = tempNode
        # self.Head.PrintNodeTotalList()
    def RegressTillTrue(self):
        while self.Head.Index != -1:
            self.Head = self.Head.Parent
            if self.Head.Right == None:
                return True
            else:
                del self.Head.Left
                del self.Head.Right
        return False

    def CheckMaxNode(self):
        if self.Head.Value > self.MaxNode.Value:
            self.MaxNode = self.Head

    def CheckNodeFeasibility(self):
        if (self.Head.Capacity <= capacity) and ((self.Head.Index) != (len(items)-1)) and (self.Head.UpperBound > self.MaxNode.Value):
            return True
        else:
            return False

    def ExpandNode(self):
        self.UnexpandedNodes.remove(self.Head)

        tempNodeTaken = Node(True, self.Head)
        tempNodeNotTaken = Node(False, self.Head)

        # self.Head.Left = tempNodeTaken
        # self.Head.Right = tempNodeNotTaken

        del self.Head

        self.Head = tempNodeTaken
        if self.CheckNodeFeasibility():
            self.CheckMaxNode()
            self.UnexpandedNodes.append(self.Head)
        else:
            del self.Head

        self.Head = tempNodeNotTaken
        if self.CheckNodeFeasibility():
            self.UnexpandedNodes.append(self.Head)
        else:
            del self.Head

    def ChooseNodeToExpand(self):
        tempMaxNode = self.UnexpandedNodes[0]
        for node in self.UnexpandedNodes:
            if node.UpperBound > tempMaxNode.UpperBound:
                tempMaxNode = node
        self.Head = tempMaxNode

    def CleanUnexpandedNodes(self):
        for node in reversed(self.UnexpandedNodes):
            if node.UpperBound <= self.MaxNode.Value:
                self.UnexpandedNodes.remove(node)
                del node


# def create_id(tempAgreeList):
#     id = 0
#     for index, i in enumerate(tempAgreeList):
#         id += 2**(index + i)
#     return id

def sort_by_density(items):
    items.sort(key=lambda x : x[3])
    items.reverse()

def sort_by_weight(items):
    items.sort(key=lambda x : x[2])
    items.reverse()

def sort_by_value(items):
    items.sort(key=lambda x : x[1])
    items.reverse()

def calculate_relaxed_integer_upperbound(tempLeveltems,capacity):
    UpperBound = 0
    tempCapacity = 0
    for item in tempLeveltems:
        if (tempCapacity + item.weight) > capacity:
            UpperBound += item.value*(capacity - tempCapacity)/item.weight
            break
        else:
            tempCapacity += item.weight
            UpperBound += item.value
    return int(UpperBound)
#
# def add_node(mainTree, tf, cap, bbv, tub, inds, par, agreeList):
#     mainTree.create_node(identifier=create_id(agreeList), \
#                          data = [cap, \
#                                  bbv, \
#                                  tub, \
#                                  inds, \
#                                  tf],
#                          parent = par)
#
# def add_node_1(mainTree, items, level, pastnode, capacity, agreeList):
#     newCapacity = mainTree[pastnode].data[0]+items[level].weight #Add current node weight
#     newCurrentBranchandBoundValue = mainTree[pastnode].data[1]+items[level].value #Add current value
#     newCurrentTheoreticalUpperBound = mainTree[pastnode].data[2]
#     newIndices = mainTree[pastnode].data[3] + [level]
#     newParent = pastnode
#     # listOfItems.append([tempLevel, CurrentBranchandBoundValue, CurrentTheoreticalUpperBound]) #Add current node to items list
#
#     add_node(mainTree, \
#              True, \
#              newCapacity, \
#              newCurrentBranchandBoundValue, \
#              newCurrentTheoreticalUpperBound, \
#              newIndices, \
#              newParent, \
#              agreeList)
#
# def add_node_0(mainTree, items, level, pastnode, capacity, agreeList):
#     tempItemsWithoutTempi = items.copy()
#     tempIndexNotChosenList = []
#
#     for index, levelToPop in enumerate(agreeList):
#         if levelToPop == 0:
#             tempIndexNotChosenList.append(index)
#             continue
#     tempIndexNotChosenList.reverse()
#     for index in tempIndexNotChosenList:
#         tempItemsWithoutTempi.pop(index)
#     sort_by_density(tempItemsWithoutTempi)
#
#     newCapacity = mainTree[pastnode].data[0]
#     newCurrentBranchandBoundValue = mainTree[pastnode].data[1]
#     newCurrentTheoreticalUpperBound = calculate_relaxed_integer_upperbound(tempItemsWithoutTempi, capacity)
#     newIndices = mainTree[pastnode].data[3]
#     newParent = pastnode
#
#     add_node(mainTree, \
#             False, \
#             newCapacity, \
#             newCurrentBranchandBoundValue, \
#             newCurrentTheoreticalUpperBound, \
#             newIndices, \
#             newParent, \
#             agreeList)
#
# def regress_till_true(mainTree, items, level, pastnode, capacity, agreeList):
#     tempNode = mainTree[pastnode].predecessor(mainTree.identifier)
#     agreeList.pop()
#
#     if not any(agreeList):
#         return -1, [], create_id([])
#
#     while True:
#         if mainTree[tempNode].data[4]:
#             tempPastNode = mainTree[tempNode].predecessor(mainTree.identifier)
#             agreeList[-1] = 0
#             break
#         else:
#             tempNode = mainTree[tempNode].predecessor(mainTree.identifier)
#             agreeList.pop()
#             level -= 1
#             continue
#     return level-1, agreeList, create_id(agreeList[:-1])

def solve_it(input_data):
    print('\n\n New Line \n\n')
    global items, capacity
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    #Include option to get value density
    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        if int(parts[1]) <= capacity:
            items.append(Item(i-1, int(parts[0]), int(parts[1]),int(parts[0])/int(parts[1])))

    #Initialize taken list
    taken = [0]*len(items)

    ## First sort by value/weight with greatest value/weight at start
    # sort_by_value(items)
    sort_by_weight(items)
    # sort_by_density(items)
    #

    ValueDensityList = []
    IndexList = []
    for index,item in enumerate(items):
        ValueDensityList.append(item.ValueDensity)
        IndexList.append(index)

    # plt.plot(IndexList,ValueDensityList)
    #
    # plt.show()

    #Brute Force
    BruteForce = False
    MainTree = Tree()
    MainTree.Head = Node(None, None)
    MainTree.AddNode(True)
    MainTree.MaxNode = MainTree.Head

    while BruteForce:
        # breakpoint()
        addNode = False
        regressNode = False
        if (MainTree.Head.Capacity < capacity) and ((MainTree.Head.Index) < (len(items)-1)):
            addNode = True
        elif (MainTree.Head.Capacity > capacity) or ((MainTree.Head.Index) == (len(items)-1)):
            regressNode = True

        if addNode:
            MainTree.CheckMaxNode()
            MainTree.AddNode(True)

        if regressNode:
            # breakpoint()
            if MainTree.RegressTillTrue():
                continue
            else:
                break
        if (not addNode) and (not regressNode):
            MainTree.AddNode(False)

    print('---Brute Force---')
    MainTree.MaxNode.PrintNode()

    #Depth First

    DepthFirst = True
    MainTree = Tree()
    MainTree.Head = Node(None, None)
    MainTree.AddNode(True)
    MainTree.MaxNode = MainTree.Head

    iterations = 0
    while DepthFirst:
        iterations +=1
        # breakpoint()
        # if (iterations % 500) == 0:
        #     print('\n----Iteration----:', iterations)
        #     MainTree.MaxNode.PrintNode()
        #     MainTree.Head.PrintNode()

        if MainTree.CheckNodeFeasibility():
            MainTree.CheckMaxNode()
            MainTree.AddNode(True)

        else:
            if MainTree.RegressTillTrue():
                MainTree.AddNode(False)
                continue
            else:
                break

    print('---DepthFirst---Iterations:',iterations)
    MainTree.MaxNode.PrintNode()


    #Best First

    BestFirst = False

    MainTree = Tree()
    MainTree.Head = Node(None, None)
    MainTree.AddNode(True)
    MainTree.UnexpandedNodes.append(MainTree.Head)
    MainTree.MaxNode = MainTree.Head
    MainTree.Head = MainTree.Head.Parent
    MainTree.AddNode(False)
    MainTree.UnexpandedNodes.append(MainTree.Head)

    iterations = 0
    while BestFirst:
        # breakpoint()
        iterations += 1
        # ind = 0
        if (iterations % 500) == 0:
            print('\n----Iteration----:', iterations)
            MainTree.MaxNode.PrintNode()
        if len(MainTree.UnexpandedNodes) != 0:
            # print('---',MainTree.MaxNode.Value,'---')
            # for node in MainTree.UnexpandedNodes:
            #     node.PrintNodeTotalList()

            # breakpoint()

            MainTree.ChooseNodeToExpand()
            MainTree.ExpandNode()
            MainTree.CleanUnexpandedNodes()
            # ind =+ 1
        else:
            break

    print('---BestFirst---Iterations:',iterations)
    MainTree.MaxNode.PrintNode()


    #Attempt at Pairing

    # a trivial algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    value = 0
    weight = 0
    taken = [0]*len(items)

    for item in items:
        if weight + item.weight <= capacity:
            taken[item.index] = 1
            value += item.value
            weight += item.weight

    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')
