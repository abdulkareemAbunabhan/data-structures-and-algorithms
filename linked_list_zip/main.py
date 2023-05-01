from linked_list_kth import Linked_list

if __name__=="__main__":
    linkedlist=Linked_list()
    linkedlist.append("A")
    linkedlist.append("B")
    linkedlist.append("C")
    linkedlist.append("D")
    linkedlist.insert_after("D","L")


    
    print(linkedlist.__str__())