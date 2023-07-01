#!/usr/bin/env python
# coding: utf-8

# ## Assignment 2
# 
#Q1. How do you comment code in Python? What are the different types of comments?

Code in python can be comment using '#' as well as ''' (text)'''
eg. 

# In[7]:


#This is a comment
'''square of all numbers'''

lst=[1,2,3,4,5,6,7,8,9,10]

[i**2 for i in lst]


# In[9]:


#Q2. What are variables in Python? How do you declare and assign values to variables?

##variables are names that points to an object and it stores data values.
#eg. take a variable 'a' and assign some values

a = 15
b = 20
c = a+b
print(c)


# In[15]:


#Q3. How do you convert one data type to another in Python?

num1 = 180
num2 = 56.33
sum = num1+num2
type(num1)
#type(num2)
#print(sum)


# In[16]:


type(num2)


# In[17]:


print(sum)           #Int data type converted to float


# In[31]:


a = '123'
b = 34

print("data type of:", {a} ,type(a))
print("data type of:",{b} ,type(b))

sum = int(a)
print("sum:" ,sum)
print("data type of sum:" ,type(sum))


# In[33]:


#Q4. How do you write and execute a Python script from the command line?

#Open command line and type python3 followed by the path , write the python script and click enter to execute the script


# In[34]:


#Q5. Given a list my_list = [1, 2, 3, 4, 5], write the code to slice the list and obtain the sub-list [2, 3].


# In[39]:


my_list = [1, 2, 3, 4, 5]

sub_list = my_list[1:3]
sub_list


# In[41]:


#Q6. What is a complex number in mathematics, and how is it represented in Python?

#Complex numbers are 2 real rumbers , that is written in the form x+yi , where x and y are real numbers and i is an imaginary number

real = 10
imaginary = 4
complex(real, imaginary)


# In[43]:


#Q7. What is the correct way to declare a variable named age and assign the value 25 to it?

age = int(25)
age


# In[44]:


#Q8. Declare a variable named price and assign the value 9.99 to it. What data type does this variable belong to?

price = 9.99
print(type(price))


# In[45]:


#Q9. Create a variable named name and assign your full name to it as a string. How would you print the value of this variable?

name = 'Nisha Shah'
print(name)


# In[50]:


# Q10. Given the string "Hello, World!", extract the substring "World".

str1 = "Hello,World!"
str1[6:]


# In[51]:


#Q11. Create a variable named "is_student" and assign it a boolean value indicating whether you are currently a student or not.

is_student = True

if age >=5:
    print(is_student)
else:
    print("You're not a studnet")


# In[ ]:




