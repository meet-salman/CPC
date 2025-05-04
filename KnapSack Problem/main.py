## list of items
# loi = [[4, 8], [0, 9], [1, 1], [9, 0], [6, 3]]

loi = []
n = int(input("Enter number of items: "))
null = True

## Input all items
print ("Enter weight and price separated by space: ")
for i in range(n):
    item = list(map(int, input(f"Item {i+1}: ", ).split()))
    loi.append(item)

    ## Validate if all items w = p =0
    if (item[0] != 0 or item[1] != 0):
        null = False

    ## Exit if all items w < 0 > p
    if (item[0] < 0 or item[1] < 0):
        print("Weight or price can't be negative.")
        exit()

## Exit if all items w = p = 0
if (null):
    print("No wiegth and price in items.")
    exit()


## Best items
best_items = [] 

## Best items total weight and price
best_wp = [0, -1]

bag_capacity = int(input("Enter bag capacity: "))

## Exit, if bag capacity = 0
if (bag_capacity <= 0):
    print("Bag capacity must be greater than zero!")
    exit()

## Generating all combinations of items
subsets = [[]]
for element in loi:
    subsets += [subset + [element] for subset in subsets] 

## Finding best possible combination 
for subset in subsets:
    w = p = 0
    for e in subset:
        w += e[0]
        p += e[1]

    ## Select combination, if best
    if w < bag_capacity and p > best_wp[1]:
        best_wp = [w, p]
        best_items = subset

## Show: if there are best_items, else message
if (best_items):
    print(best_items)
    print(best_wp)
else:
    print("No items can be added to the bag.")
