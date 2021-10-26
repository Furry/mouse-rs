import matplotlib.pyplot as plt
import matplotlib as mpl

grid = plt.plot()
# Create a function that reads a file line by line. Split the line by '-', then split each segment by ',' and return the results.
def read_file(filename):
    with open(filename) as file:
        data = file.read()
        data_list = data.split("-")
        data_list = [i.split(",") for i in data_list]
        return data_list
    #END
#END

for pair in read_file("doc.txt"):
    plt.scatter(int(pair[0]), int(pair[1]))
#END

# print(read_file("doc.txt"))

plt.show()