def remove_duplicates(arr):
   new_list = []
   for num in arr:
       if num not in new_list:
           new_list.append(num)
   return new_list
arr = [6, 8, 5, 4, 6, 8, 9, 1, 4, 9, 12]
print(remove_duplicates(arr))