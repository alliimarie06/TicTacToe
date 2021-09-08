#Allyssa Dalton

'''
Welcome to 2-player Tic-Tac-Toe.
'''

#gives xScore and oScore a value
xScore=0
oScore=0

#prints the start
#gives each place a variable
#prints the starting board
while xScore==10 or oScore==10:
    print("X will go first, O will go second.")
    print("X's player score:", xScore, "O's player score:", oScore)
    s1=str(1)
    s2=str(2)
    s3=str(3)
    s4=str(4)
    s5=str(5)
    s6=str(6)
    s7=str(7)
    s8=str(8)
    s9=str(9)
    print(s1+"|"+s2+"|"+s3)
    print("-"+"|"+"-"+"|"+"-")
    print(s4+"|"+s5+"|"+s6)
    print("-"+"|"+"-"+"|"+"-")
    print(s7+"|"+s8+"|"+s9) 


#asks X for their first turn
#prints the board after their turn
    x1=int(input("What space would you like to place your X?: "))
    if x1==1:
        s1="X"
    elif x1==2:
        s2="X"
    elif x1==3:
        s3="X"
    elif x1==4:
        s4="X"
    elif x1==5:
        s5="X"
    elif x1==6:
        s6="X"
    elif x1==7:
        s7="X"
    elif x1==8:
        s8="X"
    elif x1==9:
        s9="X"
    else:
        print("You submitted an invalid response, you lose your turn.")
    print(s1+"|"+s2+"|"+s3)
    print("-"+"|"+"-"+"|"+"-")
    print(s4+"|"+s5+"|"+s6)
    print("-"+"|"+"-"+"|"+"-")  
    print(s7+"|"+s8+"|"+s9)

#asks O player for their first turn
#prints the board after their turn
    o1=int(input("Where would you like to place your O?: "))
    if o1==x1:
        print("You tried to cheat, you have lost your turn.")
    elif o1==1:
        s1="O"
    elif o1==2:
        s2="O"
    elif o1==3:
        s3="O"
    elif o1==4:
        s4="O"
    elif o1==5:
        s5="O"
    elif o1==6:
        s6="O"
    elif o1==7:
        s7="O"
    elif o1==8:
        s8="O"
    elif o1==9:
        s9="O"
    else:
        print("You submitted an invalid response, you lose your turn.")
    
    print(s1+"|"+s2+"|"+s3)
    print("-"+"|"+"-"+"|"+"-")
    print(s4+"|"+s5+"|"+s6)
    print("-"+"|"+"-"+"|"+"-")
    print(s7+"|"+s8+"|"+s9)
    
#asks x player for their second turn
#prints the board after their turn
    x2=int(input("What space would you like to place your X?: "))
    if x2==o1:
        print("You tried to cheat. You have lost your turn.")
    elif x2==1:
        s1="X"
    elif x2==2:
        s2="X"
    elif x2==3:
        s3="X"
    elif x2==4:
        s4="X"
    elif x2==5:
        s5="X"
    elif x2==6:
        s6="X"
    elif x2==7:
        s7="X"
    elif x2==8:
        s8="X"
    elif x2==9:
        s9="X"
    else:
        print("You submitted an invalid response, you lose your turn.")
    print(s1+"|"+s2+"|"+s3)
    print("-"+"|"+"-"+"|"+"-")
    print(s4+"|"+s5+"|"+s6)
    print("-"+"|"+"-"+"|"+"-")
    print(s7+"|"+s8+"|"+s9)
    
#asks o player for their second turn
#prints the board after their turn
    o2=int(input("Where would you like to place your O?: "))
    if o2==x1 or o2==x2:
        print("You tried to cheat, you have lost your turn.")
    elif o2==1:
        s1="O"
    elif o2==2:
        s2="O"
    elif o2==3:
        s3="O"
    elif o2==4:
        s4="O"
    elif o2==5:
        s5="O"
    elif o2==6:
        s6="O"
    elif o2==7:
        s7="O"
    elif o2==8:
        s8="O"
    elif o2==9:
        s9="O"
    else:
        print("You submitted an invalid response, you lose your turn.")
    
    print(s1+"|"+s2+"|"+s3)
    print("-"+"|"+"-"+"|"+"-")
    print(s4+"|"+s5+"|"+s6)
    print("-"+"|"+"-"+"|"+"-")
    print(s7+"|"+s8+"|"+s9)

