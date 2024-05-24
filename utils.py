def string_to_bin(s):
  out = ""

  for i in s:
    out += bin(i)[2:].rjust(8, "0")

  return out

"""
x = open("testfile.txt", "rb").read()
print(string_to_bin(x))
"""