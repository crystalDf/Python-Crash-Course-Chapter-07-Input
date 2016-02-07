message = input("Tell me something, and I will repeat it back to you: ")
print(message)

prompt = "\n" + "Tell me something, and I will repeat it back to you." + \
         "\n" + "Enter \"quit\" to end the program: "

message = ""
while message != "quit":
    message = input(prompt)
    print(message)

while True:
    message = input(prompt)
    if message == "quit":
        break
    print(message)

# while True:
#     print("infinity")
