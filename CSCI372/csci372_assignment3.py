class intSet:
    
    def __init__(self):
        self.elements = []
        self.size = 0
    
    def insert(self, element):
        if element not in self.elements:
            self.elements.append(element)
            self.size += 1
            
    def remove (self, element):
        if element in self.elements:
            self.elements.remove(element)
            self.size -= 1
    
    def isMember(self,element):
        return element in self.elements
    
    def isSubset (self, other_set):
        return all(element in other_set.elements for element in self.elements)

    def intersect (self, other_set):
        new_set = intSet()
        for element in self.elements:
            if other_set.isMember(element):
                new_set.add(element)
        return new_set
    
    def union(self, other_set):
        new_set = intSet()
        for element in self.elements:
            new_set.add(element)
        for element in other_set.elements:
            if not new_set.isMember(element):  # Check if element already exists in the new set
                new_set.add(element)
        return new_set
    
    def diff(self, other_set):
        new_set = intSet()
        for element in self.elements:
            if not other_set.isMember(element):
                new_set.add(element)
        return new_set        