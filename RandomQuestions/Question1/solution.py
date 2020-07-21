from collections import Counter

def stringAnagram(dictionary, query):
	arr1 = []
	for i in dictionary:
		temp = list(i)
		arr1.append(''.join(sorted(temp)))
	
	arr2 = Counter(arr1)
	
	hashmap = dict()
	ans = []
	for i in query:
		temp = ''.join(sorted(list(i)))
		if(temp in hashmap):
			ans.append(hashmap[temp])
			continue
		else:
			for j,k in enumerate(arr2):
				if(temp == k):
					ans.append(arr2[k])
					hashmap[temp] = arr2[k]
					break
			else:
				ans.append(0)
				hashmap[temp] = 0
	return ans
	
n1 = int(input("Enter the size of dictionary array: "))
print("Input the elements of dictionary array:")
dictionary = []
for i in range(n1):
	dictionary.append(input())

n2 = int(input("Enter the size of query array: "))
print("Input the elements of query array:")
query = []
for i in range(n2):
	query.append(input())

print("The resultant array is -")
print(stringAnagram(dictionary,query))