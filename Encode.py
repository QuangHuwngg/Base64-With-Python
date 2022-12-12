import base64

string = input("Input: ")
string_encode = string.encode('utf-8')
encoded = base64.b64encode(string_encode)
print(encoded)