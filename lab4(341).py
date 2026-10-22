a = input()
b = input()


start_code = ord(a)
end_code = ord(b)

for code in range(start_code, end_code + 1):

    print(chr(code), end="")