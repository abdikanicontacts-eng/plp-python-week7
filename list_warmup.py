# Part A — List Warmup

# 1. Create a list called fruits containing four fruits of your choice
fruits = ["apple", "banana", "mango", "orange"]

# 2. Print the first and the last item using indexes
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")

# 3. .append() a fifth fruit, then print the whole list
fruits.append("pineapple")
print("After appending a fifth fruit:", fruits)

# 4. .remove() one fruit, then print the list again
fruits.remove("banana")
print("After removing one fruit:", fruits)

# 5. Print how many fruits remain using len()
print(f"Number of fruits remaining: {len(fruits)}")