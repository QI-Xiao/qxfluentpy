def sanitize(time_string):
    if '-' in time_string:
        spl = '-'
    elif ':' in time_string:
        spl = ':'
    else:
        return time_string
    (mins, secs) = time_string.split(spl)
    return mins + '.' + secs

class Athlete:
    def __init__(self, aname, dob=None, times=[]):
        self.name = aname
        self.dob = dob
        self.times = times

    def top3(self):
        return sorted(set([sanitize(t) for t in self.times]))[0:3]

    def add_time(self, time_value):
        self.times.append(time_value)

    def add_times(self, times_list):
        self.times += times_list

def opentxt(filename):
    try:
        with open(filename) as file:
            data = file.readline()
        templ = data.strip().split(',')
        return Athlete(templ.pop(0), templ.pop(0), templ)
    except IOError as err:
        print('file error:', err)
        return None


sarah = opentxt(r'head/sarah2.txt')
print(sarah.name, str(sarah.top3()))

vera = Athlete('vera')
vera.add_time('1.21')
print(vera.top3())


class NamedList(list):
    def __init__(self, a_name):
        list.__init__([])
        self.name = a_name
