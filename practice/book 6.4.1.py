def binary_tree(r):
    return [r, [], []]
def insert_left(root, new_branch):
    t = root.pop(1)

    if len(t) > 1:
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1, [new_branch, [], []])
    return root
def insert_right(root, new_branch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [new_branch, [], t])
    else:
        root.insert(2, [new_branch, [], []])
    return root
def get_root_value(root):
    return root[0]
def set_root_value(root, value):
    root[0] = value
def get_left_child(root):
    return root[1]
def get_right_child(root):
    return root[2]

r = binary_tree(1)
insert_left(r, 2)
insert_right(r, 3)
l = get_left_child(r)
set_root_value(l, 100)
insert_left(r, 4)
print(r)
