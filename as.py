# initialise empty layers
second_layer = []
layer = []


# Chek if solution exists
def not_solution(first_layer):
    for m in range(len(first_layer)):
        for n in range(len(first_layer[0])):
            if m == 0 and n == 0:
                if first_layer[m][n] != first_layer[m][n + 1] and first_layer[m + 1][n] != first_layer[m][n]:
                    return True
            elif m == 0 and n == len(first_layer[0]) - 1:
                if first_layer[m][n] != first_layer[m][n - 1] and first_layer[m + 1][n] != first_layer[m][n]:
                    return True
            elif m == 0 and n in range(1, len(first_layer[0]) - 1):
                if first_layer[m][n] != first_layer[m][n + 1] and first_layer[m + 1][n] != \
                        first_layer[m][n] and first_layer[m][n - 1] != \
                        first_layer[m][n]:
                    return True
            elif m == len(first_layer) - 1 and n == 0:
                if first_layer[m][n] != first_layer[m][n + 1] and first_layer[m][n] != first_layer[m - 1][n]:
                    return True
            elif m == len(first_layer) - 1 and n == len(first_layer[0]) - 1:
                if first_layer[m][n] != first_layer[m][n - 1] and first_layer[m][n] != first_layer[m - 1][n]:
                    return True
            elif m == len(first_layer) - 1 and n in range(1, len(first_layer[0]) - 1):
                if first_layer[m][n] != first_layer[m][n - 1] and first_layer[m][n] !=\
                        first_layer[m - 1][n] and first_layer[m][n] != first_layer[m][n + 1]:
                    return True
            elif m in range(1, len(first_layer) - 1):
                if n == 0:
                    if first_layer[m][n] != first_layer[m][n + 1] and first_layer[m][n] != first_layer[m + 1][n]:
                        if first_layer[m][n] != first_layer[m - 1][n]:
                            return True
                elif n == len(first_layer[0]) - 1:
                    if first_layer[m][n] != first_layer[m][n - 1] and first_layer[m][n] != first_layer[m + 1][n]:
                        if first_layer[m][n] != first_layer[m - 1][n]:
                            return True
                else:
                    if first_layer[m][n] != first_layer[m][n + 1] and first_layer[m][n] != first_layer[m][n - 1]:
                        if first_layer[m][n] != first_layer[m + 1][n] and first_layer[m][n] != first_layer[m - 1][n]:
                            return True


# Validate the input
def validate_input(first_layer, m, n):
    if len(first_layer) == m \
            and m < 100 and n < 100 \
            and m % 2 == 0 and n % 2 == 0:
        for z in first_layer:
            if len(z) != n:
                return False
        return True
    return False


# Create second layer with zeros
def fill_second_layer_with_0_s(rows, cols):
    for x in range(rows):
        second_layer.append([])
        for _ in range(cols):
            second_layer[x].append(0)
    return second_layer


# Validate there are no bricks spanning over 3 rows/columns or there are no more than 2 identical characters
def validate_bricks(iterable: list):
    iterable = iterable[0] + iterable[1]
    for x in iterable:
        occurrences = iterable.count(x)
        if occurrences > 2:
            print('Something went wrong. There\'re bricks spanning over 3 rows/columns!')
            quit()
        elif occurrences == 1:
            print('-1\n No solution exists.')
            quit()


# print the output shown on the pdf file. No asterisks ot dashes added.
def print_output(result):
    for x in result:
        print(' '.join([str(i) for i in x]), sep='\n')


# Input of the first layer. Casting the chars to integers
lines, columns = [int(x) for x in input('>:').split(" ")]
for x in range(int(lines)):
    layer.append([int(x) for x in input('>:').split()])

# Verify the input is correct, if not print the message and quit the programme
if not validate_input(layer, lines, columns):
    print('The input should be numbers less then 100 and even ')
    quit()

# Creating list with the available bricks
bricks = [x for x in range(((lines * columns) // 2), 0, -1)]

# Take the fist brick
brick = bricks.pop()
second_layer = fill_second_layer_with_0_s(lines, columns)
validate_bricks(layer)

if not_solution(layer):
    print('-1\n No solution exits.')
    quit()

for x in range(lines):
    for y in range(0, columns):
        try:
            if y != columns - 1:
                if layer[x][y] == layer[x][y + 1]:

                    if second_layer[x][y] != 0:
                        continue

                    second_layer[x][y] = brick
                    second_layer[x + 1][y] = brick
                    if len(bricks) > 0:
                        brick = bricks.pop()
                    else:
                        break
                else:
                    if second_layer[x][y] != 0:
                        continue
                    second_layer[x][y] = brick
                    second_layer[x][y + 1] = brick
                    if len(bricks) > 0:
                        brick = bricks.pop()
                    else:
                        break

            else:
                if second_layer[x][y] != 0:
                    continue
                if second_layer[x + 1][y] == 0:
                    second_layer[x][y] = brick
                    second_layer[x + 1][y] = brick
                    if len(bricks) > 0:
                        brick = bricks.pop()
                    else:
                        break
        except IndexError:
            print('-2 \n No solution exist.')
validate_bricks(second_layer)
print_output(second_layer)
