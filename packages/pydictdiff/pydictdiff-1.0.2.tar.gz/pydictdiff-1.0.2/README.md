# pyDictDiff

Visit [https://pypi.org/project/pydictdiff/](https://pypi.org/project/pydictdiff/)

This is a dictionary diff package for python.

### Installation

These instructions will get you a copy of the package up and running on your terminal for development and testing purposes.

To install, type:

```
pip install pydictdiff
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
Access the differences through variable "result"
```
>>> x.result
{
  "A": {
    "[-]": "B",
    "[+]": "X"
  },
  "C": {
    "D": {
      "[-]": "E",
      "[+]": "Y"
    }
  }
}
```

### Future work:
* Support for arrays