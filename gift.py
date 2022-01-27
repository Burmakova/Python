class Gift(object):
    def __init__(self, length=0, width=0, height=0):
        self.width = width
        self.height = height
        self.length = length

    def wrapping_paper(self):
        sides = [
            self.width * self.length, self.height * self.length,
            self.width * self.height
        ]
        minimal = min(sides)
        return sum(sides) * 2 + minimal

    def wrapping_ribbon(self):
        sides = [self.width, self.height, self.length]
        sides.sort()
        return (sides[0] +
                sides[1]) * 2 + self.width * self.length * self.height

    def __str__(self):
        return f"{self.length}x{self.width}x{self.height}"


def read_gifts(file):
    # Using readlines()
    input_txt = open(file, 'r')
    Lines = input_txt.readlines()

    input_txt.close()
    gifts = []
    # Strips the newline character
    for line in Lines:
        sizes = line.split('x')
        gifts.append(Gift(int(sizes[0]), int(sizes[1]), int(sizes[2])))

    return gifts


def write_gifts(file, array):
    # Using readlines()
    output_txt = open(file, 'w')

    output_txt.writelines(array)

    output_txt.close()


def to_fstring(gift):
    return f"{gift}\n"


def to_string(gift):
    return f"{gift}"


gifts_array = read_gifts('input.txt')
result = list(map(to_fstring, gifts_array))
terminal_result = list(map(to_string, gifts_array))
print(terminal_result)
write_gifts('output.txt', result)
