title: Python Method Arguments
slug: python-method-arguments
category: python
date: 2020-05-18 21:41
modified: 2020-05-18
tags: python, programming
summary: Finding Keyword Arguments in Python Class Methods


At work, we have a library that we are installing using a Git Hash.
This is an older library that has not been updated to use proper versioning and packaging. 

The library has a change that needs to get pulled down but not all users are updating this library.
The Goal of this is to check to see if a keyword argument has been added to a class method. 
The class looks kind of like this:
```python
class MyFunkyClass:
    def __init__(self):
        pass
    
    def internal_method(self, arg1, arg2):
        pass
```

Our goal here is to check that `arg2` is available as it was implemented.

I started looking around on how to do this, and came across the [inspect](https://docs.python.org/3/library/inspect.html) module. 
If you look under the `code` Type, you can see the `co_varnames` and that it will give you:
> tuple of names of arguments and local variables
This is exactly what I'm looking for.

Let's set up some code that sees if `arg2` is an argument in `MyFunkyClass.internal_method`:
```python
# Import the Class 
from funky import MyFunkyClass

# Get a pointer to the class method
method = getattr(MyFunkyClass, 'internal_method')

# Chceck if arg2 is an argument
assert 'arg2' in method.__code__.co_varnames
```

That's it. Pretty simple.

