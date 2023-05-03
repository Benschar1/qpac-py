
def strip_nl(line):
    return line.rstrip("\n")

def is_blank(line):
    return len(strip_nl(line)) == 0

def parse_list(file_iter):
    list = []

    while True:
        try:
            line = next(file_iter)
            if is_blank(line):
                return list
            else:
                list.append(strip_nl(line))

        except StopIteration:
            return list

class NotAProperty(Exception):
    pass

class EndOfFile(Exception):
    pass

#returns next property name, leaves iterator right after that line
#consumes blank lines
#if finds a line that isn't a property or reaches end of file, throws exception
def next_property(file_iter):
    while True:
        try:
            line = strip_nl(next(file_iter))
            if is_blank(line):
                continue
            elif line.startswith("%") and line.endswith("%"):
                return line[1:-1]
            else:
                raise NotAProperty(line)
        except StopIteration:
            raise EndOfFile()

def parse_desc_file(path):
    with iter(open(path, "r")) as file_iter:
        props = {}
        cur_prop = 0
        while True:
            try:
                cur_prop = next_property(file_iter)
                vals = parse_list(file_iter)
                props[cur_prop] = vals
            except EndOfFile:
                return props

path = "/var/lib/pacman/local/zoom-5.14.5-1/desc"

