import os

manifest_dir = "manifest/"

dir_exists = os.path.exists(manifest_dir)

# skip if manifest dir exists
if dir_exists:
    pass

# create manifest dir if it doesn't yet exist
else:
    os.mkdir("manifest/")

with open("manifest/test.txt", "w") as file:
    file.write("Directory contents:")
    file.write("\n")
    for f in os.listdir("test-dir/"):
        file.write(f"{f}\n")

