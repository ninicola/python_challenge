#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 28 13:33:56 2018

@author: f103861
"""

names = []
for name in range(5):
    name = input("Please enter the name of someone you know. ")
    names.append(name)

# @TODO: Use a list comprehension to create a list of lowercased names
lowercased = [name.lower() for name in names]

# @TODO: Use a list comprehension to create a list of titlecased names
# https://www.tutorialspoint.com/python/string_title.htm
titlecased = [name.title() for name in lowercased]

invitations = [
    f"Dear {name}, please come to the wedding this Saturday!" for name in titlecased]
#print(invitations)
for invitation in invitations:
      print(invitation)
