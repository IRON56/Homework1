# Contains helper functions for your apps!
from os import listdir, remove

# If the io following files are in the current directory, remove them!
# 1. 'currency_pair.txt'
# 2. 'currency_pair_history.csv'
# 3. 'trade_order.p'
def check_for_and_del_io_files():
    # Your code goes here.
    path = "C:\\Users\\Administrator\\Desktop\\Homework1\\"
    dirs = listdir(path)
    for file in dirs:
        #print(file)
        if file == "currency_pair.txt":
            remove(file)
        if file == "currency_pair_history.csv":
            remove(file)
        if file == "trade_order.p":
            remove(file)

    pass # nothing gets returned by this function, so end it with 'pass'.