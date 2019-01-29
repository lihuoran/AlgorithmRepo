import bisect

class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keylist = {} # {key: [timestamps]}
        self.keyval = {} # {key: {timestamp: value}}

    def set(self, key: 'str', value: 'str', timestamp: 'int') -> 'None':
        if key not in self.keylist:
            self.keylist[key] = []
            self.keyval[key] = {}
        bisect.insort_right(self.keylist[key], timestamp)
        self.keyval[key][timestamp] = value

    def get(self, key: 'str', timestamp: 'int') -> 'str':
        if key not in self.keylist or timestamp < self.keylist[key][0]:
            return ''

        idx = bisect.bisect_right(self.keylist[key], timestamp)
        return self.keyval[key][self.keylist[key][idx - 1]]
