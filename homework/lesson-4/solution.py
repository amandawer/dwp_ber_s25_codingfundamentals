#Exercise 0
#1. goes through each number in the list

sscores = [5, 6, 6, 13, 6, 16, 2, 4, 6, 15, 3, 7, 20, 3, 24, 24, 1, 23, 3, 3, 3, 21, 7, 2, 12]
print(len(scores)) 

#Exercise 1

count_threes = scores.count(3)
print(count_threes)

#Exercise 2

max_score = max(scores)
print(max_score) 

#Exercise 3

list_1 = ["foo", 2, "bar", 3, "baz", "spam", 4]
list_2 = ["1", 2, "3", 3, "4", "foo", "pasm", "bar"]

common = [element for element in list_1 if element in list_2]
print(common)

#Exercise 4

all_numbers = [111, 32, -9, -45, -17, 9, 85, -10]
positive_numbers = [num for num in all_numbers if num > 0]
print(positive_numbers)

#Exercise 5

reverse_this_list = [10, 20, 30, 40, 50]
print(reverse_this_list[::-1])

#Exercise 6

unique_scores = set(scores)
print(unique_scores)

#Exercise 7

countries_and_capitals = [
    ("Germany", "Berlin"),
    ("France", "Paris"),
    ("Japan", "Tokyo"),
    ("Brazil", "Brasília"),
    ("Guatemala", "Guatemala City")
]
print(countries_and_capitals)


