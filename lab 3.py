# Write a recursive function that computes the sum of all numbers from 1 to n, where n is given as parameter.

def sum(n):
    return 1 if n == 1 else n + sum(n-1)
# Write a recursive function that finds and returns the minimum element in an array, where the array and its size are given as parameters.

def findmin(arr, n):
    return arr[0] if n==1 else min(arr[n-1], findmin(arr, n-1))
# Write a recursive function that computes and returns the sum of all elements in an array, where the array and its size are given as parameters.

def findsum(arr, n):
    return arr[0] if n==1 else arr[n-1] + findsum(arr, n-1)
# Write a recursive function that determines whether an array is a palindrome, where the array and its size are given as parameters.

def is_palindrome(arr, n):
    return True if n == 0 or n == 1 else arr[n-1] == arr[0] and is_palindrome(arr[1:n-1], n-2)
# Write a recursive function that searches for a target in a sorted array using binary search, where the array, its size and the target are given as parameters.

def binary_search(arr, n, target):
    if n == 0:
        return False
    mid = n // 2
    if arr[mid] == target:
        return True
    elif arr[mid] > target:
        return binary_search(arr[:mid], mid, target)
    else:
        return binary_search(arr[mid+1:n], n - mid - 1, target)
# Implement the Greatest Common Divisor algorithm as recursive method GCD. Use recursion. Do NOT use a loop.

def gcd(a, b):
    return a if b==0 else gcd(b, a%b)
# Implement the power function recursively

def power(a, b):
    return 1 if b == 0 else a*power(a, b-1)
# Implement the factorial function recursively as fact

def fact(n):
    return 1 if n == 0 else n*fact(n-1)
# Implement Fibonacci recursively as f

def Fibonacci(n):
    return 1 if n<=2 else Fibonacci(n-1) + Fibonacci(n-2)
# Write recursive method addReciprocals that takes an integer as a parameter and returns the sum of the first n reciprocals. addReciprocals(n) returns (1.0 + 1.0/2.0 + 1.0/3.0 + 1.0/4.0 + ... + 1.0/n).

def addReciprocals(n):
    return 1 if n == 1 else 1/n + addReciprocals(n-1)
#Tree height. Given a labeled binary tree (represented by a pointer to a TreeNode) calculate its height.

class TreeNode:
    def __init__(self, label, left=None, right=None):
        self.label = label
        self.left = left
        self.right = right

def tree_height(tree):
    if tree is None:
        return 0
    else:
        left_height = tree_height(tree.left)
        right_height = tree_height(tree.right)
        return max(left_height, right_height) + 1
# Tree size. Given a labeled binary tree (represented by a pointer to a TreeNode) calculate its size.

class TreeNode:
    def __init__(self, label, left=None, right=None):
        self.label = label
        self.left = left
        self.right = right

def tree_size(tree):
    if tree is None:
        return 0
    else:
        return 1 + tree_size(tree.left) + tree_size(tree.right)