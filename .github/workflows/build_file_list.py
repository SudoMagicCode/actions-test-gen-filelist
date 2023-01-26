import os

print("Directory contents:")
os.mkdir("manifest/")
with open("manifest/test.txt", "a") as file:
    for f in os.listdir():
        file.write(f"{f}\n")

