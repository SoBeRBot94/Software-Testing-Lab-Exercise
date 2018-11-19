# Bibtex Testing Diary
## Author: Sudarsan Bhargavan

<span style="color:Red"> RED </span>

String Initialization

```py
    def extract_author(str1):
```
---

<span style="color:Green"> GREEN </span>

First Test Case <br />
Simply return the Surnames and an empty string
```py
def extract_author(str1):
    return (str1,"")
```
```
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

---

<span style="color:Red"> RED </span>

Second Test Case <br />
Return the surnames first and then the firstnames
```py
def extract_author(str1):
        names = str1.split(" ")
        return (names[1], names[0])
        return (str1,"")
```
```
E.
======================================================================
ERROR: test_author_1 (__main__.TestAuthorExtract)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "./testcase.py", line 23, in test_author_1
    (Surname,FirstNames) = bibtex.extract_author(self.simple_author_1)
  File "/home/SoBeRBot94/University-Files/SEM-1/studyPeriod-2/Software-Testing/Bibtex_Lab/bibtex.py", line 6, in extract_author
    return (names[1], names[0])
IndexError: list index out of range

----------------------------------------------------------------------
Ran 2 tests in 0.001s

FAILED (errors=1)
```

<span style="color:Green"> GREEN </span>
```py
def extract_author(str1):
    if ' ' in str1:
        names = str1.split(" ")
        return (names[1], names[0])
    else:
        return (str1,"")
```
```
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```
---

<span style="color:Red"> RED </span>

Third Test Case <br />
Split the string at whitespaces and then return the Surname first and the First and the Middle names concatenated along with whitespaces.

```py
def extract_author(str1):
    if ' ' in str1:
        names = str1.split(" ")
        len_names = len(names)
        if len_names < 3:
            return (names[1], names[0])
        elif len_names > 2:
            return (names[2], names[0] + names[1])
    else:
        return (str1,"")
```
```
..F
======================================================================
FAIL: test_author_3 (__main__.TestAuthorExtract)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "./testcase.py", line 35, in test_author_3
    self.assertEqual( (Surname,First) , ("Pearson","Justin Kenneth"))
AssertionError: Tuples differ: ('Pearson', 'JustinKenneth') != ('Pearson', 'Justin Kenneth')

First differing element 1:
'JustinKenneth'
'Justin Kenneth'

- ('Pearson', 'JustinKenneth')
+ ('Pearson', 'Justin Kenneth')
?                    +


----------------------------------------------------------------------
Ran 3 tests in 0.001s

FAILED (failures=1)
```
<span style="color:Green"> GREEN </span>

```py
def extract_author(str1):
    if ' ' in str1:
        names = str1.split(" ")
        len_names = len(names)
        if len_names < 3:
            return (names[1], names[0])
        elif len_names > 2:
            return (names[2], names[0] + " " + names[1])
    else:
        return (str1,"")
```
```
...
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```

---

<span style="color:Red"> RED </span>

Fourth Test Case <br />
Check for a comma(,) then return Surnames first and then the First and Middle names.

```py
def extract_author(str1):
    if ' ' in str1:
        names = str1.split(" ")
        len_names = len(names)
        if len_names < 3:
            return (names[1], names[0])
        elif len_names > 2:
            return (names[2], names[0] + " " + names[1])
    elif ',' in str1:
        names = str1.split(",")
        return (names[0], names[1])
    else:
        return (str1,"")
```
```
...F
======================================================================
FAIL: test_surname_first (__main__.TestAuthorExtract)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "./testcase.py", line 38, in test_surname_first
    self.assertEqual( (Surname,First) , ("Pearson","Justin Kenneth"))
AssertionError: Tuples differ: ('Kenneth', 'Pearson, Justin') != ('Pearson', 'Justin Kenneth')

First differing element 0:
'Kenneth'
'Pearson'

- ('Kenneth', 'Pearson, Justin')
+ ('Pearson', 'Justin Kenneth')

----------------------------------------------------------------------
Ran 4 tests in 0.001s

FAILED (failures=1)
```

<span style="color:Green"> GREEN </span>

Use lstrip() method to remove leading whitespaces

```py
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
```
```
....
----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
```
