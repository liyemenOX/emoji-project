import json

print("hey! there it is a emoji project")

with open("emoji.json", "r", encoding = "utf-8") as file:
    emoji = json.load(file)
    
    requested = input("enter the emoji: ").strip().lower()
    
    found_any_emoji = False
            
def print_requested_emoji():
    
    global found_any_emoji #introduced a global variable 
    
    matched_item = partial_search()# introduced a matched_item for recieving 

    print(matched_item["emoji"])
    
    
def partial_search():

    global found_any_emoji
    for item in emoji:
        for word in item["keywords"]:
            if requested in item["name"]  or requested in word:
        #starting to improve the search part of partial check 
                found_any_emoji == True
                return item
    pass
    if not found_any_emoji:
        print("emoji not found")    
            
print_requested_emoji()



    