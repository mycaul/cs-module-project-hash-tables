import random
import re

# Read in all the words in one go
word_collection = []

with open("input.txt") as f:
    words = f.read()
    words = words.split()
    
    

cache ={}
start_words = []
end_words = []
middle_words = []
string = ''

for word in words:
    if re.match('^[\"]*[A-Z]', word) is not None:
        start_words.append(word)
 
    elif re.match('^[a-z]*[.?!"]$', word) is not None:
        end_words.append(word)
      
    else:
        middle_words.append(word)
        

random_start = random.choice(start_words)

random_midle = random.choice(middle_words) 


print(random_start)
print(random_midle)


def sentence_generator():
    middle_count= 0
    
    random_start = random.choice(start_words)
    
    random_end = random.choice(end_words)
    
    for c in random_start.split():
        cache[c] = c
    while middle_count < 7:
        random_midle = random.choice(middle_words) 
        for c in random_midle.split():
            cache[c] = c
            middle_count += 1
    for c in random_end.split():
        cache[c] = c
        
    return " ".join(list(cache.keys()))

print(sentence_generator())