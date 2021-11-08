from queue import Queue

def hot_potato(names_list, num):
    """return the name of the last person remaining after repetitive counting by num"""
    name_queue = Queue()

    #loop through, send each name to empty queue
    for name in names_list:
        name_queue.enqueue(name)

    while name_queue.size() > 1:
        for i in range(num): # loop 0 to n-1
            name_queue.enqueue(name_queue.dequeue())
        name_queue.dequeue()
    return name_queue.dequeue()

print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 18))
