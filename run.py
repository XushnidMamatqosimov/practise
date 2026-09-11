message = "Hello world"
print(message)

#  Mit Task


def findDoublers(text):
    for letter in text:
        if text.count(letter) == 2:
            return True
    return False;
        
            
    


res = findDoublers("halol")
print(res)
