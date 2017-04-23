test_assessment.py


#I tested all functions written in my assessment for Functions: assessment.py

def is_hometown(home_town):
    """ Takes home_town to see if it is the same as my home_town."""

    if home_town == "Little Rock":
        return True
    else:
        return False
        
# TESTS 
print(is_hometown("Little Rock"))  
print(is_hometown("LittleRock"))  


def concat_names(first_name, last_name):
    """ Takes first name and last name str and concatenates a full name into a  
    single string """

    full_name = first_name + " " + last_name

    return full_name
    
# TESTS 
print(concat_names("first_name", "last_name"))  
print(concat_names("", " "))  


def response_greeting(home_town, first_name, last_name):
    """ Takes home town, first name, and last names as arguments returning a
    proprietary response """
    full_name = concat_names(first_name, last_name)
    if is_hometown(home_town) == True:
        print "Hi, %s, we're from the same place!" % (full_name)
    else:
        print "Hi, %s, I'd like to visit %s!" % (full_name, home_town)


print(response_greeting("Little Rock", "first_name", "last_name"))





def is_berry(fruit):
    """Determines if fruit is a berry

    >>> is_berry("blackberry")
    True

    >>> is_berry("durian")
    False

    """

    if fruit in ["strawberry", "raspberry", "blackberry"]:
        return True
    else:
        return False
    
# true test
print(is_berry("strawberry"))
# true test
print(is_berry("raspberry"))
# true test
print(is_berry("blackberry"))
 
# false test
print(is_berry("apple"))

######################################

def shipping_cost(fruit):
    """Calculates shipping cost of fruit

    >>> shipping_cost("blackberry")
    0

    >>> shipping_cost("durian")
    5

    """

    if is_berry(fruit) == True:
        return 0
    elif is_berry(fruit) == False:
        return 5
        
# true test, return 0
print(shipping_cost("strawberry"))


# false test, return 5
print(shipping_cost("applejack"))


###################################


def append_to_list(lst, num ):
    """Returns a new list consisting of the old list with the given number
       added to the end.

    >>> append_to_list([3, 5, 7], 2)
    [3, 5, 7, 2]

    """

    lst.append(num)
    return lst



lst  = [3, 5, 7, 2]
num = 10
# true test, return 0
print(append_to_list(lst,num ))

 #####################################
 
 
 
def calculate_price(base_price, state, state_tax = .05):
    """Calculate total price of an item, figuring in state taxes and fees.

    >>> calculate_price(40, "CA")
    43.26

    >>> calculate_price(400, "NM")
    420.0

    >>> calculate_price(150, "OR", 0.0)
    150.0

    >>> calculate_price(60, "PA")
    65.0

    >>> calculate_price(38, "MA")
    40.9

    >>> calculate_price(126, "MA")
    135.3

    """
    
    #  base_price + ( base_price * state_tax)  + all fees
    after_tax = base_price + ( base_price * state_tax )

    if state == "CA":
      # req a  3 percent recycle fee additional
      ca_three_percent_recycling = base_price * .03
      return after_tax + ca_three_percent_recycling 
    elif state == "PA":
      highway_safety_fee = 2
      return after_tax + 2
    elif state == "MA":
      highway_safety_fee = 2
      if base_price < 100:
        commonwealth_fund_fee = 1
      else:
        commonwealth_fund_fee = 3
    
      return after_tax + commonwealth_fund_fee


print( "calculate_price function CA" )

# CA TEST
base_price = 10 
state = "CA" 
state_tax = 0.05
# true test, return 0
print(calculate_price(base_price, state, state_tax ))


# CA TEST no tax 
print(calculate_price(base_price, state ))




print( "calculate_price function PA" )
# PA TEST
base_price = 10 
state = "PA" 
state_tax = 0.05
# true test, return 0
print(calculate_price(base_price, state, state_tax ))

print( "calculate_price function MA" )
# MA TEST
base_price = 10 
state = "MA" 
state_tax = 0.05
# true test, return 0
print(calculate_price(base_price, state, state_tax ))

 #####################################
 


# Part 3: (a)
def list_appender(lst, *args):
    """ takes a list and an indeterminate number of additional arguments and
    appends them to the list """
    
    for arg in args:
        lst.append(arg)
    return lst

lst = [10, 10, 10]
state = 01 
state_tax = 0.05

#Test true PASSED
print(list_appender(lst, state, state_tax ))




########################

# Part 3 (b)
def original_and_multiplied(word):
    """ Takes a word and returns a tuple with the word and 3 x the word """

    def word_multiplier(_word):
        return _word * 3
    return (word, word_multiplier(word))
    
state_tax = "statetax"

#Test true PASSED
print(original_and_multiplied(state_tax))