```python
#binary search
# Get the sorted list and the string to find from the user
sorted_list = input("Enter a sorted list of strings separated by spaces: ").split()
to_find = input("Enter the string to search for: ")

left = 0
right = len(sorted_list) - 1
found = False  # Initialize the found flag

# Perform binary search
while left <= right:
    mid = (left + right) // 2
    if sorted_list[mid] == to_find:
        print(f"{to_find} found at index {mid}")
        found = True
        break
    elif sorted_list[mid] < to_find:
        left = mid + 1
    else:
        right = mid - 1

# If not found, print a message
if not found:
    print(f"{to_find} not found in list.")

```

    Enter a sorted list of strings separated by spaces: 4 5 9 6 8 7 1
    Enter the string to search for: 5
    5 found at index 1



```python

```
