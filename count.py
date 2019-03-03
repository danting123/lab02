

def count_char(text):
    # TODO count the number of times each character occurs in the text
    # and print out each character along with its count
   master = {}
   for item  in text:
     if item in master:
        master[item] += 1
     else:
        master[item] = 1
   for key,val in master.items():
     print(key,val)

def count_char_insensitive(text):
    # TODO do the same as `count_char` but in a case-insensitive manner

   master = {}
   for item  in text:
     item = item.lower()
     if item in master:
        master[item] += 1
     else:
        master[item] = 1
   for key,val in master.items():
     print(key,val)


def count_char_ordered(text):
    # TODO print the characters in the descending order of the count
    # HINT: lookup `sorted()` in the Python documentation
    
    # This task is quite difficult, so please feel free to make use of
    # resources online (Python docs, Stack Overflow, etc.)
    
   master = {}
   for item  in text:
     item = item.lower()
     if item in master:
        master[item] += 1
     else:
        master[item] = 1
   master = sorted(master.items(),key=lambda x:x[1],reverse=True)
   for i in range(len(master)):
        print(master[i][0],master[i][1])

