import json

print("hey! there it is a emoji project")

with open("emoji.json", "r", encoding = "utf-8") as file:
    emoji = json.load(file)
    
    requested = input("enter the emoji: ").strip().lower()
    
    found_any_emoji = False
            
def print_requested_emoji():
    
    global found_any_emoji #introduced a global variable 
    
    for item in emoji:
        
        partial_search(item)
            #looping through the entire list of emojis
                
    
    if not found_any_emoji:
        print("emoji not found")
    
def partial_search(item):

    global found_any_emoji
    if requested in item["name"] or requested in item["keywords"]: 
        #starting to improve the search part of partial check 
        print(item["emoji"])
    found_any_emoji = True

print_requested_emoji()



    