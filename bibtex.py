#!/usr/bin/env python

def extract_author(str1):
    if ' ' in str1 and ',' not in str1:
        names = str1.split(" ")
        len_names = len(names)
        if len_names < 3:
            return (names[1], names[0])
        elif len_names > 2:
            return (names[2], names[0] + " " + names[1])
    elif ',' in str1 and ' ' in str1:
        names = str1.split(",")
        return (names[0], names[1].lstrip(" "))
    else:
        return (str1,"")

#def extract_authors(str2):
#    if 'and' in str2:
#        names = str2.split("and")
#        mul_authors = str(names[0]).split(",")
#        proper_mul_authors = str(names[1]).split(",")
#        mul_authors[1] = str(mul_authors[1].rstrip(" "))
#        proper_mul_authors[1] = str(proper_mul_authors[1].rstrip(" "))
#        return (names[0], (mul_authors[0], mul_authors[1]))
#        return (names[1], (proper_mul_authors[0], proper_mul_authors[1]))
