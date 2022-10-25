# InventWithPython
# Python Gently book

filename = "Ex"
for i in range(12, 43):
    filename = "Ex" + str(i) + ".py"
    with open(filename, 'a') as f:
        f.write(f"(print(Ex{str(i)} done))")