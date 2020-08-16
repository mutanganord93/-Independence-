import SeparateChainingHashST
import BinarySearchT

def message():
	print("Select an option number:")
	print("1. Print country and its colonial information")
	print("2. Print colonial power and its old colonies")
	print("3. Print countries in the order they accessed independence")
	print("4. Print the oldest country to access independence")
	print("5. Print the youngest country to access independence")
	print("6. Print countries in range x and y of the year they got access to independence")

seq = SeparateChainingHashST.SeparateChainingHashST(20)
indepCountr = SeparateChainingHashST.SeparateChainingHashST(20)
projectTest = BinarySearchT.country()
myTree = BinarySearchT.BinarySearchTree()
arr = projectTest.fileReader('indepC.txt')
for line in arr:
		myTree.insert(line)

message()
value = input("option:\n")

while value != 'no':
	try:
		value = int(value)
		if value == 1:
			country = input("country: ")
			for line in arr:
				indepCountr.put(line.countryName,line)
			indepCountr.find(country)

		elif value == 2:
			for line in arr:
				seq.put(line.colonialPower,line)
			country = input("country: ")
			seq.find(country)

		elif value == 3:
			myTree.walk()

		elif value == 4:
			print(f"{myTree.findMin().data.countryName}, {myTree.findMin().data.colonyName}, {myTree.findMin().data.colonialPower}, {myTree.findMin().data.indYear}, {myTree.findMin().data.leader}")

		elif value == 5:
			print(f"{myTree.treeMax().countryName}, {myTree.treeMax().colonyName}, {myTree.treeMax().colonialPower}, {myTree.treeMax().indYear}, {myTree.treeMax().leader}")

		elif value == 6:
			q = myTree.rangeSearch("1 February 1947","4 January 1969")
			while q:
				s = q.popleft()
				print(f"{s.countryName}, {s.colonyName}, {s.colonialPower}, {s.indYear}, {s.leader}")
		
		print("Do you want to perform an operation?(yes/no)")
		value = input("option:\n")
		if value == 'yes':
			message()
			value = input("option:\n")
	except ValueError:
		print('Invalid input')