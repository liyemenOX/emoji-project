import json
import sqlite3

class Emoji:
    def __init__(self,name,emoji,keywords,category):
        self.name = name
        self.emoji = emoji
        self.keywords = keywords
        self.category = category

        
print("hey! there it is a emoji project")

class Emoji_Database:
    def __init__(self,filename):
        self.filename = filename
        self.emoji = []
        self.load_emojis()
        #removed the search_history cause it was pure ram based and we want the history to stay forever
        self.conn = sqlite3.connect("emoji_history.db")
        
        self.cursor = self.conn.cursor()
        
        self.cursor.execute("""
                            CREATE TABLE IF NOT EXISTS history(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            emoji_symbol TEXT,
                            emoji_name TEXT)""") 
        
        self.conn.commit()   
                    
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
        
        # writing the loop for the insert command
        for item in multiple_result:
            
            self.cursor.execute(
                "INSERT INTO HISTORY(emoji_symbol,emoji_name) VALUES (?,?)", (item.emoji,item.name)
            )
            
        self.conn.commit()
        return multiple_result
    
    def add_to_search(self):
        print("\n--- PRINT PERMANENT SQL SEARCH HISTORY ---")
        
        self.cursor.execute("SELECT emoji_symbol,emoji_name FROM history")
        
        saved_history = self.cursor.fetchall()
        
        if not saved_history:
            print("No history found ")
        else:
            for index,row in enumerate(saved_history, 1):
                print(f"{index}. Saved Emoji: {row[0]} {row[1]}")
        
db = Emoji_Database("emoji.json")

requested = input("enter the emoji:").strip().lower()

multiple_result = db.partial_search(requested)

if db.found_any_emoji and multiple_result:
    print("\nMatching Emojis:")
    for emoji_obj in multiple_result:  
        print(emoji_obj.emoji,emoji_obj.name,emoji_obj.category) 
    
else:
    print("\nNo matching emojs found!")

db.add_to_search()



    
