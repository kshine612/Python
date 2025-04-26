#sort tuples in descneding order by price
import operator
food = [["Pizza",320],[ "Garlic bread",420],["Pasta",200], ["Noodles",150], ["Vada pav",20], ["Dabeli",25]]
print(sorted(food, key=operator.itemgetter(1)))
    
