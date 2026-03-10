import random as r
import sys
def check_update(abc3,text_contents2,abc2):
    z=0
    if len(abc3)==1:
        for index,i in enumerate( text_contents2):
            if abc3.lower()==i.lower():
                #print ("match")
                z=1
                abc2=abc2[:index]+i+abc2[index+1:]
            #else:
                #print ("No match")
        print(abc2)
        list1=[]
        if z==0:
            list1 = [abc2, False]
            return list1
        else:
            list1 = [abc2, True]
            return list1
    else:
        print("Invalid input")
        sys.exit()
print("Enter\n 1 for \"Animals\"\n 2 for \"places:both countries and cities\"\n 3 for places on in INDIA \n 5 or any other number for general play\n")
left=0
already=0
catagory=int(input())
match catagory:
    case 1:
        file = 'input1_game.txt'
        file2 = "description1.txt"
    case 2:
        file = "input2_game.txt"
        file2 = "description2.txt"
    case 3:
        file = "input3_game.txt"
        file2 = "description3.txt"
    case 5:
        file="input5_game.txt"
        file2 = "description5.txt"

f= open(file,'r')
#for i in
#print(f.readline())
#print(f.read())
store=0
lines = [line.strip() for line in f.readlines()]
print(lines)
store = r.randint(0, len(lines) - 1)
text_contents=lines[store]
f.seek(0)
"""for index,i in enumerate(f):
    if i==text_contents:
        store=index
        break"""
f.close()
current_line=0
#line_number=(store+store)
f= open(file2,'r')
lines2 = f.readlines()
updated_lines2=[]
updated_lines2=[line for line in lines2 if line.strip() !=""]
print(updated_lines2)
description_content = updated_lines2[store]
"""while current_line < line_number:
   # f.readline()
  #  current_line += 2
#print (description_content.replace(text_contents,"It"))
#description_content = (f.readline())
#print (description_content.replace(text_contents,"It"))
#print"""
f.close()
k = len(text_contents)
abc2=""
for i in text_contents:
    if i==" ":
        abc2=abc2+" "
    else:
        abc2 = abc2 + "_"
diff_easy_hard=int(input("Enter 1 for normal play; with hints,\nEnter 2 for easy play"))
match diff_easy_hard:
    case 1:
        already=0
    case 2:
        already=1
        z = description_content.find(":")
        updated_description = description_content[z + 2:]  # Get content after ':'

        # Replace occurrences of text_contents with "It"
        updated_description = updated_description.replace(text_contents, "It")

        # Handle the case where the first letter is uppercase
        upper = text_contents.capitalize()  # Capitalize the first letter
        updated_description = updated_description.replace(upper, "It")

        # Handle the case where the first letter is lowercase
        lower = text_contents.lower()  # Ensure the first letter is lowercase
        updated_description = updated_description.replace(lower, "It")

        print(updated_description)

print(abc2)
"""#print("Starting the game\n")
#word=check_update(abc,text_contents,abc2)
#update1=""
#print ("word",w)"""
w=abc2
lifeline=5
st_all=""
while(lifeline>=0):
    t=0
    abc = input("Enter guess\n")
    for j in st_all:
        if abc.lower() == j.lower():
            print("You entered same character second time")
            t=1
    if t==1:
            continue
    if not st_all:
        st_all=st_all+" "+abc
    else:
        st_all=st_all+","+abc
    left=0

    #w=""

    for i in w:
         if i == "_":
             #print (i)
             left+=1
    if left>0:
            word=check_update(abc,text_contents,w)
            w=""
            w=word[0]
    elif(left<1):
        print("You won")
        break
    print("all the guessed letters are",st_all)
    if (word[1] == False):
        lifeline -= 1
    print("Number of lifelines left ", lifeline)
    if(lifeline==0):
        print("You lost")
        print("The original answer is", text_contents)
        break
if already:
    pass
else:
    print(description_content)