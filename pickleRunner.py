pickle_file = open("./src/main/resources/hashes.pickle", "rb")
objects = []
while True:
    try:
        objects.append(pickle.load(pickle_file))
    except EOFError:
        break
pickle_file.close()

print(objects)