# -- coding: utf-8 --
"""
Created on Tue Mar 14 15:42:53 2023

@author: Jorge Roa & Carmen Garro
"""

from cq import CircularQueue

#Example 1
cirqe = CircularQueue()
cirqe.enqueue(1)
cirqe.enqueue(2)
cirqe.enqueue(3)
print(cirqe)


#Example 2

# Use the rotate method to move the first element to the end of the queue
cirqe.rotate()
print("Queue after rotate:", cirqe)

# Dequeue the element and display the updated queue
dequeued_element = cirqe.dequeue()
print("Dequeued element:", dequeued_element)
print("Queue after dequeue:", cirqe)


#Example 3: Look at the next element to be dequeued without removing it

# Create a new CircularQueue instance
cirqe = CircularQueue()

# Enqueue some elements
cirqe.enqueue(1)
cirqe.enqueue(2)
cirqe.enqueue(3)

# Display the current state of the queue
print("Current Queue:", cirqe)

# Use the peek method to look at the next element without dequeuing it
next_element = cirqe.peek()
print("Next element to be dequeued:", next_element)

# Display the queue again to show that the element has not been dequeued
print("Queue after peek:", cirqe)

# Dequeue the element and display the updated queue
dequeued_element = cirqe.dequeue()
print("Dequeued element:", dequeued_element)
print("Queue after dequeue:", cirqe)

