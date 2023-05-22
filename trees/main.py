from binary_tree import *

tes=Binary_trees()
tes.adds("1")
tes.adds("2")
tes.adds("3")
tes.adds("4")
tes.adds("6")
print(tes.pre_order())
print(tes.in_order())
print(tes.post_order())

ted=Binary_search_tree()
ted.add(15)
ted.add(5)
ted.add(25)
ted.add(3)
ted.add(7)
ted.add(23)
ted.add(27)
print(ted.contains(11))
print(ted.contains(7))
print(ted.contains(23))
print(ted.contains(13))
print(ted.in_order())
print(ted.pre_order())
print(ted.post_order())