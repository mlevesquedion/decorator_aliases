# Python experiment : declaring function aliases with a decorator

Just curious whether this could be done in a nice way. The answer appears to be no. I do not recommend actually doing this.

To define aliases, just assign your function to extra variables, e.g. :

```python
def mean(lst):
    return sum(lst) / len(lst)

avg = mean
average = mean
```

## Credits

Idea to use inspect taken from here : https://mail.python.org/pipermail/python-list/2013-November/659992.html

## Inspiration

Inspired by https://martinfowler.com/bliki/HumaneInterface.html