import matplotlib.pyplot as plt
from collections import defaultdict


def plot_table():
    pass


def plot_graphs():
    pass


def arrange_data(x_stuff, y_stuff):
    pass


def decode(file):
    params_tmp, outc_tmp = [line.split(':') for line in file]
    parameters = defaultdict(lambda: ())

    
    for parameter in parameters:
        [parameter[0]] = parameter[1:]

    param_names, outcome_names = [], []
    param_vals, outcome_vals = [], []
    
    parameters = parameters.split(',')[::2]
    outcomes = outcomes.split(',')


def main():
    data = {}
    with open("./results/vary_ruu_size.txt") as file:
        x_vals, y_vals = decode(file)

    arranged_data = arrange_data(x_vals, y_vals)
    
    # Plotting the lines with labels
    for label, (x, y) in :
        plt.plot(x, y, label = label)

    # Adding legend, x and y labels, and title for the lines
    plt.legend()
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Multiple Line Plot')
    # Displaying the plot
    plt.show()


if __name__ == "__main__":
    main()
