from board import Board
import copy

class Node:
    
    def __init__(self, value, name):
        self.value = value
        self.weight = 0
        self.name = name
        self.children = []
    
    def add_child(self, value, name):
        NewNode = Node(value, name)
        self.children.append(NewNode)
        
    def add_children():
        pass
    
    def calc_weight():
        pass
    
    def get_child():
        pass
    
    def choose_child():
        pass