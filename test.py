path = "pw.txt"  # path to filename

def get_CP():
    pw = open(path, "r")
    line = pw.readline()
    pw.close()
    return line

passord = get_CP()
pas = "passord"

def change_pw(password):
    password = str(password)
    pw = open(path, "w")
    pw.write(password)
    pw.close()



change_pw(12442)
print(get_CP())


print("----------")

a = "1"
b = "4"

print(a)
print(b)

print("----------")

c = a + b

print(c)
print(int(c))