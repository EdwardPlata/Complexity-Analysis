def insert_sort(arr, simulation = False):
	for i in range(len(arr)):
		cursor = arr[i]
		pos = i
		while pos > 0 and arr[pos-1] > cursor:
			arr[pos] = arr[pos-1]
			pos = pos-1
			arr[pos] = cursor
	return arr
def main():
	arr = [5,4,3,2,1]
	return insert_sort(arr)

if __name__ == '__main__':
	print(main())
