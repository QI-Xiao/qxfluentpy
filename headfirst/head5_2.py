def sanitize(time_string):
    if '-' in time_string:
        spl = '-'
    elif ':' in time_string:
        spl = ':'
    else:
        return time_string
    (mins, secs) = time_string.split(spl)
    return mins + '.' + secs


class AthleteList(list):
    def __init__(self, aname, dob=None, a_times=[]):
        list.__init__([])
        self.name = aname
        self.dob = dob
        self.extend(a_times)

    def top3(self):
        return sorted(set([sanitize(t) for t in self]))[0:3]

vera = AthleteList('vearvi')
vera.append('1.31')
print(vera.top3())
vera.extend(['2.22','1-21','2:22'])
print(vera.top3())