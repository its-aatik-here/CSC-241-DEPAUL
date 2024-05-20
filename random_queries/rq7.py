import code 
# for num in range (0,10):
#     print(num,end = " ")


# for value in range (0,2):
#     print (num,end = " ")

# for siuuu in range (3,13):
#     print (siuuu,end = " ")


# for num in range (0,9,2):
#     print(num,end = " ")

# for num in range (0,24,3):
#     print(num,end = " ")

# for num in range (3,12,5):
#     print(num,end = " ")

# count = 0
# for num in range (5,25,2):
#     count += 1
#     print(num,end = " ")
# print ()
# print(count,end = " ")


# num = 2
# while num < 12:
#     num += 1
#     print(num,end = " ")

# total = 0
# for num in range (1,6):
#     total += num
# print (total)

# for x in range (6,-2,-1):
#     print(x,end = " ")

# num=30
# while num >4:
#     print(num)
#     num = num/2

# for x in range (11,-4,-2):
#     print (x,end=" ")

# total = 0
# for num in range (1,15):
#     total = total + num
# print (total)

# total=0
# num = 0
# while num < 15:
#     total = total + num
#     num = num + 1
# print (f"the sum is = {total}")


def countLetters(text):
    count=0
    for char in text:
        if char.isalnum():
            count += 1
    print (count)

code.interact(local=dict(globals(), **locals()))