# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    
    with open(filename) as f:  # using automatic close with with
        filename = str(f.read())  # making sure it returns a string
    
    return filename 


print(read_file_content("./story.txt"))

  
def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    count_dict = dict()
    words= text.split()
    print(words)
    for word in words:
        if word in count_dict:
            count_dict[word] = count_dict[word] + 1
            print("already there then count")
            
        else:
            count_dict[word] = 1
            print("new then move")
    return count_dict

print(count_words())

    
   
    #return {"as": 10, "would": 20}



