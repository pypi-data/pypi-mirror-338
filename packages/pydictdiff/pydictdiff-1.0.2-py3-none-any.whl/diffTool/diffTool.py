
#!/usr/bin/env python3

class Diff:

    def __init__(self, p, q, exclude = []):

        self.d1, self.d2 = p, q
        self.exclude = exclude
        self.result = self.process()  # Driver


    # Calculate diffs between d1, d2
    def process(self) -> dict:
        def recurse(d1, d2):
            diff = {}
            
            # Keys in d1 but not in d2
            for key in d1:
                if key in self.exclude:  # skip excluded keys
                    continue
                if key not in d2:
                    diff[key] = {"[-]": d1[key]}
                elif isinstance(d1[key], dict) and isinstance(d2[key], dict):
                    nested_diff = recurse(d1[key], d2[key])
                    if nested_diff:
                        diff[key] = nested_diff
                elif d1[key] != d2[key]:
                    diff[key] = {"[-]": d1[key], "[+]": d2[key]}
            
            # Keys in d2 but not in d1
            for key in d2:
                if key in self.exclude:  # skip excluded keys
                    continue
                if key not in d1:
                    diff[key] = {"[+]": d2[key]}
            return diff
        return recurse(self.d1, self.d2)


# my whiteboard
if __name__ == "__main__":
    d1 = {
        "A": "B",
        "C": {
            "D": "E"
        }
    }
    d2 = {
        "A": "X",
        "C": {
            "D": "Y"
        }
    }
    x = Diff(d1, d2)
    ret = x.process()
    print(ret)
