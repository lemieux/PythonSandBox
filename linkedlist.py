import time
 
def print_timing(func):
    def wrapper(*arg):
        t1 = time.time()
        res = func(*arg)
        t2 = time.time()
        print '%s took %0.3f ms' % (func.func_name, (t2-t1)*1000.0)
        return res
    return wrapper

class LinkedList:

	class Node:
		def __init__(self,value=None,next=None):
			self.value = value
			self.next = next

		def __str__(self):
			return str(self.value)


	def __init__(self):
		self.head = None

	def append(self,value):
		node = LinkedList.Node(value)
		if not self.head:
			self.head = node
			self.tail = node
		else:
			self.tail.next =  node
			self.tail = node

	def prepend(self,value):
		node = LinkedList.Node(value)
		node.next = self.head
		self.head = node

	
	def insert(self,value,index):
		new_node = LinkedList.Node(value)
		if index < 0:
			raise Exception("Index must be equal or higher than zero.")

		i = 0
		prev = None
		node = self.head	
		while i <= index:
			if not node:
				raise Exception("Index must be within the list range.")

			if i == index :
				if prev:
					prev.next = new_node
				else :
					self.head = new_node

				new_node.next=node

			else:
				prev = node
				node = node.next
			i+=1

	@print_timing
	def reverse(self):
		
		
		prev	= None
		current = self.head
		next 	= None

		while current :
			next = current.next
			current.next = prev
			prev = current
			current = next
		
		self.head = prev

	@print_timing
	def recursive_reverse(self):
		if self.head:
			self.head = self._reversenodes(self.head)
		

	def _reversenodes(self,node,prev = None):
		
		next =node.next
		node.next = prev
		prev = node
		node = next

		if node :
			return self.reversenodes(node,prev)
		else :
			return prev




	def __str__(self):
		val = "["
		node = self.head
		while node :
			val+=node.__str__()
			node = node.next
			if node:
				val+=", "
		val+="]"

		return val
		
	
	


list = LinkedList()
for i in range(10000):
	list.append(i)


list.reverse()
