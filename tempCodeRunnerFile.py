print("hey! there it is a emoji project")

emoji = { #dictionary named as emoji
    "fire" : "🔥",
    "skull" : "💀",
    "banana" : "🍌",
    "monkey" : "🐒",
}

def print_requested_emoji():
    typed = input("enter the emoji: ")
    if typed in emoji: #basically checking the dictionary
        print(emoji[typed])
    else:
        print("not in the memory")

print_requested_emoji()

    