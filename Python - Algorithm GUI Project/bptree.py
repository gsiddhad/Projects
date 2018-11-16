# Algorithms GUI Project / bptree.py
# Created on: 07-Nov-2018
# Author: Gourav Siddhad
# B Plus Tree

from bisect import bisect_left, bisect_right


class BPTree():

	def __init__(self, capacity = 0):
		if capacity < 2:
			capacity = 2
		self._tree = BPTreeLeaf([], None, capacity)
		self._capacity = capacity

	def read_File(self, inputFile):
		with open(inputFile, 'r') as Input:
			for line in Input:
				ints = [int(x) for x in line.split()]
				for v in ints:
					self.insert(v)

	def insert(self, key):
		pkey, ppointer = self._tree.insert(key)
		if pkey is not None:
			new_master_node = BPTreeNode([pkey], [self._tree, ppointer], self._capacity)
			self._tree = new_master_node

	def keys(self):
		return self._tree.keys()

	def find(self, key):
		return self._tree.find(key)

	def num_nodes(self):
		return self._tree.num_nodes()

	def num_leaves(self):
		return self._tree.num_leaves()

	def num_keys(self):
		return self._tree.num_keys()

	def height(self):
		return self._tree.height() + 1

	def stats(self):
		return (self.height(), self.num_nodes(), self.num_leaves(), self.num_keys())

	def __str__(self):
		s = " Level\n "
		for level in range(1, self.height() + 1):
			if level == 1:
# 				s += ' ' * self.num_keys() * 2 + str(self._tree)
				s += '' + str(self._tree)
			elif level == self.height():
				count = 0
				s += "\n Level\n "
				leaf = self._tree._pointers[0]
				for i in range(self.height() - 2):
					leaf = leaf._pointers[0]

				while leaf._next is not None:
					s += str(leaf) + " -> "
					count += 1
					if count % 6 == 0:
						s += '\n '
					leaf = leaf._next
				s += str(leaf)
			elif level == 2:
				s += "\n Level\n "
# 				s += ' ' * self.num_keys()
				for child in self._tree._pointers:
					s += str(child) + " "
# 					s += ' ' * self.num_keys()
			elif level == 3:
				s += "\n Level\n "
# 				s += ' ' * self.num_keys()
				for child in self._tree._pointers:
					for kid in child._pointers:
						s += str(kid) + " "
			elif level == 4:
				s += "\n Level\n "
# 				s += ' ' * self.num_keys()
				for child in self._tree._pointers:
					for kid in child._pointers:
						for kid2 in kid._pointers:
							s += str(kid2) + " "

			elif level == 5:
				s += "\n Level\n "
# 				s += ' ' * self.num_keys()
				for child in self._tree._pointers:
					for kid in child._pointers:
						for kid2 in kid._pointers:
							for kid3 in kid._pointers:
								s += str(kid3) + " "
			s += "\n "
		return s


class BPTreeNode():

	def __init__(self, keys, pointers, capacity):
		self._keys = keys  # in sorted order
		self._pointers = pointers  # one more than the number of keys
		self._capacity = capacity

	def keys(self):
		return self._pointers[0].keys()

	def find(self, key):
		return self._pointers[bisect_right(self._keys, key)].find(key)

	def insert_here(self, position, key, pointer):  # inserting at node level
		self._keys.insert(position, key)
		self._pointers.insert(position + 1, pointer)

		cap = self._capacity
		split_index = (cap + 1) // 2
		if len(self._keys) > cap:
			pkey = self._keys[split_index]
			self._keys.remove(pkey)

			new_lateral_node = BPTreeNode(self._keys[split_index:], self._pointers[split_index + 1:], cap)

			self._keys = self._keys[:split_index]
			self._pointers = self._pointers[:split_index + 1]

			return (pkey, new_lateral_node)
		return (None, None)

	def insert(self, key):
# 		insert key into this subtree
# 		return (None, None) if there is nothing to promote
# 		return (pkey, ppointer) if self splits

		# Insert down correct path
		(pkey, ppointer) = self._pointers[bisect_right(self._keys, key)].insert(key)

		# Handle promotions
		if pkey is not None:
			position = bisect_left(self._keys, pkey)
			(promoted_key, new_lateral_node) = self.insert_here(position, pkey, ppointer)
			return (promoted_key, new_lateral_node)
		return (None, None)

	def num_nodes(self):
#         Number of nodes in this subtree including this one
# 		Sum of num_nodes of each child plus 1
		return 1 + sum(map(lambda n: n.num_nodes(), self._pointers))

	def num_leaves(self):
#         ''' number of leaves in this subtree'''
		# Sum of num_leaves of each child
		return sum(map(lambda n: n.num_leaves(), self._pointers))

	def num_keys(self):
#         number of keys in the leaves of this subtree
		# Map num_keys to each child node then sum the results
		return sum(map(lambda n: n.num_keys(), self._pointers))

	def height(self):
#         ''' height of this subtree'''
		return 1 + self._pointers[0].height()

	def __str__(self):
		return str(self._keys)


class BPTreeLeaf():

	def __init__(self, keys, next_leaf, capacity):
		self._keys = keys  # in sorted order
		self._next = next_leaf  # next BPTreeLeaf
		self._capacity = capacity

	def keys(self):
		all_keys = []
		for element in self._keys:
			all_keys.append(element)
		current = self
		while current._next is not None:
			current = current._next
			all_keys.extend(current._keys)
		return all_keys

	def find(self, key):
		return key in self._keys

	def insert(self, key):
# 		insert key into self. A key should not appear twice in the BPTreeLeaf level
# 		return (None, None) if there is nothing to promote
# 		return (pkey, ppointer) if self splits
# 		(pkey, ppointer) this is the promoted key, and,
# 		a pointer to the newly created

		index = bisect_left(self._keys, key)
		if index == len(self._keys) or self._keys[index] != key:
			self._keys.insert(index, key)

		cap = self._capacity
		split_index = (cap + 1) // 2

		if len(self._keys) > cap:
			new_leaf = BPTreeLeaf(self._keys[split_index:], self._next, cap)

			self._keys = self._keys[:split_index]
			self._next = new_leaf

			return (new_leaf._keys[0], new_leaf)
		return (None, None)

	def num_nodes(self):
		return 0

	def num_leaves(self):
		return 1

	def num_keys(self):
		return len(self._keys)

	def height(self):
		return 0

	def __str__(self):
		return str(self._keys)
