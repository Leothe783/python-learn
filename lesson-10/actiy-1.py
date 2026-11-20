# 1) Ask the user to enter a word and store it in `string`.
string=input('enter a word')
# 2) Ask the user to enter a single character and store it in `char`.
char=input('enter a character')
# 3) Set `i` to 0.
#    (This will be used as the index to move through the string.)
i=0
count=0
# 4) Set `count` to 0.
#    (This will store how many times `char` appears.)

# 5) While `i` is less than the length of `string`:
while i<len(string):
    if string[i]==char:
      count+=1
      
    i=i+1
print('total nuber of times',char,'as occurred',count)  
#    a) Check if the character at position `i` in `string` is equal to `char`.
#    b) If yes, increase `count` by 1.
#    c) Increase `i` by 1 to move to the next character.

# 6) After the loop, print how many times `char` occurred in `string` using `count`.