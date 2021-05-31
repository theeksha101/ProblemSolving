start_house, end_house = map(int, input().split())
left_tree, right_tree = map(int, input().split())
number_of_apples, number_of_oranges = map(int, input().split())
apple_distances = map(int, input().split())
orange_distances = map(int, input().split())
apple_count = 0
orange_count = 0

for distance in apple_distances:
    if start_house <= left_tree + distance <= end_house:
        apple_count += 1
for distance in orange_distances:
    if start_house <= right_tree + distance <= end_house:
        orange_count += 1
print(apple_count)
print(orange_count)
