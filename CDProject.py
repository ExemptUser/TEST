import csv



def menu():
    print("What do you want to do?")
    print("""
      Enter 'Exit' to quit.
      Enter 'Show' to see your current list.
      Enter 'Add' to add to your current list
      Enter 'Delete' to delete song from your current list
      Enter 'Modify' to edit your current list
      """)
def quit():
    input = raw_input("Are you sure you want to quit? [Y/N]: ")
    if input.lower() == 'y':
        exit()
    elif input.lower() == 'n':
        menu()
    else:
        print("\"{}\" is not a valid command.".format(input))
        quit()

def writecsv():
    with open("list.csv",'a+') as f:                 #open file and closes on block end
        title = raw_input("Enter song title: ")     #stores user input for title
        artist = raw_input("Enter artist name: ")   #stores user input for artist
        ID = len(f.readlines())+1              #stores next track number to be written
        f.write("\n"+str(ID)+','+title+','+artist)                         #writes track to file + newline character
    print("Added track number {}. \"{}\" by {} to list.".format(ID,title,artist))    # add new items to list

def delete():
    print([])
def show():
    reader = csv.reader(open('C:\\Users\\Vince\\PycharmProjects\\CD catalogue\\list.csv'), delimiter=',', quotechar='|')

    for row in reader:
        print(', '.join(row))

    f = open("list.csv")
    print("\n ========== Dipslaying {} songs in this list. ==========".format(len(f.readlines())))

menu()


if __name__=='__main__': #maincheck
    while True:
        command = raw_input("> ")
        if command.lower() == 'exit':
            quit()
            continue
        elif command.lower() == 'help':
            menu()
            continue
        elif command.lower() == 'show':
            show()
            continue
        elif command.lower() =='add':
            writecsv()
            continue
        elif command.lower() =='delete':
            delete()
            continue
        else:
            print("Not a valid command. Type 'help' to see menu.")
