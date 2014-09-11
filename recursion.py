import pdb

def sumTo(n):
    result = n
    #base case
    if n == 0:
        return result
    #general case
    else:
        result = n + sumTo(n - 1)
        return result
        
##def palindrome(word):
##    n = len(word)
##    pal = True
##    #base case
##    if n == 1 or n == 0 or n == 2:
##        print(word)
##        print("test")
##        return pal
##    #general case
##    else:
##        print(word)
##        if word[-1] == word[0]:
##            newWord = word[1:-1]
##            word = palindrome(newWord)
##            #print(word)
##        else:
##            return True

def ispalindrome(word):
    if len(word) < 2:
        return True
    if word[0] != word[-1]:
        return False
    return ispalindrome(word[1:-1])

if __name__ == "__main__":

    #pdb.set_trace()
    res = ispalindrome("efr")
    print(res)
