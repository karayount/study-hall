""" Given a tree, write a function to find all the 'cousins' of a given node,
where cousins are all nodes of that generation (depth from root)
"""

class Tree(object):

    def __init__(self, root=None):
        self.root = root

    def find_cousins(self, person):
        """
        find all Nodes of the same depth as input Node person
        :param person: tree Node sought
        :return: list of tree Nodes from depth, or empty list if none
        """

        current_tier =[self.root]
        children_tier = []
        while current_tier:
            for item in current_tier:
                children_tier.extend(item.children)
            if person in children_tier:
                return children_tier
            else:
                current_tier = children_tier
                children_tier = []
        return children_tier