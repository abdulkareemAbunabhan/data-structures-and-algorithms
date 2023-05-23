from tree_max import *

tes=Binary_trees()
tes.adds("1")
tes.adds("2")
tes.adds("3")
tes.adds("4")
tes.adds("6")
print(tes.pre_order())
print(tes.in_order())
print(tes.post_order())
print(tes.max)
print(tes.tree_max())