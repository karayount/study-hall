class Tree(object):

    def __init__(self, root):
        self.root = root

    def find_DFS(self, node):
        to_check = [self.root]
        while to_check:
            check = to_check.pop()
            print check
            if check == node:
                return node
            to_check.extend(check.children)

    def find_BFS(self, node):
        to_check = [self.root]
        while to_check:
            check = to_check.pop(0)
            print check
            if check == node:
                return node
            to_check.extend(check.children)

    def __repr__(self):
        return "<Tree root=%s>" % self.root.data


class TreeNode(object):

    def __init__(self, data, children=None):
        self.data = data
        self.children = children or []

    def add_children(self, new_children):
        for child in new_children:
            self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

    def __repr__(self):
        return "<TreeNode data=%s>" % self.data


kara = TreeNode("Kara")
kevin = TreeNode("Kevin")
kyla = TreeNode("Kyla")
johanna = TreeNode("Johanna", [kara, kevin, kyla])
alison = TreeNode("Alison")
dana = TreeNode("Dana")
laura = TreeNode("Laura", [alison, dana])
richie = TreeNode("Richie", [johanna, laura])
consoli = Tree(richie)
print consoli