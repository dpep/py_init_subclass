init_subclass
======
Backwards compatibility for Python 3
[\_\_init_subclass\_\_](https://docs.python.org/3/reference/datamodel.html#object.__init_subclass__)


### Install
```pip install init_subclass```


### Usage
```
class Philosopher(InitSubclass):
    subclasses = []

    def __init_subclass__(cls):
        Philosopher.subclasses.append(cls.__name__)


class Socrates(Philosopher):
    pass
class Plato(Philosopher):
    pass


print Philosopher.subclasses
=> ['Socrates', 'Plato']
```
