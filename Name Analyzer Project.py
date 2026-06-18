# Name Analyzer Project

# Write a Python program that: takes a list of names and performs multiple operations on the list

#Specifically:

#Creates a list with all names in UPPERCASE
#Finds only the names with more than 5 letters
#Counts how many names contain the letter "a"
#Returns all results (you can print them)

#Uppercase
def to_upper(names):
    new_list=[]
    for name in names:
        name.upper()
        new_list.append(name.upper())
    return (new_list)

#Names Length
def long_names(names):
    new_list=[]
    for name in names:
        if len(name)>5:
            new_list.append(name)
    return(new_list)

# Counting letters
def count_a(names):
    count = 0
    for name in names:
        if 'a' in name.lower():
            count += 1
    return count

#Printing Results
print(to_upper(['Panagiota', 'Maria', 'Georgia']))
print(long_names(['Panagiota', 'Maria', 'Georgia']))
print(count_a(['Panagiota','Maria', 'Georgia']))
            
        
        
       
   