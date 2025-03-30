#create an empty list
fruits = []
fruits = list()

#elements
fruits = ["apple", "banana", "oragne", "kiwi", "berry", "mango"]
print(fruits)
print(fruits[4])

#add element
fruits.append("melon")
print(fruits)

#add element at specific position example 2nd position
fruits.insert(2,"pineapple")
print(fruits)

#remove element
fruits.remove("apple")
print(fruits)

#remove last element
fruits.pop()
print(fruits)

#sort elements in a list in ascending order
fruits.sort()
print(fruits)

#count elements
print(len(fruits))

#iterate through list of fruits and print each fruit
for fruit in fruits:
    print(fruit)

#class exercise 1
scoresOG = [15, 19, 17, 12, 17, 13]
scores = scoresOG.copy()
print(scores)
#print first score
print(scores[1])
#print last score
print(scores[5])
#print higest score
print(max(scores))
#print lowest scoer
print(min(scores))
#add 21 to the list
scores.append(21)
#sort the scores in increasing order
scores.sort()
print(scores)
#sort the scores in decreasing order
scores.sort(reverse = True )
print(scores)
#remove one of the number 17
scores.remove(17)
scores.pop(2)
print(scores)
print(scoresOG)
#iterate over the list of scores and calculates the total score by summing up all the scores
total_score = 0
for score in scores:
    total_score += score
    #total_score = total_score + score
    # 0 = 0 +15
    # 15 = 15 + 19
print("Total score:", total_score)

#find square to