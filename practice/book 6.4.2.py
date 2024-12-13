class binary_tree:
    def __init__(self, root_obj):
        self.key = root_obj
        self.left_child = None
        self.right_child = None
    def insert_left(self, new_node):
        if self.left_child is None:
            self.left_child = binary_tree(new_node)
        else:
            t = binary_tree(new_node)   #新建一颗树
            t.left = self.left_child    #
            self.left_child = t
    def insert_right(self, new_node):
        if self.right_child is None:
            self.right_child = binary_tree(new_node)
        else:
            t = binary_tree(new_node)
            t.right = self.right_child
            self.right_child = t
    def get_left_child(self):
        return self.left_child
    def get_right_child(self):
        return self.right_child
    def get_root_value(self):
        return self.key
    def set_root_value(self, obj):
        self.key = obj



r = binary_tree(1)
r.insert_left(2)
r.insert_right(3)
r.insert_left(4)
l = r.get_left_child()