#asks x player for their third turn
#prints the board after their turn
#prints they won, if they win 
    x3=int(input("What space would you like to place your X?: "))
    if x3==o1 or x3==o2:
        print("You tried to cheat. You have lost your turn.")
    elif x3==1:
        s1="X"
    elif x3==2:
        s2="X"
    elif x3==3:
        s3="X"
    elif x3==4:
        s4="X"
    elif x3==5:
        s5="X"
    elif x3==6:
        s6="X"
    elif x3==7:
        s7="X"
    elif x3==8:
        s8="X"
    elif x3==9:
        s9="X"
    else:
        print("You submitted an invalid response, you lose your turn.")
    
    print(s1+"|"+s2+"|"+s3)
    print("-"+"|"+"-"+"|"+"-")
    print(s4+"|"+s5+"|"+s6)
    print("-"+"|"+"-"+"|"+"-")
    print(s7+"|"+s8+"|"+s9)

    if s1=="X" and s2=="X" and s3=="X":
        print("X player won! Good job!")
        xScore=xScore+1
        continue
    elif s4=="X" and s5=="X" and s6=="X":
            print("X player won! Good job!")
            xScore=xScore+1
            continue
    elif s7=="X" and s8=="X" and s9=="X":
            print("X player won! Good job!")
            xScore=xScore+1
            continue
    elif s1=="X" and s5=="X" and s6=="X":
            print("X player won! Good job!")
            xScore=xScore+1
            continue
    elif s3=="X" and s5=="X" and s7=="X":
            print("X player won! Good job!")
            xScore=xScore+1
            continue
    elif s1=="X" and s4=="X" and s7=="X":
            print("X player won! Good job!")
            xScore=xScore+1
            continue 
    elif s2=="X" and s5=="X" and s8=="X":
            print("X player won! Good job!")
            xScore=xScore+1
            continue
    elif s3=="X" and s6=="X" and s9=="X":
            print("X player won! Good job!")        
            xScore=xScore+1
            continue
#asks o player for their third turn
#prints the board after their turn
#prints they won, if they win
    o3=int(input("Where would you like to place your O?: "))
    if o3==x1 or o3==x2 or o3==x3:
        print("You tried to cheat, you have lost your turn.")
    elif o3==1:
        s1="O"
    elif o3==2:
        s2="O"
    elif o3==3:
        s3="O"
    elif o3==4:
        s4="O"
    elif o3==5:
        s5="O"
    elif o3==6:
        s6="O"
    elif o3==7:
        s7="O"
    elif o3==8:
        s8="O"
    elif o3==9:
        s9="O"
    else:
        print("You submitted an invalid response, you lose your turn.") 

    print(s1+"|"+s2+"|"+s3)
    print("-"+"|"+"-"+"|"+"-")
    print(s4+"|"+s5+"|"+s6)
    print("-"+"|"+"-"+"|"+"-")
    print(s7+"|"+s8+"|"+s9)
    
    if s1=="O" and s2=="O" and s3=="O":
        print("O player won! Good job!")
        oScore=oScore+1
        continue
    elif s4=="O" and s5=="O" and s6=="O":
        print("O player won! Good job!")
        oScore=oScore+1
        continue
    elif s7=="O" and s8=="O" and s9=="O":
        print("O player won! Good job!")
        oScore=oScore+1
        continue
    elif s1=="O" and s5=="O" and s6=="O":
            print("O player won! Good job!")
            oScore=oScore+1
            continue
    elif s3=="O" and s5=="O" and s7=="O":
            print("O player won! Good job!")
            oScore=oScore+1
            continue
    elif s1=="O" and s4=="O" and s7=="O":
            print("O player won! Good job!")
            oScore=oScore+1
            continue
    elif s2=="O" and s5=="O" and s8=="O":
            print("O player won! Good job!")
            
    elif s3=="O" and s6=="O" and s9=="O":
            print("O player won! Good job!")
            oScore=oScore+1
            continue
    
