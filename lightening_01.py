#Write a function that take a list, a number, and a string as args.

#The string parameter should have a default value.

#In the function body, loop over the list and output the items.

#Use "slice" to loop through on the first n items in the array, where n = the value of the second argument.

#each item should be prefaced by value of the string argument
    #one example output might then be "I have visited the city of San Francisco" was an item in the list, and the string argument was "I have visited  the city of"

#Try it out! Execute the function both with and without passing in a value for the string parameter.

list = ["egg","bananas", "rice", "cheese"]
num = 5

def my_function(list, num, string="my string"):
    for item in list[:num]:
        print(string + " " +item)

    print("Print Sample 1", list, num, string)
    print("Print Sample 2", f'{list} {num} {string}')

my_function(list, num, "my brain is fried")
