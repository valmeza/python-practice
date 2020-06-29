# This is a comment
# python basics

add = 2 + 2
print(add)

sub = 2 - 2
print(sub)

more_math = 59 - 5 * 3
print(more_math)

floating = 8 / 5
print(floating)

squared = 5 ** 2
print(squared)

width = 20
height = 5 * 9
print(width * height)

l = "something"
print(l)

print('Hello World!')
print("Hello with double quotes")
print("Py" "thon")

print(3 * "un" + "ium")

word = "Crazy Eyes"
print(word[-1])
print(word[0:2])
print(word[-2:])

print(len(word))

long = "supercalifragilisticexpialidocious"
print(len(long))

squares = [1, 4, 8, 16, 25]
print(squares)

print(squares[0])
print(squares[1])

adding = squares + [1, 2, 34]
print(adding)

letters = ["a", "b", "c", "d", "e", "f", "g"]
print("Original Array: ", letters)

letters[2:5] = ["C", "D", "E"]
print("After replacing values: ", letters)

print("Length:", len(letters))

a = ["a", "b", "c"]
n = [1, 3, 44]
x = [a, n]
print("Nested Arrays:", x[0][1])

a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b
