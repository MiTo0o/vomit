from setuptools import setup

setup(
  name="vomit",
  version="0.02",
  description="The new pop()",
  url="https://github.com/MiTo0o",
  author="MiTo",
  author_email="derzanchiang1800@gmail.com",
  license="MIT",
  packages=["vomit"],
  zip_safe=False,
  long_description="""
# vomit
________
Don't like using .pop() because it looks weird?

LOOK NO FURTHER

The vomit package contains a vomit() function which does the same thing as
.pop(). If you really think about it, when you pop and element from a stack (Last One First Out)
it's basically vomitting.


## install
    pip install vomit

If that doesnt work try:

    pip3 install vomit

## usage

```py
from vomit import vomit
stack = [1, 2, 3, 4, 5]

puke = vomit(stack)
# puke = 5

# stack = [1, 2, 3, 4]
```
  """,
  long_description_content_type='text/markdown'
)