import base64

string = input("Input: ")
decoded = base64.b64decode(string)
print(decoded.decode('utf-8'))