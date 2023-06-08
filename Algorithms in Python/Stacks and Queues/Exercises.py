# EXERCISE 1.
# Use a single list to create three stacks.
# _____________________________________________________________________________________________________________________________

# Why on earth would anyone want to do this???  If you do...

class MultiStack:
    def __init__(self, stack_size):
        self.stack_size = stack_size
        self.number_stacks = 3
        self.sizes = [None] * self.number_stacks
        self.list = [None] * (self.stack_size * self.number_stacks)