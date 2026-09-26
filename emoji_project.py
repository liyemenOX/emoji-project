import json

class Emoji:
    def __init__(self,name,emoji,keywords,category):
        self.name = name
        self.emoji = emoji
        self.keywords = keywords
        self.category = category

        
print("hey! there it is a emoji project")

class Emoji_Database:
    def __init__(self,filename):
        self.emoji = []
        self.search_history = []
        self.load_emojis()
        self.filename = filename
        
    def load_emojis(self):
        with open("emoji.json", "r", encoding = "utf-8") as file:
            emoji = json.load(file)
    
        for item in emoji:
            new_emoji_object = Emoji(item["name"],item["emoji"],item["keywords"],item["category"])
            self.emoji.append(new_emoji_object)
            
      
    
    def partial_search(self,requested):
        
        multiple_result = []
        self.found_any_emoji = False
         
        for item in self.emoji:
            if requested in item.name or requested in item.category:
                self.found_any_emoji = True
                multiple_result.append(item)
                
            else:
                for word in item.keywords:
                    if requested in word:  #starting to improve the search part of partial check 
                        self.found_any_emoji = True
                        multiple_result.append(item)
                        break
                
                        
        self.search_history.append(multiple_result)
        return multiple_result
    
db = Emoji_Database("emoji.json")

requested = input("enter the emoji:").strip().lower()

multiple_result = db.partial_search(requested)

if db.found_any_emoji and multiple_result:
    print("\nMatching Emojis:")
    for emoji_obj in multiple_result:  
        print(emoji_obj.emoji,emoji_obj.name,emoji_obj.category) 
    
else:
    print("\nNo matching emojs found!")






    
