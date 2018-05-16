init_subclass
======
Add Python 2 backwards compatibility for
object.__init_subclass__

https://docs.python.org/3/reference/datamodel.html#object.__init_subclass__


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
