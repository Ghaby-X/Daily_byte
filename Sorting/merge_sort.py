class merge_sort:
    def __init__(self) -> None:
        pass
    
    def sort(self, nums: list):
        if len(nums) == 1:
            return nums
        
        mid = len(nums) // 2
        
        left_nums = self.sort(nums[0:mid].copy())
        right_nums = self.sort(nums[mid:].copy())
        
        return self.merge(left_nums, right_nums)

    
    def merge(self, arr1: list, arr2: list):
        arr1_counter = 0
        arr2_counter = 0
        merged_array = []
        
        
        while arr1_counter < len(arr1) and arr2_counter < len(arr2):
            if arr1[arr1_counter] <= arr2[arr2_counter]:
                merged_array.append(arr1[arr1_counter])
                arr1_counter += 1
                continue
                
            if arr1[arr1_counter] > arr2[arr2_counter]:
                merged_array.append(arr2[arr2_counter])
                arr2_counter += 1
        
        while arr1_counter < len(arr1):
            merged_array.append(arr1[arr1_counter])
            arr1_counter += 1
        
        while arr2_counter < len(arr2):
            merged_array.append(arr2[arr2_counter])
            arr2_counter += 1
        
        return merged_array
                

if __name__ == '__main__':
    sorter = merge_sort()
    
    print(sorter.sort([1,6,7,3,8,2,2,5,0,9,3]))