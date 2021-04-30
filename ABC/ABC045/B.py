sa = input()
sb = input()
sc = input()
 
turn = "a"
while True:
    if turn == "a":
        turn = sa[:1]
        if len(sa) == 0:
            print("A")
            break
        else:
            sa = sa[1:]
    elif turn == "b":
        turn = sb[:1]