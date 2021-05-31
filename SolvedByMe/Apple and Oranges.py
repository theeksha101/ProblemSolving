def countApplesAndOranges(source_house, destination_house,
                          location_apple_tree, location_orange_tree,
                          dist_apple_fall, dist_oranges_fall):
    count_apples = 0
    count_oranges = 0
    apple_fell_position = [i + location_apple_tree for i in dist_apple_fall]
    orange_fell_position = [j + location_orange_tree for j in dist_oranges_fall]

    for apple in apple_fell_position:
        if apple in range(source_house, destination_house + 1):
            count_apples += 1
    print(count_apples)

    for orange in orange_fell_position:
        if orange in range(source_house, destination_house + 1):
            count_oranges += 1
    print(count_oranges)


countApplesAndOranges(2, 3, 1, 5, [2], [-2])
