class BinaryHeap:
    def __init__(self, heap_type='min'):
        self.heap = []
        self.heap_type = heap_type.lower()  

    def size(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.heap[0]

    def push(self, value):
        self.heap.append(value)
        self.heapify_up()

    def pop(self):
        if self.is_empty():
            return None

        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        del self.heap[-1]
        self.heapify_down()

        return root

    def heapify_up(self):
        index = len(self.heap) - 1

        while self.has_parent(index) and self.should_heapify_up(index):
            parent_index = self.get_parent_index(index)
            self.swap(index, parent_index)
            index = parent_index

    def heapify_down(self):
        index = 0

        while self.has_left_child(index):
            smaller_child_index = self.get_left_child_index(index)

            if self.has_right_child(index) and self.compare_children(smaller_child_index, self.get_right_child_index(index)):
                smaller_child_index = self.get_right_child_index(index)

            if self.should_heapify_down(index, smaller_child_index):
                break

            self.swap(index, smaller_child_index)
            index = smaller_child_index

    def compare_children(self, left_index, right_index):
        if self.heap_type == 'min':
            return self.heap[left_index] > self.heap[right_index]
        elif self.heap_type == 'max':
            return self.heap[left_index] < self.heap[right_index]

    def should_heapify_up(self, child_index):
        if self.heap_type == 'min':
            return self.heap[child_index] < self.heap[self.get_parent_index(child_index)]
        elif self.heap_type == 'max':
            return self.heap[child_index] > self.heap[self.get_parent_index(child_index)]

    def should_heapify_down(self, parent_index, child_index):
        if self.heap_type == 'min':
            return self.heap[parent_index] > self.heap[child_index]
        elif self.heap_type == 'max':
            return self.heap[parent_index] < self.heap[child_index]

    def has_parent(self, index):
        return index > 0

    def has_left_child(self, index):
        return self.get_left_child_index(index) < len(self.heap)

    def has_right_child(self, index):
        return self.get_right_child_index(index) < len(self.heap)

    def get_parent_index(self, index):
        return (index - 1) // 2

    def get_left_child_index(self, index):
        return 2 * index + 1

    def get_right_child_index(self, index):
        return 2 * index + 2

    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]


min_heap = BinaryHeap(heap_type='min')

elements_to_insert = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
for element in elements_to_insert:
    min_heap.push(element)

print("Min Heap:")
while not min_heap.is_empty():
    print(min_heap.pop(), end=' ')
