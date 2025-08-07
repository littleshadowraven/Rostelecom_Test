def find_triplets(arr):
	result = []
	n = len(arr)

	for i in range(n - 2):
		for j in range(i + 1, n - 1):
			for k in range(j + 1, n):

				if arr[i] + arr[j] + arr[k] == 0:
					if [arr[i], arr[j], arr[k]] not in result:
						result.append([arr[i], arr[j], arr[k]])
	return result


arr = [-1, 0, 1]
res = find_triplets(arr)
print(res)

arr = [0, 0, 0, 0]
res = find_triplets(arr)
print(res)

arr = [-2, 0, 1, 1, 2]
res = find_triplets(arr)
print(res)
