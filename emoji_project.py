import json

print("hey! there it is a emoji project")

with open("emoji.json", "r", encoding = "utf-8") as file:
    emoji = json.load(file)

def print_requested_emoji():
    
    requested = input("enter the emoji: ").lower()
    
    if requested in emoji: #basically checking the dictionary
        #now looping inside 
        print(emoji[requested])
                
    else:
        print("emoji not found")#calling the function

print_requested_emoji()



    