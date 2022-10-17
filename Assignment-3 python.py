#!/usr/bin/env python
# coding: utf-8

# # Python Crash Course Exercises - Solutions
# 
# This is an optional exercise to test your understanding of Python Basics. If you find this extremely challenging, then you probably are not ready for the rest of this course yet and don't have enough programming experience to continue. I would suggest you take another course more geared towards complete beginners, such as [Complete Python Bootcamp]()

# ## Exercises
# 
# Answer the questions or complete the tasks outlined in bold below, use the specific method described if applicable.

# ** What is 7 to the power of 4?**

# In[1]:


7 **4


# In[15]:


**Split string**

    s = ("Hi there Sam!")
    
**into a list. **


# In[16]:


s = 'Hi there Sam!'


# s.split()

# In[17]:


s= ['Hi', 'there', 'sam!']


# ** Given the variables:**
# 
#     planet = "Earth"
#     diameter = 12742
# 
# ** Use .format() to print the following string: **
# 
#     The diameter of Earth is 12742 kilometers.

# In[18]:


planet = "Earth"
diameter = 12742


# In[19]:


print("The diameter of {} is {} kilometers.".format(planet,diameter))


# ** Given this nested list, use indexing to grab the word "hello" **

# In[20]:


lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]


# In[7]:


lst[3][1][2][0]


# ** Given this nest dictionary grab the word "hello". Be prepared, this will be annoying/tricky **

# In[8]:


d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}


# In[21]:


d['k1'][3]['tricky'][3]['target'][3]


# ** What is the main difference between a tuple and a list? **

# In[10]:


# Tuple is immutable, list is mutable otherwise can be changed.


# ** Create a function that grabs the email website domain from a string in the form: **
# 
#     user@domain.com
#     
# **So for example, passing "user@domain.com" would return: domain.com**

# In[11]:


def domainGet(email):
    return email.split('@')[-1]


# In[12]:


domainGet('user@domain.com')


# ** Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization. **

# In[13]:


def findDog(st):
    return 'dog' in st.lower().split()


# In[14]:


findDog('Is there a dog here?')


# ** Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases. **

# In[15]:


def countDog(st):
    count = 0
    for word in st.lower().split():
        if word == 'dog':
            count += 1
    return count


# In[16]:


countDog('This dog runs faster than the other dog dude!')


# ** Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'. For example:**
# 
#     seq = ['soup','dog','salad','cat','great']
# 
# **should be filtered down to:**
# 
#     ['soup','salad']

# In[17]:


seq = ['soup','dog','salad','cat','great']


# In[18]:


list(filter(lambda word: word[0]=='s',seq))


# ### Final Problem
# **You are driving a little too fast, and a police officer stops you. Write a function
#   to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket". 
#   If your speed is 60 or less, the result is "No Ticket". If speed is between 61 
#   and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big    Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all 
#   cases. **

# In[19]:


def caught_speeding(speed, is_birthday):
    
    if is_birthday:
        speeding = speed - 5
    else:
        speeding = speed
    
    if speeding > 80:
        return 'Big Ticket'
    elif speeding > 60:
        return 'Small Ticket'
    else:
        return 'No Ticket'


# In[20]:


caught_speeding(81,True)


# In[21]:


caught_speeding(81,False)


# In[ ]:


# print("Enter the speed(km/h)(only member phase):\n")
speed=int(input(">"))
print("Enter your birthday:(in DD/MM/YYYY format)\n")
is_birthday=str(input(">"))
def caught_speeding(speed, is_birthday):
    
    if is_birthday=="01/03/2002":
        speeding = speed - 5
    else:
        speeding = speed
    
    if speeding <=60:
        print("no ticket")
    elif speeding>61 and speeding<=80:
      print("Small Ticket")
    else:
      print("Big Ticktet")
caught_speeding (speed,is_birthday)

 Enter the speed(km/h)(only member phase):

>87
Enter your birthday:(in DD/MM/YYYY format)

>01/03/2002
Big Ticktet
# In[ ]:


print("Enter the speed(km/h)(only member phase):\n")
speed=int(input(" "))
print("Enter your birthday:(in DD/MM/YYYY format)\n")
is_birthday=str(input(" "))
def caught_speeding(speed, is_birthday):
    
    if is_birthday=='01/03/2002':
        speeding = speed - 5
    else:
        speeding = speed
    
    if speeding <=60:
        print("no ticket")
    elif speeding>61 and speeding<=80:
      print("Small Ticket")
    else:
      print("Big Ticktet")
caught_speeding (speed,is_birthday)


# 
# 
#  67
# Enter your birthday:(in DD/MM/YYYY format)
# 
#  01/03/2002
# Small Ticket
# Create an employee list with basic salary values(at least 5 values for 5 employees) and using a for loop retreive each employee salary and calculate total salary expenditure.
# 

# In[ ]:


def weeklyPaid(hours_worked, wage):
    if hours_worked > 40:
        return 40 * wage + (hours_worked - 40) * wage * 1.5
    else:
        return hours_worked * wage
 
 
hours_worked = 35
wage = 1000
 
pay = weeklyPaid(hours_worked, wage)
 
print(f"Total salary expenditure: Rs.{pay:.2f} ")


# Total salary expenditure: Rs.35000.00 
# Create two dictionaries in Python:
# 
# First one to contain fields as Empid, Empname, Basicpay
# 
# Second dictionary to contain fields as DeptName, DeptId.
# 
# Combine both dictionaries.

# In[2]:


def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res  
# Driver code
dict1 = {'EmpName': 'B N PUNEETH','Empid':'01032002', 'Basicpay': 50000}
dict2 = {'DeptName': 'Technical', 'DeptId': 3767}
dict3 = Merge(dict1, dict2)
print(dict3)
{'EmpName': 'B N PUNEETH', 'Empid': '01032002', 'Basicpay': 50000, 'DeptName': 'Technical', 'DeptId': 3767}


# {'EmpName': 'B N PUNEETH', 'Empid': '01032002', 'Basicpay': 50000, 'DeptName': 'Technical', 'DeptId': 3767}
# {'EmpName': 'B N PUNEETH',
#  'Empid': '01032002',
#  'Basicpay': 50000,
#  'DeptName': 'Technical',
#  'DeptId': 3767}
#  

# In[7]:


print("Great job")


# In[ ]:




