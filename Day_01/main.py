def sum_by_two(input):
    for i, x in enumerate(input):
            for y in input[i:]:
                if x + y == sum:
                    return str(x * y)

def sum_by_three(input):
    for i, x in enumerate(input):
        for j, y in enumerate(input[i:]):
            for z in input[j:]:
                if x + y + z == sum:
                    return "{0} * {1} * {2} = {3}".format(x, y, z, x*y*z)

def find_zero(input):
    for x in input:
        if int(x) == 0:
            return True
    return False

f = open("input.txt", "r")
input = []
sum = 2020
for entry in f:
    input.append(int(entry))

print(sum_by_two(input))
print(sum_by_three(input))

# debugging for a typescript friend
print(find_zero(input))
