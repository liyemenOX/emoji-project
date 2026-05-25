import json

print("hey! there it is a emoji project")

with open("emoji.json", "r", encoding = "utf-8") as file:
    emoji = json.load(file)
    
    requested = input("enter the emoji: ").strip().lower()
            
def print_requested_emoji():
    
    for item in emoji: #looping through the entire list of emojis
        if requested == item["name"] or requested == item["keywords"]:
            
            partial_search(item)
            break      
    
    else:
            print("emoji not found")#calling the function

def partial_search(item):
    
    if requested in item["name"]:
        print(item["emoji"])

print_requested_emoji()
        

            