try:
    with open('ama.txt', 'r') as f:
        data = f.read()
        print(data)
except FileNotFoundError:
    print("An error occurred while reading 'sample.txt'.")
