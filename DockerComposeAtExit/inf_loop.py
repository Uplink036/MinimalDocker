import atexit

def teardown():
    with open("aFile.txt", "w"):
        pass
    print("Goodbye World!", flush=True)

atexit.register(teardown)
loop = 0
while True:
    print(f"{loop=}", flush=True)
    loop += 1