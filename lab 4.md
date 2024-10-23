```python
# linear search 

string = input("Enter a string: ")
target = input("Which character to search for: ")


found = False


for index in range(len(string)):
    if target == string[index]:
        print(f"Element found at index {index}")
        found = True
        break  


if not found:
    print("Element not found.")

```

    Enter a string: 4 5 7 6 2 3
    Which character to search for: 4
    Element found at index 0



```python

```