#asks x player for their fourth turn
#prints the board after their turn
#prints they won, if they win
    x4=int(input("What space would you like to place your X?: "))
    if x4==o1 or x4==o2 or x4==o3:
        print("You tried to cheat. You have lost your turn.")
    elif x4==1:
        s1="X"
    elif x4==2:
        s2="X"
    elif x4==3:
        s3="X"
    elif x4==4:
        s4="X"
    elif x4==5:
        s5="X"
    elif x4==6:
        s6="X"
    elif x4==7:
        s7="X"
    elif x4==8:
        s8="X"
    elif x4==9:
        s9="X"
    else:
        print("You submitted an invalid response, you lose your turn.")
    
    print(s1+"|"+s2+"|"+s3)
    print("-"+"|"+"-"+"|"+"-")
    print(s4+"|"+s5+"|"+s6)
    print("-"+"|"+"-"+"|"+"-")
    print(s7+"|"+s8+"|"+s9)
    
    if s1=="X" and s2=="X" and s3=="X":
        print("X player won! Good job!")
        xScore=xScore+1
        continue
    elif s4=="X" and s5=="X" and s6=="X":
        print("X player won! Good job!")
        xScore=xScore+1
        continue
    elif s7=="X" and s8=="X" and s9=="X":
        print("X player won! Good job!")
        xScore=xScore+1
        continue
    elif s1=="X" and s5=="X" and s6=="X":
        print("X player won! Good job!")
        xScore=xScore+1
        continue
    elif s3=="X" and s5=="X" and s7=="X":
        print("X player won! Good job!")
        xScore=xScore+1
        continue
    elif s1=="X" and s4=="X" and s7=="X":
        print("X player won! Good job!")
        xScore=xScore+1
        continue
    elif s2=="X" and s5=="X" and s8=="X":
        print("X player won! Good job!")
        xScore=xScore+1
        continue
    elif s3=="X" and s6=="X" and s9=="X":
        print("X player won! Good job!")
        xScore=xScore+1
        continue

#asks o player for their fourth turn 
#prints the board after their turn
#prints they won, if they win
    o4=int(input("Where would you like to place your O?: "))
    if o4==x1 or o4==x2 or o4==x3 or o4==x4:
        print("You tried to cheat, you have lost your turn.")
    elif o4==1:
        s1="O"
    elif o4==2:
        s2="O"
    elif o4==3:
        s3="O"
    elif o4==4:
        s4="O"
    elif o4==5:
        s5="O"
    elif o4==6:
        s6="O"
    elif o4==7:
        s7="O"
    elif o4==8:
        s8="O"
    elif o4==9:
        s9="O"
    else:
        print("You submitted an invalid response, you lose your turn.")

    print(s1+"|"+s2+"|"+s3)
    print("-"+"|"+"-"+"|"+"-")
    print(s4+"|"+s5+"|"+s6)
    print("-"+"|"+"-"+"|"+"-")
    print(s7+"|"+s8+"|"+s9)

    if s1=="O" and s2=="O" and s3=="O":
        print("O player won! Good job!")
        oScore=oScore+1
        continue
    elif s4=="O" and s5=="O" and s6=="O":
        print("O player won! Good job!")
        oScore=oScore+1
        continue
    elif s7=="O" and s8=="O" and s9=="O":
        print("O player won! Good job!")
        oScore=oScore+1
        continue
    elif s1=="O" and s5=="O" and s6=="O":
        print("O player won! Good job!")
        oScore=oScore+1
        continue
    elif s3=="O" and s5=="O" and s7=="O":
        print("O player won! Good job!")
        oScore=oScore+1
        continue
    elif s1=="O" and s4=="O" and s7=="O":
        print("O player won! Good job!")
        oScore=oScore+1
        continue
    elif s2=="O" and s5=="O" and s8=="O":
        print("O player won! Good job!")
        oScore=oScore+1
        continue
    elif s3=="O" and s6=="O" and s9=="O":
        print("O player won! Good job!")
        oScore=oScore+1
        continue
        
#asks x player for their fifth turn
#prints the board after their turn
#prints they won, if they win
    x5=int(input("What space would you like to place your X?: "))
    if x5==o1 or x5==o2 or x5==o3 or x5==o4:
        print("You tried to cheat. You have lost your turn.")
    elif x5==1:
        s1="X"
    elif x5==2:
        s2="X"
    elif x5==3:
        s3="X"
    elif x5==4:
        s4="X"
    elif x5==5:
        s5="X"
    elif x5==6:
        s6="X"
    elif x5==7:
        s7="X"
    elif x5==8:
        s8="X"
    elif x5==9:
        s9="X"
    else:
        print("You submitted an invalid response, you lose your turn.")
    
    print(s1+"|"+s2+"|"+s3)
    print("-"+"|"+"-"+"|"+"-")
    print(s4+"|"+s5+"|"+s6)
    print("-"+"|"+"-"+"|"+"-")
    print(s7+"|"+s8+"|"+s9)
    
    if s1=="X" and s2=="X" and s3=="X":
        print("X player won! Good job!")
        xScore=xScore+1
        continue
    elif s4=="X" and s5=="X" and s6=="X":
       print("X player won! Good job!")
       xScore=xScore+1
       continue
    elif s7=="X" and s8=="X" and s9=="X":
        print("X player won! Good job!")
        xScore=xScore+1
        continue
    elif s1=="X" and s5=="X" and s6=="X":
        print("X player won! Good job!")
        xScore=xScore+1
        continue
    elif s3=="X" and s5=="X" and s7=="X":
        print("X player won! Good job!")
        xScore=xScore+1
        continue
    elif s1=="X" and s4=="X" and s7=="X":
        print("X player won! Good job!")
        xScore=xScore+1
        continue
    elif s2=="X" and s5=="X" and s8=="X":
        print("X player won! Good job!")
        xScore=xScore+1
        continue
    elif s3=="X" and s6=="X" and s9=="X":
        print("X player won! Good job!")
        xScore=xScore+1
        continue

