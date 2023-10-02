 **UA DATALAB WORKSHOP SERIES, FALL 2023**

## An Introduction to Python for Data Science

<p><img src="https://github.com/clizarraga-UAD7/Workshops/blob/main/Python-Ecosystem.png" width=840 title="Python Ecosystem">

***

[Python](https://en.wikipedia.org/wiki/Python_(programming_language)) is one of the used [programming languages](https://en.wikipedia.org/wiki/Programming_language) in [Data Science](https://en.wikipedia.org/wiki/Data_science), as are [R](https://en.wikipedia.org/wiki/R_(programming_language)), [Julia](https://en.wikipedia.org/wiki/Julia_(programming_language)) and [SQL](https://en.wikipedia.org/wiki/SQL). 

Python is an [open-source](https://en.wikipedia.org/wiki/Open-source_software), [high-level](https://en.wikipedia.org/wiki/High-level_programming_language), [interpreted](https://en.wikipedia.org/wiki/Interpreter_(computing)), [general-purpose programming language](https://en.wikipedia.org/wiki/General-purpose_programming_language). Its design philosophy emphasizes [code readability](https://en.wikipedia.org/wiki/Code_readability) with the use of [significant indentation](https://en.wikipedia.org/wiki/Off-side_rule).

[Python](https://www.python.org) was created by the Dutch programmer [Guido van Rossum](https://en.wikipedia.org/wiki/Guido_van_Rossum), releasing version 0.9 on February 20th, 1991. The current Python stable version is Python 3.10.4, released on  March 24th, 2022. 

According to the [TIOBE Index](https://en.wikipedia.org/wiki/TIOBE_index), [Python is the most popular language](https://www.tiobe.com/tiobe-index/) used by the program developers community. 
  

Python is one of the popular languages used by data scientists for various applications. Python provide great functionality to work in mathematics, statistics, machine learning, data visualization and scientific computing. It has a wide collection of libraries to support data science applications. See [Kaggle free courses on Python](https://www.kaggle.com/learn).  

***

### Main Python Libraries

Since Python is developed by a wide community of developers and users, there is a set of libraries that can be used for specific tasks. We mention a few:


* [Numpy](https://numpy.org). The fundamental library for [scientific computing](https://en.wikipedia.org/wiki/Computational_science). 
* [SciPy](https://scipy.org). Fundamental [algorithms](https://en.wikipedia.org/wiki/Algorithm) for scientific computing.
* [Pandas](https://pandas.pydata.org). Basic library for [Data Analysis](https://en.wikipedia.org/wiki/Data_analysis) with Python.
* [Matplotlib](https://matplotlib.org). Basic [data visualization](https://en.wikipedia.org/wiki/Data_and_information_visualization) library in Python.
* [Seaborn](https://seaborn.pydata.org). Specialized library for [statistical data](https://en.wikipedia.org/wiki/Data) visualization.
* [Scikit-learn](https://scikit-learn.org/stable/). A [Machine Learning](https://en.wikipedia.org/wiki/Machine_learning) library for Python.
* [Scikit-image](https://scikit-image.org). A machine learning library for [digital image processing](https://en.wikipedia.org/wiki/Digital_image_processing). 
* [Tensorflow 2.0](https://www.tensorflow.org). Specialized library for [Deep Learning](https://en.wikipedia.org/wiki/Deep_learning) Models.
* [PyTorch](https://pytorch.org). Another library for Deep Learning. 
* [Hugging Face](). A collection of Deep Learning models named [Transformer](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)) used for [Natural Language Processing](https://en.wikipedia.org/wiki/Natural_language_processing), [Machine Translation](https://en.wikipedia.org/wiki/Machine_translation) and [Computer Vision](https://en.wikipedia.org/wiki/Computer_vision). 

Machine Learning and Deep Learning are beyond the scope of this workshop.  

***

### Python Programming Environments.

There are several options for working with Python. 
* There is a [Command-Line Interface](https://en.wikipedia.org/wiki/Command-line_interface) for a [command shell](https://en.wikipedia.org/wiki/Shell_(computing)) Python named [iPython (interactive Python)](https://en.wikipedia.org/wiki/IPython).
* There are [GUI (graphical user interface)](https://en.wikipedia.org/wiki/Graphical_user_interface) options like the web-based [Jupyter Lab / Jupyter Notebooks](https://jupyter.org) or [Spyder](https://www.spyder-ide.org).

### Working in Python.

There are two options for working in Python. Offline and Cloud-based platforms. 

* **Offline method**. Need to install all Python libraries in a local machine. The [Anaconda Python](https://www.anaconda.com) has all the packages needed. You can [download the free academic license version](https://www.anaconda.com/products/distribution). 
* **Cloud-based option**. Again, there are several options. We recommend using [_Google Colab_ (colab.research.google.com)](https://colab.research.google.com) with your _Gmail account_.
 
***

### Using Jupyter Notebooks in _Google Colab_.

[_Google Colab_](https://colab.research.google.com/) offers a basic free Python development environment on Google Cloud. It has the advantage of storing all our files in the Google Drive, as well as storing a copy of our code in [Github.com](https://github.com).

Start your [_Google Colab_ session](https://colab.research.google.com/) login in into the platform. 

<p><img src="https://github.com/clizarraga-UAD7/Workshops/blob/main/Intro2Python1.png" width=840>

<details closed>
  <summary>:memo: Note (Click to open)</summary>
To execute a Code Cell: SHIFT+ENTER _or_ use execute button.
</details>

***

### Python basics.

Python like any programming language has data types and arithmetic operations.

<details closed>
  <summary>:memo: Code Style: Python Programming Best Practices(Click to open)</summary>

* Use 4-space indentation, and no tabs.
* 4 spaces are a good compromise between small indentation (allows greater nesting depth) and large indentation (easier to read). Tabs introduce confusion, and are best left out.
* Wrap lines so that they don’t exceed 79 characters. Use `\` to break a long line. 
* This helps users with small displays and makes it possible to have several code files side-by-side on larger displays.
* Use blank lines to separate functions and classes, and larger blocks of code inside functions.
* When possible, put comments on a line of their own (Everything to the right of `#` is a comment.
* Use docstrings, that is comments extending several lines to document your code.
* Use spaces around operators and after commas, but not directly inside bracketing constructs: a = f(1, 2) + g(3, 4).
* Name your classes and functions consistently; the convention is to use UpperCamelCase for classes and lowercase_with_underscores for functions and methods.
* Special symbols and non-Roman scripts can sometime cause encoding and compatibility issues. Consider using Plain ASCII.

</details>


#### Variables

A variable has two parts, a string of characters and numbers (name), and an associated piece of information (value). We use the **assignment operator**  “=” symbol, to assign values to variables in Python. For example, the line `x=5` assigns the value 5 to the variable with name “x”. 
When we execute this line in Python, this number will be stored into this variable. 
Until the value is changed or the variable deleted, the character x behaves like the value 5. We can manipulate the variable in many ways, such as perform mathematical operations with it, or print it:

[**Numbers (Integers and Floating)**](https://docs.python.org/3/tutorial/introduction.html#numbers)
```
x = 5          # Define x = 5 as an Integer. 
print(type(x)) # Prints type "<class 'int'>"
print(x)       # Prints "5"
print(x + 1)   # Addition; prints "6"
```

Python automatically classifies the type of variables. Besides floats and integers, we can also create Boolean variables and strings:

**Boolean or logical variables (True, False)**
```
t = True
f = False
print(type(t)) # Prints "<class 'bool'>"
print(t and f) # Logical AND; prints "False"
print(t or f)  # Logical OR; prints "True"
print(not t)   # Logical NOT; prints "False"
print(t != f)  # Logical XOR; prints "True"
```
<details closed>
  <summary>:memo: Some details about Boolean values (Click to open)</summary>
  In order to assign a boolean value to a variable, we can use the words `True` or `False` after the assignment operator (note the capitalization).
  
  `True` and `False` behave similar to integers like 1 and 0. It’s possible to assign a Boolean value to variables, but cannot use `True` as a variable name.
```
  False = 5
    File "<stdin>", line 1
    SyntaxError: cannot assign to False
```

</details>

[**Strings**](https://docs.python.org/3/tutorial/introduction.html#strings)
```
hello = 'Hello'    # String literals can use single quotes
world = "World!"    # or double quotes; it does not matter.
print(hello)       # Prints "Hello"
print(len(hello))  # String length; prints "5"
hw = hello + ' ' + world  # String concatenation
print(hw)  # prints "Hello World!"
hw2 = '%s %s %d' % (hello, world, 2)  # sprintf style string formatting
print(hw2)  # prints "Hello World! 2"
```

#### The Python interpreter as a Calculator.

Basic operations are allowed on a command line. 

[**Numbers (Integers and Floating)**](https://docs.python.org/3/tutorial/introduction.html#numbers)
```
x = 5          # Define x = 5 as an Integer. 
print(type(x)) # Prints type "<class 'int'>"
print(x)       # Prints "5"
print(x + 1)   # Addition; prints "6"
print(x - 1)   # Subtraction; prints "4"
print(x * 2)   # Multiplication; prints "10"
print(x ** 2)  # Exponentiation; prints "25"
print(x + 1 + 3 * x) # Prints "21". The multiplication operator has precedence over addition. 
print((x + 1) + (3 * x)) # Prints "20". The preferred way of writing an operation. 
x += 1    # Equivalent to "x = x + 1"
print(x)  # Prints "6"
x *= 2    # Equivalent to "x = x * 2"
print(x)  # Prints "12"
y = 5/2   # Automatically defines y = 2.5 as a floating or real number.
print(type(y)) # Prints "<class 'float'>"
print(y, y + 1, y * 2, y ** 2) # Prints "2.5 3.5 5.0 6.25"
```

For more details, see [this helpful tutorial](https://pythonnumericalmethods.berkeley.edu/notebooks/chapter02.01-Variables-and-Assignment.html).

#### Data Structures.

By default Python has several objects to store data: lists, dictionaries, sets, and tuples.

<details closed>
  <summary>:memo: Note (Click to open)</summary>
Python counting start at 0.
</details>

[**Lists**](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
```
xs = [1, 2, 3]    # Create a list
print(xs, xs[2])  # Prints "[1, 2, 3] 3"
print(xs[-1])     # Negative indices count from the end of the list; prints "3"
xs[2] = 'foo'     # Lists can contain elements of different types
print(xs)         # Prints "[1, 2, 'foo']"
xs.append('bar')  # Add a new element to the end of the list
print(xs)         # Prints "[1, 2, 'foo', 'bar']"
x = xs.pop()      # Remove and return the last element of the list
print(x, xs)      # Prints "bar [1, 2, 'foo']"
```

Slicing or accessing the contents of a list.
```
nums = list(range(5))     # range is a built-in function that creates a list of integers
print(nums)               # Prints "[0, 1, 2, 3, 4]"
print(nums[2:4])          # Get a slice from index 2 to 4 (exclusive); prints "[2, 3]"
print(nums[2:])           # Get a slice from index 2 to the end; prints "[2, 3, 4]"
print(nums[:2])           # Get a slice from the start to index 2 (exclusive); prints "[0, 1]"
print(nums[:])            # Get a slice of the whole list; prints "[0, 1, 2, 3, 4]"
print(nums[:-1])          # Slice indices can be negative; prints "[0, 1, 2, 3]"
nums[2:4] = [8, 9]        # Assign a new sublist to a slice
print(nums)               # Prints "[0, 1, 8, 9, 4]"
```

[**Tuples**](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)

A tuple is an (immutable) ordered list of values. A tuple is in many ways similar to a list; one of the most important differences is that tuples can be used as keys in dictionaries and as elements of sets, while lists cannot. 

```
d = {(x, x + 1): x for x in range(10)}  # Create a dictionary with tuple keys
t = (5, 6)        # Create a tuple
print(type(t))    # Prints "<class 'tuple'>"
print(d[t])       # Prints "5"
print(d[(1, 2)])  # Prints "1"
```

[**Sets**](https://docs.python.org/3/tutorial/datastructures.html#sets)

A set is an unordered collection of distinct elements.

```
animals = {'cat', 'dog'}
print('cat' in animals)   # Check if an element is in a set; prints "True"
print('fish' in animals)  # prints "False"
animals.add('fish')       # Add an element to a set
print('fish' in animals)  # Prints "True"
print(len(animals))       # Number of elements in a set; prints "3"
animals.add('cat')        # Adding an element that is already in the set does nothing
print(len(animals))       # Prints "3"
animals.remove('cat')     # Remove an element from a set
print(len(animals))       # Prints "2"
```


[**Dictionaries**](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

A dictionary stores (key, value) pairs. In a list, we call an item by using its index or position. While using dictionaries, we use a pair's key in order to call the value:

```
d = {'cat': 'cute', 'dog': 'furry'}  # Create a new dictionary with some data
print(d['cat'])       # Get an entry from a dictionary; prints "cute"
print('cat' in d)     # Check if a dictionary has a given key; prints "True"
d['fish'] = 'wet'     # Set an entry in a dictionary
print(d['fish'])      # Prints "wet"
# print(d['monkey'])  # KeyError: 'monkey' not a key of d
print(d.get('monkey', 'N/A'))  # Get an element with a default; prints "N/A"
print(d.get('fish', 'N/A'))    # Get an element with a default; prints "wet"
del d['fish']         # Remove an element from a dictionary
print(d.get('fish', 'N/A')) # "fish" is no longer a key; prints "N/A"
```

#### Loops

In Python, objects like lists, tuples and dictionaries provide a stream of items that can be used one after th other, automatically. 
We can **loop** over the elements of any such **iterable object**, in order to generate multiple, automatic outputs.

Ex. a **for** loop for a list, that will run as many times as there are objects in the list:

```
animals = ['cat', 'dog', 'monkey']
for animal in animals:
    print(animal)
# Prints "cat", "dog", "monkey", each on its own line.

nums = [0, 1, 2, 3, 4]
squares = [x ** 2 for x in nums]
print(squares)   # Prints [0, 1, 4, 9, 16]
```
Loop or iterate over the keys in a dictionary.
```
d = {'person': 2, 'cat': 4, 'spider': 8}
for animal in d:
    legs = d[animal]
    print('A %s has %d legs' % (animal, legs))
# Prints "A person has 2 legs", "A cat has 4 legs", "A spider has 8 legs"
```
[**Python loops**]([https://docs.python.org/3/tutorial/controlflow.html#defining-functions](https://wiki.python.org/moin/ForLoop))

***

### Numpy

[Numpy](http://www.numpy.org/) is the core library for scientific computing in Python. It provides a high-performance multidimensional array object, and tools for working with these arrays. 

[Numpy](https://numpy.org/doc/stable/reference/index.html#reference) includes a large collection of mathematical defined functions. 
* [Basic Mathematical Functions](https://numpy.org/doc/stable/reference/routines.math.html)
* [Linear Algebra functions](https://numpy.org/doc/stable/reference/routines.linalg.html) based on the matrix algebra [BLAS](https://en.wikipedia.org/wiki/Basic_Linear_Algebra_Subprograms) and numeric linear algebra [LAPACK](https://en.wikipedia.org/wiki/LAPACK) software libraries. 
* [Discrete Fourier Transform](https://numpy.org/doc/stable/reference/routines.fft.html) for spectral analysis.
* [Random sampling library](https://numpy.org/doc/stable/reference/random/index.html)
* [And more ...](https://numpy.org/doc/stable/reference/routines.html) 


Before we start working with the **Numpy Library**, we need to **load** (_import_) it into the working memory, by including the following line in a Jupyter Notebook code cell.

```
import numpy as np
```
where the _alias_ or short name _np_ is given to refer to Numpy.

```
import numpy as np

print('Pi number = ', np.pi) # Using the definition of Pi from Numpy
print('The square root of Pi is = ', np.sqrt(np.pi)) # Using the square root function in Numpy

```

#### Arrays

A [numpy array](https://numpy.org/doc/stable/reference/arrays.html) is a grid of values, all of the same type, and is indexed by a tuple of nonnegative integers. The number of dimensions is the _rank_ of the array; the _shape_ of an array is a tuple of integers giving the size of the array along each dimension.
 
```
import numpy as np

a = np.array([1, 2, 3])   # Create a rank 1 array
print(type(a))            # Prints "<class 'numpy.ndarray'>"
print(a.shape)            # Prints "(3,)"
print(a[0], a[1], a[2])   # Prints "1 2 3"
a[0] = 5                  # Change an element of the array
print(a)                  # Prints "[5, 2, 3]"

b = np.array([[1,2,3],[4,5,6]])    # Create a rank 2 array
print(b.shape)                     # Prints "(2, 3)"
print(b[0, 0], b[0, 1], b[1, 0])   # Prints "1 2 4"
```

Numpy also includes a set of functions to create arrays
```
import numpy as np

a = np.zeros((2,2))   # Create an array of all zeros
print(a)              # Prints "[[ 0.  0.]
                      #          [ 0.  0.]]"

b = np.ones((1,2))    # Create an array of all ones
print(b)              # Prints "[[ 1.  1.]]"

c = np.full((2,2), 7)  # Create a constant array
print(c)               # Prints "[[ 7.  7.]
                       #          [ 7.  7.]]"

d = np.eye(2)         # Create a 2x2 identity matrix
print(d)              # Prints "[[ 1.  0.]
                      #          [ 0.  1.]]"

e = np.random.random((2,2))  # Create an array filled with random values (0,1)
print(e)                     # If run many times will give different results

```

Slicing can also be used for arrays similarly as it was used for lists.
```
import numpy as np

# Create the following rank 2 array with shape (3, 4)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

# Use slicing to pull out the subarray consisting of the first 2 rows
# and columns 1 and 2; b is the following array of shape (2, 2):
# [[2 3]
#  [6 7]]
b = a[:2, 1:3]

#### Array indexing

Numpy offers several ways to index into arrays.

# A slice of an array is a view into the same data, so modifying it
# will modify the original array.
print(a[0, 1])   # Prints "2"
b[0, 0] = 77     # b[0, 0] is the same piece of data as a[0, 1]
print(a[0, 1])   # Prints "77"
```

Integer array indexing 
```
import numpy as np

a = np.array([[1,2], [3, 4], [5, 6]])

# An example of integer array indexing.
print(np.array([a[0, 0], a[1, 1], a[2, 0]]))  # Prints "[1 4 5]"
print(np.array([a[0, 1], a[0, 1]]))  # Prints "[2 2]"
```

#### Datatypes

Every numpy array is a grid of elements of the same type.

```
import numpy as np

x = np.array([1, 2])   # Let numpy choose the datatype
print(x.dtype)         # Prints "int64"

x = np.array([1.0, 2.0])   # Let numpy choose the datatype
print(x.dtype)             # Prints "float64"

x = np.array([1, 2], dtype=np.int64)   # Force a particular datatype
print(x.dtype)                         # Prints "int64"
```

#### Array math

Basic mathematical functions operate elementwise on arrays.

```
import numpy as np

x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)

# Elementwise sum; both produce the array
# [[ 6.0  8.0]
#  [10.0 12.0]]
print(x + y)
print(np.add(x, y))

# Elementwise difference; both produce the array
# [[-4.0 -4.0]
#  [-4.0 -4.0]]
print(x - y)
print(np.subtract(x, y))

# Elementwise product; both produce the array
# [[ 5.0 12.0]
#  [21.0 32.0]]
print(x * y)
print(np.multiply(x, y))

# Elementwise division; both produce the array
# [[ 0.2         0.33333333]
#  [ 0.42857143  0.5       ]]
print(x / y)
print(np.divide(x, y))

# Elementwise square root; produces the array
# [[ 1.          1.41421356]
#  [ 1.73205081  2.        ]]
print(np.sqrt(x))
```

Inner product: 
```
import numpy as np

x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

v = np.array([9,10])
w = np.array([11, 12])

# Inner product of vectors; both produce 219
print(v.dot(w))
print(np.dot(v, w))

# Matrix / vector product; both produce the rank 1 array [29 67]
print(x.dot(v))
print(np.dot(x, v))

# Matrix / matrix product; both produce the rank 2 array
# [[19 22]
#  [43 50]]
print(x.dot(y))
print(np.dot(x, y))
```

Sum of elements:
```
import numpy as np

x = np.array([[1,2],[3,4]])

print(np.sum(x))  # Compute sum of all elements; prints "10"
print(np.sum(x, axis=0))  # Compute sum of each column; prints "[4 6]"
print(np.sum(x, axis=1))  # Compute sum of each row; prints "[3 7]"
```

Transposing a matrix:
```
import numpy as np

x = np.array([[1,2], [3,4]])
print(x)    # Prints "[[1 2]
            #          [3 4]]"
print(x.T)  # Prints "[[1 3]
            #          [2 4]]"

# Note that taking the transpose of a rank 1 array does nothing:
v = np.array([1,2,3])
print(v)    # Prints "[1 2 3]"
print(v.T)  # Prints "[1 2 3]"
```

### Pandas

[Pandas](https://pandas.pydata.org/) is a Python Library designed by [Wes McKinney](https://en.wikipedia.org/wiki/Wes_McKinney) for data manipulation and data analysis. Pandas basic [data structures](https://en.wikipedia.org/wiki/Data_structure) objects are [1-dimensional Series](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series) and [2-dimensional DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame).

Pandas can read a wide variety of data formats, such as [comma separated values (csv)](https://en.wikipedia.org/wiki/Comma-separated_values), [Microsoft Excel](https://en.wikipedia.org/wiki/Microsoft_Excel) files, [JSON](https://en.wikipedia.org/wiki/JSON), [SQL](https://en.wikipedia.org/wiki/SQL) tables and queries, and more. Pandas is a base tool for [data cleansing](https://en.wikipedia.org/wiki/Data_cleansing) and [data wrangling](https://en.wikipedia.org/wiki/Data_wrangling).

The [Pandas Python Library](https://en.wikipedia.org/wiki/Pandas_(software)) was developed in 2008 by [Wes McKinney](https://en.wikipedia.org/wiki/Wes_McKinney), for performing data manipulation and analysis. Pandas uses data structures and functions for manipulating numerical tables and time series.

As we will see further, Pandas has a set of plotting functions based on Matplotlib, that will help us visualize the analyzed dataframe.

What is a DataFrame?. It is a two-dimensional, size-mutable, potentially heterogeneous tabular data.

![dataframe](https://user-images.githubusercontent.com/97635720/155039557-4ab98001-917a-45ea-b74b-31c057a8a4d0.png)

#### Some basic operations on a Pandas DataFrame _df_.

| Function | Action |
| :-: | :-- |
| [`pd.read_csv(filename)`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html?highlight=read_csv) | Reads a CSV (comma separated values) file |
| [`pd.read_excel(filename)`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html) | Read an Excel file |
|    | [Reading other file formats](https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html) | 
| [`pd.to_csv(filename)`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html?highlight=to_csv) | Write the dataframe to a file |
| [`df.head()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.head.html)   | Shows the first 5 rows by default. If you wish to print `n` rows use `df.head(n)` |
| [`df.tail()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.tail.html)   | Shows the last 5 rows by default |
| [`df.shape`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.shape.html)    | Prints the dataframe dimensions (rows, columns) |
| [`df.info()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.info.html)   | Prints out dataframe information: number of rows, columns, names, data types, number of non null entries and more |
| [`df.describe()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html)  | Returns a statistical analysis of float variables |
| [`df['categorical variable'].describe()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html) | Describes how many they are and how many are different |
| [`df['categorical variable'].value_counts().head(10)`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.value_counts.html)  | Counts the number of occurrences of each categorial variable and shows the first 10 |
| [`df.columns`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.columns.html) |  Prints the names of the columns |
| [`df.columns = ['col1','col2','col3']`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.columns.html) | It names the columns according to list | 
| [`df.rename(columns={'Old1' : 'New1', 'Old2' : 'New2'}, inplace=True)`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rename.html) | Renames some of the columns |
| [`df.drop_duplicates(inplace=True)`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop_duplicates.html) | Eliminates repeated rows |
| [`df.isnull().sum()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.isnull.html) | Returns the sum of missing values in each variable |
| [`df.dropna()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html) | Will eliminate rows having at least one null value |
| [`df.dropna(axis=1)`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html) | Will eliminate columns having at least one null value |
| [`df.mean()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.mean.html) | Computes the arithmetic mean of the dataframe |
| [`df.fillna(x_mean, inplace=True)`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.fillna.html) |  Will replace missing values with given mean value |
| [`df.corr()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.corr.html) | Show the correlation between variables |

### Selecting information from a Pandas DataFrame

| Function | Action |
| :-: | :-- |
| ` df['B'] ` | Selects column `'B'` | 
| ` df[['A','B']] ` | Selects columns `'A'` and `'B'` |
| ` df_new =  df[['A','B']] ` | Creates a new dataframe `df_new` composed by two selected columns of `df` |
| ` df['C'] = df['A'] + df['B'] ` |  Creates a new column in `df`, being the sum of columns `'A'` and `'B'` |
| ` df_copy = df.copy()` | Creates a new dataframe copy of existing `df` |   
| ` df.drop('D', axis=1, inplace=True)` | Eliminates column `'D'` and redefines `df` |   
| ` df.loc['2']`  | Returns `df` row with index `'2'` |
| ` df.loc['2','C']` | Returns the specific value of `df`, with index=`2`, and column=`'C'` |
| ` df.iloc[2]` |  Returns row with index=`2` | 
| ` df.loc['2':'4']` | Returns rows with index `'2','3'`, and `'4'` |
| ` df.iloc[2:4]` | Returns rows with index `'2'` and `'3'`, excludes `'4'` |
| ` df[df['B'] == 5.0]`   | Selects rows where the condition `df['B']` equals `5.0` |
| ` df[(df['B'] == 5.0) & (df['D'] <= 2.0)]`  | Selects rows that satisfy both conditions simultaneously | 

The standard operators for comparing two values and conditional clauses. 

| Operators |   |
| --- | --- |
| Comparison | ```  '<',   '<=',   '==',   '!=',   '>=',   '>', ``` | 
| or their wrappers | ``` '.lt()',   '.le()',   'eq()',   '.ne()',   '.ge()',   '.gt()' ```|
| Conditionals | ` & (and)`,  `\| (or)`  |   


#### Reading a `csv` file into Pandas

Let's apply the above functions in an example. We can read a local file or a remote files. 
 
```
# We load the libraries into running memory

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

``` 

Let's read in _raw form_ or _plain text_ the CSV (comma separated values) _Penguins dataset_ from a Github repository using Pandas. And print the first 5 lines.

```
# Read the penguins size dataset

filename = "https://raw.githubusercontent.com/clizarraga-UAD7/Datasets/main/penguins/penguins_size.csv"

df = pd.read_csv(filename)

df.head()
```

Next, we can apply a set of functions to inquiry about the dataframe
```
# General information about the dataset
df.info()
````

***


### :books: Basic References

* [Python Tutorial](https://docs.python.org/3/tutorial/index.html). Python.org.
* [Numpy Tutorial](https://numpy.org/doc/stable/user/absolute_beginners.html#). Numpy.org.
* [SciPy User's Guide](https://docs.scipy.org/doc/scipy/tutorial/index.html#user-guide). SciPy.org.
* [Getting started with Pandas](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html). Pydata.org.

#### Cheat Sheets
* [Jupyter Notebook.](https://www.datacamp.com/cheat-sheet/jupyter-notebook-cheat-sheet) Cheat Sheet. Datacamp.
* [Python 3.](https://perso.limsi.fr/pointal/_media/python:cours:mementopython3-english.pdf) Cheat Sheet. Laurent Pointal. Mémento v.2.0.6.
* [Python Basics.](https://s3.amazonaws.com/dq-blog-files/python-cheat-sheet-basic.pdf) Data Science Cheat Sheet. Dataquest.
* [Python Intermediate.](https://s3.amazonaws.com/dq-blog-files/python-cheat-sheet-intermediate.pdf) Data Science Cheat Sheet. Dataquest.
* [Importing Data.](https://www.datacamp.com/cheat-sheet/importing-data-in-python-cheat-sheet) Python for Data Science Cheat Sheet. Datacamp.
* [Numpy. Data Analysis in Python.](https://www.datacamp.com/cheat-sheet/numpy-cheat-sheet-data-analysis-in-python) Cheat Sheet.  Datacamp. 
* [Numpy.](https://s3.amazonaws.com/dq-blog-files/numpy-cheat-sheet.pdf) Data Science Cheat Sheet. Dataquest.
* [Pandas.](https://www.datacamp.com/cheat-sheet/pandas-cheat-sheet-for-data-science-in-python) Data Science Cheat Sheet. Datacamp.
* [Pandas. Data Wrangling in Python.](https://www.datacamp.com/cheat-sheet/pandas-cheat-sheet-data-wrangling-in-python) Cheat Sheet. Datacamp.
* [Pandas.](https://drive.google.com/file/d/1UHK8wtWbADvHKXFC937IS6MTnlSZC_zB/view) Data Science Cheat Sheet. Dataquest.

#### Free Short Courses.
* [Introduction to Programming](https://www.kaggle.com/learn/intro-to-programming). Kaggle.com.
* [Python](https://www.kaggle.com/learn/python). Kaggle.com.
* [Data Cleaning](https://www.kaggle.com/learn/data-cleaning). Kaggle.com.
* [Pandas](https://www.kaggle.com/learn/pandas). Kaggle.com.

***

Created: 05/20/2022 (C. Lizárraga); 
Last update: 09/28/2023 (M. Krishnaswamy)


<img src="https://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-nc-sa.png" width="128">  [  CC BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/4.0/)


<img src="https://datascience.arizona.edu/sites/default/files/Data%20Science%20Institute_Webheader%20%281%29_0.svg" width="256">
  

