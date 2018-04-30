import re

def common_prefix(a, b):
    i = 0
    while i < min(len(a), len(b)):
        if a[i] != b[i]:
            break
        i += 1
    return a[:i]

class _RetrieNode:
    def __init__(self, value, terminal=True, children=None):
        self.value = value
        self.terminal = terminal
        if children:
            self.children = children
        else:
            self.children = []

    def add(self, new_str):
        common = common_prefix(self.value, new_str)
        assert common
        if common != self.value:
            # split this node into a new one with a child
            self.children = [
                    _RetrieNode(
                        self.value[len(common):],
                        self.terminal,
                        self.children)]
            self.value = common
            self.terminal = False
        if common != new_str:
            # self.children.append(_RetrieNode(new_str[len(common):]))
            remainder = new_str[len(common):]
            for child in self.children:
                if child.value[0] == remainder[0]:
                    child.add(remainder)
                    return
            self.children.append(_RetrieNode(remainder))
        else:
            self.terminal = True

    def regex_str(self):
        re_str = re.escape(self.value)
        if self.children:
            re_str += '(?:'
            re_str += '|'.join(child.regex_str() for child in self.children)
            re_str += ')'
            if self.terminal:
                re_str += '?'
        return re_str

    def __repr__(self):
        return '<Retrie value=%r terminal=%r children=%r>' % (
                self.value if hasattr(self, 'value') else '?',
                self.terminal if hasattr(self, 'terminal') else '?',
                self.children if hasattr(self, 'children') else '?')

class Retrie:
    def __init__(self, *args):
        self.roots = []
        for new_str in args:
            self.add(new_str)

    def add(self, new_str):
        for root in self.roots:
            if root.value[0] == new_str[0]:
                root.add(new_str)
                return
        self.roots.append(_RetrieNode(new_str))

    def regex_str(self):
        re_str = '|'.join(root.regex_str() for root in self.roots)
        return re_str

    def regex(self):
        return re.compile(self.regex_str())

    def __repr__(self):
        return '<Retrie roots=%r>' % self.roots

