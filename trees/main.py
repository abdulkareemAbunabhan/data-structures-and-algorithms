from binary_tree import *

tes=Binary_trees()
tes.add("1")
tes.add("2")
tes.add("3")
tes.add("4")
tes.add("6")
print(tes.res)
print(tes.pre_order())
print(tes.in_order())
print(tes.post_order())

ted=Binary_search_tree()
ted.adds("15")
ted.adds("5")
ted.adds("25")
ted.adds("3")
ted.adds("7")
ted.adds("23")
ted.adds("27")
print(ted.contains("11"))
print(ted.contains("7"))
print(ted.in_order())
print(ted.post_order())
