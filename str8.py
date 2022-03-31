#Program for a Function that takes a list of words and returns the length of the longest one.

def longest_word(list):                                 #define a function which takes list as a parameter
    longest=0                                         
    
    for words in list:                                  #loop for each word in list
        if len(words)>longest:                          #compare length iteratively
            longest=len(words)
            lword=words
    return lword                                        #return longest word

w=['Entertainment','entire','Elephant','inconsequential']
print("Longest word is",longest_word(w), "with", len(longest_word(w)), "letters.")
