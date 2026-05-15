lucky_numbers= [4, 8, 15, 16, 23, 42, 46]
friends = ["Ayesha", "Zainab", "Noor", "Javeria", "Mahnoor", "Minahil", "Fiza"]
print(friends) #  ["Ayesha", "Zainab", "Noor", "Javeria", "Mahnoor", "Minahil", "Fiza"]
friends.extend(lucky_numbers)
print(friends) # ['Ayesha', 'Zainab', 'Noor', 'Javeria', 'Mahnoor', 'Minahil', 'Fiza', 4, 8, 15, 16, 23, 42, 46]
friends.append("Creed")
print(friends) # ['Ayesha', 'Zainab', 'Noor', 'Javeria', 'Mahnoor', 'Minahil', 'Fiza', 'Creed']
friends.insert(1, "Kelly")
print(friends) # ['Ayesha', 'Kelly', 'Zainab', 'Noor', 'Javeria', 'Mahnoor', 'Minahil', 'Fiza']
friends.remove("Ayesha")
print(friends) # ['Zainab', 'Noor', 'Javeria', 'Mahnoor', 'Minahil', 'Fiza']
friends.clear()
print(friends) # []
friends.pop()
print(friends) #  ['Ayesha', 'Zainab', 'Noor', 'Javeria', 'Mahnoor', 'Minahil']
print(friends.index("Mahnoor")) # 4
# print(friends.index("Mehwish")) # Error
print(friends.count("Mahnoor")) # 1
friends.sort()
print(friends) # ['Ayesha', 'Fiza', 'Javeria', 'Mahnoor', 'Minahil', 'Noor', 'Zainab']
friends.reverse()
print(friends) # ['Fiza', 'Minahil', 'Mahnoor', 'Javeria', 'Noor', 'Zainab', 'Ayesha']
friends2 = friends.copy()
print(friends2)