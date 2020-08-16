from collections import deque
import compareTo
import csv

class country:
	def __init__(self):
		self.countryName = None
		self.colonyName = None
		self.colonialPower = None
		self.leader = None
		self.indYear = None
		self.politicParty = None

	def fileReader(self,file):
		myIndependenceList = []
		with open(file)as csv_file:
			csv_reader = csv.reader(csv_file,delimiter=',')
			for row in csv_reader:
				liberation = country()
				liberation.countryName = row[0]
				liberation.colonyName = row[1]
				liberation.colonialPower = row[2]
				liberation.indYear = row[3]
				liberation.leader = row[4]
				liberation.politicParty = row[5]
				myIndependenceList.append(liberation)
		return myIndependenceList

class Node:
	def __init__(self,data):
		self.data = data
		self.right = None
		self.left = None
		self.parent = None

class BinarySearchTree:
	def __init__(self):
		self.root = None

	def setRoot(self,data):
		self.root = Node(data)

	def insert(self,data):
		node = Node(data)
		return self.setNode(node)

	def setNode(self,node):
		y = None
		x = self.root

		# travel down a tree
		while x is not None:
			y = x
			if compareTo.compareTo().CompareTo(node.data.indYear,x.data.indYear) == -1:
				x = x.left
			else:
				x = x.right
		
		node.parent = y

		if y is None:
			self.setRoot(node.data)
		
		elif compareTo.compareTo().CompareTo(node.data.indYear,y.data.indYear) == -1:
			y.left = node
		else:
			y.right = node
	
	def findMin(self):
		return self.treeMin(self.root)

	def treeMin(self,minVal):
		while minVal.left is not None:
			minVal = minVal.left

		return minVal

	def treeMax(self):
		maxVal = self.root
		while maxVal.right is not None:
			maxVal = maxVal.right

		return maxVal.data


	def walk(self):
		return self.inOrderWalk(self.root)

	def inOrderWalk(self,cur):
		if cur is not None:
			self.inOrderWalk(cur.left)
			print(f"{cur.data.countryName}, {cur.data.colonyName}, {cur.data.colonialPower}, {cur.data.indYear}, {cur.data.leader}, {cur.data.politicParty}")
			self.inOrderWalk(cur.right)
	
	def find(self, val):
		return self.findNode(self.root, val)

	def findNode(self, currentNode, val):
		if(currentNode is None):
			return None
		elif(val == currentNode.data):
			return currentNode
		elif(val < currentNode.data):
			return self.findNode(currentNode.left, val)
		else:
			return self.findNode(currentNode.right, val)

	def rangeSearch(self,lo,hi):
		q = deque()
		self.range(self.root,q,lo,hi)
		return q
		

	def range(self,x,q,lo,hi):
		if x is None:
			return
		
		cmplo = compareTo.compareTo().CompareTo(lo,x.data.indYear)
		cmphi = compareTo.compareTo().CompareTo(hi,x.data.indYear)
		if cmplo < 0:
			self.range(x.left,q,lo,hi)
		if cmphi >= 0 and cmplo <= 0:
			q.append(x.data)
		if cmphi > 0:
			self.range(x.right,q,lo,hi)
		

	def transplant(self, u, v):
		if u.parent is None:
			self.root = v
		elif u is u.parent.left:
			u.parent.left = v
		else:
			u.parent.right = v
		if v is not None:
			v.parent = u.parent

	def delete(self,val):
		delVal = self.find(val)
		return self.treeDelete(delVal)

	def treeDelete(self,z):
		if z.left is None:
			self.transplant(z,z.right)
		elif z.right is None:
			self.transplant(z,z.left)
		else:
			y = self.treeMin(z.right)
			if y.parent is not z:
				self.transplant(y,y.right)
				y.right = z.right
				y.right.parent = y
			self.transplant(z,y)
			y.left = z.left
			y.left.parent = y

	# def print_root(self):
	# 	print(f"Root: {self.root.data}")  
