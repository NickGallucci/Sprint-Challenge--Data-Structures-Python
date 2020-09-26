class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.oldest_data = 0

    def append(self, item):
        # Check if the length of the list is less tha the capacity
        if len(self.storage) < self.capacity:
            # Append item to the end of the list
            self.storage.append(item)
        # If the list has reached capacity
        else:
            #Append the item by replacing the item at the oldest index
            self.storage[self.oldest_data] = item
            #Checks if the oldest item is the last item in the list
            if self.oldest_data < len(self.storage) - 1:
                self.oldest_data += 1
            #Increment the oldest index
            else:
            #Reset oldest to first index
                self.oldest_data = 0

    def get(self):
        #Returns the list
        return self.storage