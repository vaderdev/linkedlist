class Node:
  def __init__(self, data=None, next=None):
    self.data = data
    self.next = next

class LinkedList:
  def __init__(self):
    self.head = None

  def insert_at_beginning(self, data):
    node = Node(data, self.head)
    self.head = node

  def insert_at_end(self, data):
    if self.head is None:
      self.head = Node(data)
      return 

    itr = self.head
    while itr.next:
      itr = itr.next

    itr.next = Node(data)

  def insert_values(self, data_list):
    self.head = None
    for d in data_list:
      self.insert_at_end(d)

  def get_length(self):
    count = 0
    itr = self.head
    
    while itr:
      count += 1
      itr = itr.next

    print(count)

  def remove(self, index):
    if index < 0 and index >= self.get_length():
      raise Exception("Invaild index.")

    if index == 0:
      self.head = self.head.next
      return

    count = 0
    itr = self.head
    while itr:
      if count == index - 1:
        itr.next = itr.next.next
        break
        
      itr = itr.next
      count += 1

  def insert(self, index, data):
    if index < 0 and index >= self.get_length():
      raise Exception("Invalid index.")

    if index == 0:
      self.insert_at_beginning(data)
      return
    
    count = 0
    itr = self.head
    while itr:
      if count == index - 1:
        node = Node(data, itr.next)
        itr.next = node
        break
        
      itr = itr.next
      count += 1

  def insert_after_value(self, data_after, data_to_insert):
    pass

  def remove_by_value(self, data):
    pass
      
  def print(self):
    if self.head is None:
      print("Linked list is empty.")
      return
      
    itr = self.head
    llstr = ''
    
    while itr:
      llstr += str(itr.data) + '-->'
      itr = itr.next
      
    print(llstr)

if __name__ == "__main__":
  ll = LinkedList()
  ll.insert_values([1, 2, 3, 4, 5])
  ll.insert_at_beginning(0)
  ll.print()