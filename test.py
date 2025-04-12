def count_character(string, target):
    count = 0

    for ch in string:   
        if ch == target:
            count = count + 1
    
    return(count)

print("Should print a count of 3:")
print(count_character("oxen and foxen all live in boxen", "x"))
