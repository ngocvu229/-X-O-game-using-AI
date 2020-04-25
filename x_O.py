import random

def play_game():
    print("""   
    Welcome to the X_O game

You are fighting against Nguyen Ngoc Vu

     
Please select a mode:

1_ you fight first

2_ Vu Nguyen first

""")
    while True:
        try:
            select = int(input("Selection : "))
        except:
            print("Please enter a number ! ")
        else:
            if select == 1 or select == 2:
                break

    print("=================")
    print("_________________")
    print(" ", 0, " | ", 1, " | ", 2)
    print("=================")
    print(" ", 3, " | ", 4, " | ", 5)
    print("=================")
    print(" ", 6, " | ", 7, " | ", 8)
    print("_________________")
    print("=================\n")


    list_game = [" "," "," "," "," "," "," "," "," "]
    def print_border():
        print(" ",list_game[0]," | ",list_game[1]," | ",list_game[2])
        print("=================")
        print(" ",list_game[3]," | ",list_game[4]," | ",list_game[5])
        print("=================")
        print(" ",list_game[6]," | ",list_game[7]," | ",list_game[8])



    def player():
        while True:
            x = input("Nhập ô bạn muốn đánh : ")
            if x :
                if int(x) <= 8 and int(x) >= 0:
                    if check_o(int(x)):
                        list_game[int(x)] = "x"
                        break

    def com():
        while True:
            o = random.randint(0,8)
            if list_game[4] == " ":
                o = 4
                break

            elif list_game[0] == list_game[1] and list_game[0] == "o" and list_game[2] == " ":
                o = 2
                break
            elif list_game[1] == list_game[2] and list_game[1] == "o" and list_game[0] == " ":
                o = 0
                break
            elif list_game[0] == list_game[2] and list_game[0] == "o" and list_game[1] == " ":
                o = 1
                break
            elif list_game[3] == list_game[4] and list_game[3] == "o" and list_game[5] == " ":
                o = 5
                break
            elif list_game[3] == list_game[5] and list_game[3] == "o" and list_game[4] == " ":
                o = 4
                break
            elif list_game[4] == list_game[5] and list_game[4] == "o" and list_game[3] == " ":
                o = 3
                break
            elif list_game[6] == list_game[7] and list_game[6] == "o" and list_game[8] == " ":
                o = 8
                break
            elif list_game[6] == list_game[8] and list_game[6] == "o" and list_game[7] == " ":
                o = 7
                break
            elif list_game[7] == list_game[8] and list_game[7] == "o" and list_game[6] == " ":
                o = 6
                break
            elif list_game[0] == list_game[3] and list_game[0] == "o" and list_game[6] == " ":
                o = 6
                break
            elif list_game[0] == list_game[6] and list_game[0] == "o" and list_game[3] == " ":
                o = 3
                break
            elif list_game[3] == list_game[6] and list_game[3] == "o" and list_game[0] == " ":
                o = 0
                break
            elif list_game[1] == list_game[4] and list_game[1] == "o" and list_game[7] == " ":
                o = 7
                break
            elif list_game[1] == list_game[7] and list_game[1] == "o" and list_game[4] == " ":
                o = 4
                break
            elif list_game[4] == list_game[7] and list_game[4] == "o" and list_game[1] == " ":
                o = 1
                break
            elif list_game[2] == list_game[5] and list_game[2] == "o" and list_game[8] == " ":
                o = 8
                break
            elif list_game[2] == list_game[8] and list_game[2] == "o" and list_game[5] == " ":
                o = 5
                break
            elif list_game[5] == list_game[8] and list_game[2] == "o" and list_game[2] == " ":
                o = 2
                break
            elif list_game[0] == list_game[4] and list_game[0] == "o" and list_game[8] == " ":
                o = 8
                break
            elif list_game[0] == list_game[8] and list_game[0] == "o" and list_game[4] == " ":
                o = 4
                break
            elif list_game[4] == list_game[8] and list_game[4] == "o" and list_game[0] == " ":
                o = 0
                break
            elif list_game[2] == list_game[4] and list_game[2] == "o" and list_game[6] == " ":
                o = 6
                break
            elif list_game[2] == list_game[6] and list_game[2] == "o" and list_game[4] == " ":
                o = 4
                break
            elif list_game[4] == list_game[6] and list_game[4] == "o" and list_game[2] == " ":
                o = 2
                break
            elif list_game[1] == list_game[3] and list_game[1] == "o" and list_game[0] == " ":
                o = 0
                break
            elif list_game[1] == list_game[5] and list_game[1] == "o" and list_game[2] == " ":
                o = 2
                break
            elif list_game[3] == list_game[7] and list_game[3] == "o" and list_game[6] == " ":
                o = 6
                break
            elif list_game[5] == list_game[7] and list_game[5] == "o" and list_game[8] == " ":
                o = 8
                break
            #########
            elif list_game[0] == list_game[1] and list_game[0] == "x" and list_game[2] == " ":
                o = 2
                break
            elif list_game[1] == list_game[2] and list_game[1] == "x" and list_game[0] == " ":
                o = 0
                break
            elif list_game[0] == list_game[2] and list_game[0] == "x" and list_game[1] == " ":
                o = 1
                break
            elif list_game[3] == list_game[4] and list_game[3] == "x" and list_game[5] == " ":
                o = 5
                break
            elif list_game[3] == list_game[5] and list_game[3] == "x" and list_game[4] == " ":
                o = 4
                break
            elif list_game[4] == list_game[5] and list_game[4] == "x" and list_game[3] == " ":
                o = 3
                break
            elif list_game[6] == list_game[7] and list_game[6] == "x" and list_game[8] == " ":
                o = 8
                break
            elif list_game[6] == list_game[8] and list_game[6] == "x" and list_game[7] == " ":
                o = 7
                break
            elif list_game[7] == list_game[8] and list_game[7] == "x" and list_game[6] == " ":
                o = 6
                break
            elif list_game[0] == list_game[3] and list_game[0] == "x" and list_game[6] == " ":
                o = 6
                break
            elif list_game[0] == list_game[6] and list_game[0] == "x" and list_game[3] == " ":
                o = 3
                break
            elif list_game[3] == list_game[6] and list_game[3] == "x" and list_game[0] == " ":
                o = 0
                break
            elif list_game[1] == list_game[4] and list_game[1] == "x" and list_game[7] == " ":
                o = 7
                break
            elif list_game[1] == list_game[7] and list_game[1] == "x" and list_game[4] == " ":
                o = 4
                break
            elif list_game[4] == list_game[7] and list_game[4] == "x" and list_game[1] == " ":
                o = 1
                break
            elif list_game[2] == list_game[5] and list_game[2] == "x" and list_game[8] == " ":
                o = 8
                break
            elif list_game[2] == list_game[8] and list_game[2] == "x" and list_game[5] == " ":
                o = 5
                break
            elif list_game[5] == list_game[8] and list_game[2] == "x" and list_game[2] == " ":
                o = 2
                break
            elif list_game[0] == list_game[4] and list_game[0] == "x" and list_game[8] == " ":
                o = 8
                break
            elif list_game[0] == list_game[8] and list_game[0] == "x" and list_game[4] == " ":
                o = 4
                break
            elif list_game[4] == list_game[8] and list_game[4] == "x" and list_game[0] == " ":
                o = 0
                break
            elif list_game[2] == list_game[4] and list_game[2] == "x" and list_game[6] == " ":
                o = 6
                break
            elif list_game[2] == list_game[6] and list_game[2] == "x" and list_game[4] == " ":
                o = 4
                break
            elif list_game[4] == list_game[6] and list_game[4] == "x" and list_game[2] == " ":
                o = 2
                break
            elif list_game[1] == list_game[3] and list_game[1] == "x" and list_game[0] == " ":
                o = 0
                break
            elif list_game[1] == list_game[5] and list_game[1] == "x" and list_game[2] == " ":
                o = 2
                break
            elif list_game[3] == list_game[7] and list_game[3] == "x" and list_game[6] == " ":
                o = 6
                break
            elif list_game[5] == list_game[7] and list_game[5] == "x" and list_game[8] == " ":
                o = 8
                break
            elif list_game[4] != " " and (list_game[0] == " " or list_game[2] == " " or list_game[6] == " " or list_game[8] == " " ):
                c=0
                a = random.sample([6, 0, 2, 8],4)
                for i in range(5):
                    if list_game[a[i]] != "x" and list_game[a[i]] != "o":
                        o = a[i]
                        break
                break
            else:
                if list_game[o] == " ":
                    break
        list_game[o] = "o"

    def check_o(n):
        if list_game[n] != " ":
            print("chỗ này đã được đánh, chọn ô khác.")
            return  False
        return True

    def check_game():
        if list_game[0] == list_game[1] and list_game[1] == list_game[2]:
            win_game(list_game[0])
            if list_game[0] != " ":
                return True
        elif list_game[3] == list_game[4] and list_game[4] == list_game[5]:
            win_game(list_game[3])
            if list_game[3] != " ":
                return True
        elif list_game[6] == list_game[7] and list_game[7] == list_game[8]:
            win_game(list_game[6])
            if list_game[6] != " ":
                return True
        elif list_game[0] == list_game[3] and list_game[3] == list_game[6]:
            win_game(list_game[0])
            if list_game[0] != " ":
                return True
        elif list_game[1] == list_game[4] and list_game[4] == list_game[7]:
            win_game(list_game[1])
            if list_game[1] != " ":
                return True
        elif list_game[2] == list_game[5] and list_game[5] == list_game[8]:
            win_game(list_game[2])
            if list_game[2] != " ":
                return True
        elif list_game[0] == list_game[4] and list_game[4] == list_game[8]:
            win_game(list_game[0])
            if list_game[0] != " ":
                return True
        elif list_game[2] == list_game[4] and list_game[4] == list_game[6]:
            win_game(list_game[2])
            if list_game[2] != " ":
                return True
        return False
    def win_game(a):
        if a == "x":
            print("you WIN \\\\^V^//")
        elif a == "o":
            print("you LOST \'^\'!!!!")

    def tie():
        c = 0
        for i in list_game:
            if i != " ":
                c+=1
        if c == 9 :
            return True
        print(c)
        return False

    if select == 1 :
        print_border()
        while 1:
            player()
            if tie():
                if not check_game():
                    print("TIE..........")
                    break
            else:
                if check_game():
                    print_border()
                    break
                com()
                print_border()
                if check_game():
                    break
    elif select == 2 :
        while 1:
            com()
            print_border()
            if tie():
                if not check_game():
                    print("tie")
                    break
            else:
                if check_game():
                    print_border()
                    break
                player()
                if check_game():
                    break


play_game()
