class Solution(object):
   def searchRange(self, numbers, value):
      res = [0, 0]
      low = 0
      high = len(numbers)
      while low < high:
         mid = int(low + (high-low)//2)
         if numbers[mid] == value:
            high = mid
            res[0] = mid
            res[1] = mid
         elif numbers[mid] < value:
            low = mid+1
         else:
            high = mid
      if res[0] == -1:
         return res
      low = res[0]+1
      high = len(numbers)
      while low < high:
         mid = int(low + (high-low)//2)
         if numbers[mid] == value:
            low = mid+1
            res[1] = mid
         elif numbers[mid] < value:
            low = mid + 1
         else:
            high = mid
      return res


ob1 = Solution()
print(ob1.searchRange([5,7,7,9,9,10], 9))
