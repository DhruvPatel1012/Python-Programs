import random
passlen = int(input("enter the length of password"))
samp ="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*?"
password =  "".join(random.sample(samp,passlen ))
print(password)