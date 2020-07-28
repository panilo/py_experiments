# Inheritance and compositions 

## Inheritance 
Inheritance models what is called an **is a** relationship. This means that when you have a Derived class that inherits 
from a Base class, you created a relationship where Derived is a specialized version of Base.

Derived classed extends Base classes. 

Note: In an inheritance relationship:

- Classes that inherit from another are called derived classes, subclasses, or subtypes.
- Classes from which other classes are derived are called base classes or super classes.
- A derived class is said to derive, inherit, or extend a base class.

### Example

Let’s say you have a base class _Animal_ and you derive from it to create a _Horse_ class. The inheritance relationship 
states that a Horse **is an** Animal. This means that Horse inherits the interface and implementation of Animal, 
and Horse objects can be used to replace Animal objects in the application.

This is known as the Liskov substitution principle. The principle states that “in a computer program, if S is a subtype 
of T, then objects of type T may be replaced with objects of type S without altering any of the desired properties 
of the program”.

### Overview of Inheritance in Python 

Everything in Python is an object. Modules are objects, class definitions and functions are objects, and of course, 
objects created from classes are objects too.

Inheritance is a required feature of every object oriented programming language. This means that Python 
supports inheritance and it’s one of the few languages that supports **multiple inheritance**.

When you write Python code using classes, you are using inheritance even if you don’t know you’re using it.

```python
class MyClass: 
    pass

def test():
    c = MyClass()
    dir(c)    
```

```
# Output from dir(c)

['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
'__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
'__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
'__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
'__str__', '__subclasshook__', '__weakref__']
```

dir() returns a list of all the members in the specified object. MyClass have not declared any members, so all these
member actually come from object(). This is because every class defined in Python implicitly derives from `object`. 
The last statement is always true except for Exceptions.

```python
def test():
    o = object()
    dir(o)    
```

```
# Output from dir(o)

['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__',
'__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
'__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__',
'__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
'__subclasshook__']
```

In Python an Exception must derive from BaseException 

```python
class MyErrorNotDerivingFromBaseExc:
    pass

raise MyErrorNotDerivingFromBaseExc()
    
class MyError(Exception):
    pass

raise MyError()
```

```
# MyErrorNotDerivingFromBaseExc
# The following is a Runtime error because my class doesn't derive from BaseException 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: exceptions must derive from BaseException

# MyError
# This error has been raised by MyError
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
__main__.MyError
```

## Compositions
Composition is a concept that models a **has a** relationship. It enables creating complex types by combining objects of 
other types. This means that a class Composite can contain an object of another class Component. This relationship means 
that a Composite has a Component. Classes that contain objects of other classes are usually referred to as composites, 
where classes that are used to create more complex types are referred to as components.

For example, Horse class can be composed by another object of type Tail. Composition allows you to express that 
relationship by saying a Horse **has a** Tail.

Composition enables you to reuse code by adding objects to other objects, as opposed to inheriting the interface and 
implementation of other classes. Both _Horse_ and _Dog_ classes can leverage the functionality of Tail through composition 
without deriving one class from the other

### Composition in Python 
Composition is an object oriented design concept that models a has a relationship. In composition, 
a class known as composite contains an object of another class known to as component. In other words, 
a composite class has a component of another class.

If you look at the Employee class, you’ll see that it contains two attributes:

- id to identify an employee.
- name to contain the name of the employee.

These two attributes are objects that the Employee class has. Therefore, you can say that an Employee **has an** id and 
**has a** name.

Composition is more flexible than inheritance because it models a loosely coupled relationship. 
Changes to a component class have minimal or no effects on the composite class. Designs based on composition are more 
suitable to change.

#### Composition to Change Run-Time Behavior
Inheritance, as opposed to composition, is a tightly couple relationship. With inheritance, there is only one way to 
change and customize behavior. Method overriding is the only way to customize the behavior of a base class. This creates 
rigid designs that are difficult to change.

Composition, on the other hand, provides a loosely coupled relationship that enables flexible designs and can be used to 
change behavior at run-time.


