import socket

print("Hello, welcome to my string manipulation program.")
print("This program can be used to modify and analyze any text you'd like to.")
print("Whether you're writing a paper for a class, or an email to your boss, you can use this to make fixes and changes quickly, rather than manually doing an advanced search/replace or counting the amount of words/characters in it.")
print("The benefit of this program is the speed it offers in how quick you can make changes. The cost of using this program is accidentally ruining a text you give it. Because of this potential risk, make sure to save whatever text you want to modify before running it through this program.")

print()


def helpMessage():
    print()
    print("Program Instructions:")
    print("Input the following characters to proceed.")
    print("You can also enter the capitalized version of the letters if you wish.")
    print()
    print("h - Display this help menu (New Feature)")
    print("r - Reverse your string (New feature)")
    print("cc - Show character count of string (New Feature)")
    print()    

helpMessage()

print("Caution, new features are new and thus may still need more development.")
print("On the other hand, they add functionality. You could help with their development, here's the github repo with code:")
print("Please be careful with tinkering, it has an even higher chance of ruining your text. make sure to back it up!")
print("Also, when tinkering be cautious of the fact that if you're submitting code to be incorporated into the repo it's properly commented and tested. It could ruin our code.")
print("https://github.com/sharoninator/cs361-string-program")


print("Enter a text to be manipulated/analyzed. Terminate the text with a backslash like this: \\")


string = ""
while True:
    new = input()
    string+=new + "\n"
    if(new[len(new)-1] == "\\"):
        string = string[:-2]
        break

while True:
    option = input("Option: ").lower()

    if(option == "h"):
        helpMessage()
        continue
    elif(option == "r"):
        print("Reversed string:")
        port = 4545
    elif(option == "cc"):
        print("Character count:")
        port = 4546
    else:
        print("Invalid option, try again")
        continue
        
    with socket.create_connection(('localhost', port)) as client_socket:
        client_socket.send(string.encode())
        received_data = client_socket.recv(1024).decode()
        print(received_data)
