
def quicksort(arr, step=0):
	if len(arr) <= 1:
		return arr
	else:
		pivot = arr[0]
		smaller = [i for i in arr[1:] if i <= pivot]
		bigger = [i for i in arr[1:] if i > pivot]
		print(' '*4*step + '{} {} {}'.format(smaller, pivot, bigger))
		return quicksort(smaller, step+1) + [pivot] + quicksort(bigger, step+1)

if __name__ == '__main__':
	print(quicksort([5,6,79,8,9,3,32,1,5,6,7,8]))
