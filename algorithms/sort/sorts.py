import random

class Sort:
    def sort(self, nums):
        print(self)
        nums_sorted = self._sort(nums)
        print('before sort: {}'.format(nums))
        print('after sort: {}'.format(nums_sorted))

    def _sort(self, nums):
        return nums

    def __str__(self):
        return 'No sort'


class DefaultSort(Sort):
    def _sort(self, nums):
        return sorted(nums)

    def __str__(self):
        return 'Default sort'


class QuickSort(Sort):
    def _sort(self, nums):
        return self._quick_sort(nums)

    def _quick_sort(self, nums):
        if len(nums) == 0:
            return []
        pivol = nums[0]
        lt_list = [v for v in nums[1:] if v < pivol]
        gte_list = [v for v in nums[1:] if v >= pivol]

        return self._quick_sort(lt_list) + [pivol] + self._quick_sort(gte_list) 

    def __str__(self):
        return 'Quick sort'


class MergeSort(Sort):
    def _sort(self, nums):
        return self._merge_sort(nums)

    def _merge_sort(self, nums):
        n = len(nums)
        if n <= 1:
            return nums
        elif n == 2:
            return [min(nums), max(nums)]
        else:
            l_list = self._merge_sort(nums[:n//2])
            r_list = self._merge_sort(nums[n//2:])
            # print(l_list, r_list)
            merged_list = []

            l_len = len(l_list)
            r_len = len(r_list)
            l_index = 0
            r_index = 0
            while l_index < l_len and r_index < r_len:
                if l_list[l_index] <= r_list[r_index]:
                    merged_list.append(l_list[l_index])
                    l_index += 1
                else:
                    merged_list.append(r_list[r_index])
                    r_index += 1
            
            if l_index < l_len:
                merged_list.extend(l_list[l_index:])
            if r_index < r_len:
                merged_list.extend(r_list[r_index:])

            return merged_list


    def __str__(self):
        return 'Merge sort'

def get_random_list(n):
    return [random.randint(1, 10) for i in range(n)]

if __name__ == '__main__':
    nums = get_random_list(10)
    
    s = Sort()
    s.sort(nums)

    s = DefaultSort()
    s.sort(nums)

    s = QuickSort()
    s.sort(nums)

    s = MergeSort()
    s.sort(nums)
    