for row in range(1,5):
    for col in range(1,8):
        if(row+col==5)|(row==4)|(col-row==3):
            print("*",end="")
        else:
            print(end=" ")
    print()