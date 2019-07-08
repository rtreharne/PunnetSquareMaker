import random

def dict_from_parents(p1, p2):
    return p1, p2

if __name__ == "__main__":
    parent_1 = input("please enter the genotype of the first parent: ").split(';')
    parent_2 = input("please enter the genotype of the second parent: ").split(';') 
    p1, p2 = dict_from_parents(parent_1, parent_2)
    print(p1, p2)
