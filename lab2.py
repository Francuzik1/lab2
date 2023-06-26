from Adapter import Adapter
from Node import Node, SLinkedList
capital_one = SLinkedList()
capital_one.headval = Node("Italy", "Rome")
var_1 = Node("Belarus", "Minsk")
var_2 = Node("UK", "London")
var_3 = Node("Germany", "Berlin")
var_4 = Node("Spain", "Madrid")
capital_one.headval.nextval = var_1
var_1.nextval = var_2
var_2.nextval = var_3
var_3.nextval = var_4
bister = capital_one.list_returner()
print(bister)
for e in bister:
    e = Adapter(e[0], e[1])
print(e.for_printer('Spain'))
print(e.for_printer('Spain'))
print(e.for_printer('Italy'))
print(e.for_printer('Belarus'))
e.deliter('Spain')
