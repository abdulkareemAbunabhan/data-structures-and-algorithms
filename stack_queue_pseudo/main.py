from stack_queue_pseud import PseudoQueue

que=PseudoQueue()
que.enqueue("1")
que.enqueue("1")
que.enqueue("1")
print(que.dequeue())
print(que.__str__())

tester=PseudoQueue()
tester.enqueue("1")
tester.enqueue("2")
tester.enqueue("3")
tester.enqueue("4")
tester.enqueue("5")
tester.dequeue()
tester.dequeue()
tester.enqueue("7")
print(tester.__str__())