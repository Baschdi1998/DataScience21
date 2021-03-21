#---------------------------------------------------------------------------
# Class to store named Lists
#
# By: Bastian Junker
# Date: 21.03.2021
#---------------------------------------------------------------------------

class ListKeeper:
    
    # Initialize class with a dictionary called lists and add the list 'example' to it
    def __init__(self):
        self.lists = {}
        self.lists['example'] = [1,2,3,4,5]
        
    # Return all List names
    def show(self):
        return self.lists.keys()
    
    # Adds a List to the dictionary
    def add(self, name, list):
        self.lists[name] = list
    
    # Deletes the list 'name'
    def delete(self, name):
        self.lists.pop(name)
        
    # Returns the list sorted list 'name'
    def sort(self, name):
        self.lists[name].sort()
        return self.lists[name]
    
    # Add the given 'list' to the list 'name' -- self.list[name].append() is not used to prevent nested lists
    def append(self, name, list):
        self.lists[name] = self.lists[name] + list
        
    
        