row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map1 = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = (input("Where do you want to put the treasure? First digit for column, second digit for row.\n"))

column = int(position[0])-1
row = int(position[1])-1

hazine= map1[row][column]="X"
print(f"{row1}\n{row2}\n{row3}")