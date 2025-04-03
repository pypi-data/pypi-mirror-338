# pyDictDiff

Visit [https://test.pypi.org/project/diffTool/](https://test.pypi.org/project/diffTool/)

This is a dictionary diff package for python.

### Installation

These instructions will get you a copy of the package up and running on your terminal for development and testing purposes.

To install, type:

```
pip install -i https://test.pypi.org/simple/ diffTool
```

Alternatively, to clone (with HTTPS):
```
git clone https://gitlab.com/anupamkrish/pydictdiff.git
```
or (with SSH):
```
git clone git@gitlab.com:anupamkrish/pydictdiff.git
```

### Usage

Import the package
```
>>> from diffTool import Diff
```
Instantiate the class
```
>>> x = Diff(
        {
            "A": "B",
            "C": {
                "D": "E"
            }
        },
        {
            "A": "X",
            "C": {
                "D": "Y"
            }
        }
    )
```
Access the differences through variable 'diffs'
```
>>> x.diffs
[
  {
    "A": {
      "[-]": "B",
      "[+]": "X"
    }
  },
  {
    "C -> D": {
      "[-]": "E",
      "[+]": "Y"
    }
  }
]
```

### Caveat(s):

* Does not detect elements not present in 2nd dictionary.

### Future work:

* Resolve caveat
* Support for arrays
* Strict option i.e. checks for order
* Return single dictionary
* Improved speed for large dictionaries
