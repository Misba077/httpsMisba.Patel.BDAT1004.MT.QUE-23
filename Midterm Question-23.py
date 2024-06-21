#!/usr/bin/env python
# coding: utf-8

# # Midterm Question - 23

# Develop a recursive function tough() that takes two nonnegative integer arguments and outputs a pattern as shown below. 
# Hint: The first argument represents the indentation of the pattern, where the second argument 
#     -- always a pattern of 2 indicates the number *s in the longest line of *s in the pattern
# 

# In[25]:


def tough(indent, pattern):
    if pattern == 0:
        return
    
    if indent % 2 == 0:
        print(' '* (indent // 2) + '*')
    else:
        print(' '* (indent // 2) + '*' * (pattern + 1))
    
    tough(indent + 1, pattern - 1)

tough(0, 4)