#asks o player for their fifth turn
#prints the board after their turn
#prints they won, if they win
    o5=int(input("Where would you like to place your O?: "))
    if o5==x1 or o5==x2 or o5==x3 or o5==x4 or o5==x5:
        print("You tried to cheat, you have lost your turn.")
    elif o5==1:
        s1="O"
    elif o5==2:
        s2="O"
    elif o5==3:
            s3="O"
    elif o5==4:
        s4="O"
    elif o5==5:
        s5="O"
    elif o5==6:
        s6="O"
    elif o5==7:
        s7="O"
    elif o5==8:
        s8="O"
    elif o5==9:
        s9="O"
    else:
        print("You submitted an invalid response, you lose your turn.")

    print(s1+"|"+s2+"|"+s3)
    print("-"+"|"+"-"+"|"+"-")
    print(s4+"|"+s5+"|"+s6)
    print("-"+"|"+"-"+"|"+"-")
    print(s7+"|"+s8+"|"+s9)

    if s1=="O" and s2=="O" and s3=="O":
        print("O player won! Good job!")
        oScore=oScore+1
        continue
    elif s4=="O" and s5=="O" and s6=="O":
        print("O player won! Good job!")
        oScore=oScore+1
        continue
    elif s7=="O" and s8=="O" and s9=="O":
        print("O player won! Good job!")
        oScore=oScore+1
        continue
    elif s1=="O" and s5=="O" and s6=="O":
        print("O player won! Good job!")
        oScore=oScore+1
        continue
    elif s3=="O" and s5=="O" and s7=="O":
        print("O player won! Good job!")
        oScore=oScore+1
        continue
    elif s1=="O" and s4=="O" and s7=="O":
        print("O player won! Good job!")
        oScore=oScore+1
        continue
    elif s2=="O" and s5=="O" and s8=="O":
        print("O player won! Good job!")
        oScore=oScore+1
        continue
    elif s3=="O" and s6=="O" and s9=="O":
        print("O player won! Good job!")
        oScore=oScore+1
        continue

#asks x player for their sixth turn
#prints the board after their turn
#prints they won, if they win
    x6=int(input("What space would you like to place your X?: "))
    if x6==o1 or x6==o2 or x6==o3 or x6==o4 or x6==o5:
        print("You tried to cheat. You have lost your turn.")
    elif x6==1:
        s1="X"
    elif x6==2:
        s2="X"
    elif x6==3:
        s3="X"
    elif x6==4:
        s4="X"
    elif x6==5:
        s5="X"
    elif x6==6:
        s6="X"
    elif x6==7:
        s7="X"
    elif x6==8:
        s8="X"
    elif x6==9:
        s9="X"
    else:
        print("You submitted an invalid response, you lose your turn.")
    
    print(s1+"|"+s2+"|"+s3)
    print("-"+"|"+"-"+"|"+"-")
    print(s4+"|"+s5+"|"+s6)
    print("-"+"|"+"-"+"|"+"-")
    print(s7+"|"+s8+"|"+s9) 

    if s1=="X" and s2=="X" and s3=="X":
        print("X player won! Good job!")
        xScore=xScore+1
        continue
    elif s4=="X" and s5=="X" and s6=="X":
        print("X player won! Good job!")
        xScore=xScore+1
        continue
    elif s7=="X" and s8=="X" and s9=="X":
        print("X player won! Good job!")
        xScore=xScore+1
        continue
    elif s1=="X" and s5=="X" and s6=="X":
        print("X player won! Good job!")
        xScore=xScore+1
        continue
    elif s3=="X" and s5=="X" and s7=="X":
        print("X player won! Good job!")
        xScore=xScore+1
        continue
    elif s1=="X" and s4=="X" and s7=="X":
        print("X player won! Good job!")
        xScore=xScore+1
        continue
    elif s2=="X" and s5=="X" and s8=="X":
        print("X player won! Good job!")
        xScore=xScore+1
        continue
    elif s3=="X" and s6=="X" and s9=="X":
        print("X player won! Good job!")
        xScore=xScore+1
        continue
