class Vendor:
    def __init__(self, inventory= None):
        if not inventory:
            inventory = []
        self.inventory = inventory
    
    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not  in  self.inventory:
            return False
        self.inventory.remove(item)
        return item
        

    def get_by_category(self, category):
        items = []
        for item in self.inventory:
            if  item.category == category:
                items.append(item)
        return items
    
    def swap_items(self, friend_vendor, my_item, friend_item):
        if my_item not in self.inventory or friend_item not in friend_vendor.inventory:
            return False
        elif my_item not in friend_vendor.inventory and friend_item not in self.inventory:
            friend_vendor.add(my_item)
            self.remove(my_item)
            self.add(friend_item)
            friend_vendor.remove(friend_item)
            return True
        
    def swap_first_item(self, friend_vendor):
        if not friend_vendor.inventory or not self.inventory:
            return False
        first_friend_item= friend_vendor.inventory[0]
        first_self_item = self.inventory[0]
        self.swap_items(friend_vendor, first_self_item, first_friend_item)
        return True

    def get_best_by_category(self, category:str):
        # result = None
        # list_categories = [item for item in self.inventory if item.category.upper() == category.upper() ]
        # if not list_categories:
        #     return None
        # else:
        #     max_value = max([item.condition for item in list_categories])
        #     for item in list_categories:
        #         if item.condition == max_value:
        #             result = item 
        #     return result


        list_categories = [item for item in self.inventory if item.category.upper() == category.upper() ]
        max_value = max(list_categories, key = lambda c: c.condition, default=None)
        return max_value

    def swap_best_by_category(self, other, my_priority, their_priority):
        friend_request = self.get_best_by_category(their_priority)
        self_request = other.get_best_by_category(my_priority)
        return self.swap_items(other, friend_request, self_request)
        