import json

print("hey! there it is a emoji project")

with open("emoji.json", "r", encoding = "utf-8") as file:
    emoji = json.load(file)
    
    requested = input("enter the emoji: ").strip().lower()
    
    found_any_emoji = False
            
def print_requested_emoji():
    
    global found_any_emoji #introduced a global variable 
    
    multiple_result = partial_search()
    
    if not multiple_result:
        print("no matching emoji found in database")
        return     

    for item in  multiple_result:
        print(item["emoji"])
    
    
def partial_search():

    multiple_result = []
    
    global found_any_emoji
    for item in emoji:
        for word in item["keywords"]:
            if requested in item["name"]  or requested in word:
        #starting to improve the search part of partial check 
                found_any_emoji = True
                multiple_result.append(item)
                break;
    return multiple_result
           
print_requested_emoji()



    