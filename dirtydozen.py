row1=["◻","◻","◻"]
row2=["◻","◻","◻"]
row3=["◻","◻","◻"]
maps=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
treasure_place=input("Where do you want to place the treasure? ")
horizontal=int(treasure_place[0])
vertical=int(treasure_place[1])
#print(horizontal)
#print(vertical)
#print(maps[horizontal][vertical])
maps[vertical-1][horizontal-1]='X'
print(f"{row1}\n{row2}\n{row3}")