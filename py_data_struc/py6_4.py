# myTree = ['a', ['b', ['d',[],[]], ['e',[],[]]], ['c', ['f',[],[]], []]]
# print(myTree)
# print('left subtree = ', myTree[1])
# print('root = ', myTree[0])
# print('right subtree = ', myTree[2])
#
#
# def BinaryTree(r):
#     return [r, [], []]
#
# def insertLeft(root, newBranch):
#     t = root.pop(1)
#     if len(t) > 1:
#         root.insert(1, [newBranch, t, []])
#     else:
#         root.inesrt(1, [newBranch, [], []])
#     return root
#
# def insertRight(root,newBranch):
#     t = root.pop(2)
#     if len(t) > 1:
#         root.insert(2,[newBranch,[],t])
#     else:
#         root.insert(2,[newBranch,[],[]])
#     return root
#
# def getRootVal(root):
#     return root[0]
#
# def setRootVal(root,newVal):
#     root[0] = newVal
#
# def getLeftChild(root):
#     return root[1]
#
# def getRightChild(root):
#     return root[2]


class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key

r = BinaryTree('a')
print(r.getRootVal())
print(r.getLeftChild())
r.insertLeft('b')
print(r.getLeftChild())
print(r.getLeftChild().getRootVal())
r.insertRight('c')
print(r.getRightChild())
print(r.getRightChild().getRootVal())
r.getRightChild().setRootVal('hello')
print(r.getRightChild().getRootVal())

