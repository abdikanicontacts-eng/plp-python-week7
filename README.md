# Shopping List Manager (PLP Python Week 7)

## File Descriptions
* `list_warmup.py`: Demonstrates basic list operations including index access, appending items, removing items, and checking length with `len()`.
* `shopping_list.py`: An interactive command-line shopping list manager allowing users to add, remove (with membership validation), display, and exit gracefully.
* `list_report.py`: Generates a summary report from a list, featuring numbered output, character length filtering, and programmatic detection of the longest string.

## Why is it safer to check `in` before calling `.remove()`?
Checking whether an item exists in a list using the `in` keyword before calling `.remove()` prevents the program from crashing with a `ValueError`. If you attempt to remove an item that is not present, Python raises an unhandled exception and stops execution. Using a conditional check ensures the program handles unexpected input smoothly and presents a friendly warning message to the user instead.