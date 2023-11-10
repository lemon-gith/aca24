import matplotlib.pyplot as plt
from collections import defaultdict
import os
from icecream import ic

#region helper functions
def plot_table():
    pass


def entries_to_tuple_list(data_list):
    data_tuple_list = []
    for row in data_list:
        for datapoint in row.split(';'):
            if not datapoint:
                continue
            split_dp = datapoint.split(',')
            tup = []
            tup.append(split_dp[0])
            if split_dp[1:]:
                tup.extend(list(map(float, split_dp[1:])))
            data_tuple_list.append(tuple(tup))

    return data_tuple_list

def decode(file, keep=(None, None)):
    """
    takes in a file formatted as:\n
    param_name,data;param_name,data:output_name,data;output_name,data\n\n
    `keep` == None, means keep all values\n
    `keep`: ({<name of param>, <...>},{<name of outcome>, <...>})
    `keep`: (None,{<name of outcome>, <...>}), to keep all parameters
    """
    tmp = [line.strip().split(':') for line in file]
    params_rows = [entry[0] for entry in tmp]
    outc_rows = [entry[1] for entry in tmp]


    param_tuples = entries_to_tuple_list(params_rows)
    outc_tuples = entries_to_tuple_list(outc_rows)

    parameters = defaultdict(lambda: [])
    outcomes = defaultdict(lambda: [])

    if keep[0]:
        for param in param_tuples:
            if param[0] in keep[0]:
                parameters[param[0]].append(param[1:])
    else:
        for param in param_tuples:
            parameters[param[0]].append(param[1:])
    
    if keep[1]:
        for outc in outc_tuples:
            if outc[0] in keep[1]:
                outcomes[outc[0]].append(outc[1:])
    else:
        for outc in outc_tuples:
            outcomes[outc[0]].append(outc[1:])

    return parameters, outcomes
#endregion


#region to modify as needed
def process_data(x_stuffs, y_stuffs):
    """
    just makes 3 nice little dictionaries, raising errors when there are errors to raise :)))
    """
    if len(x_stuffs) > 2:
        raise ValueError("x_stuffs is too large :/")
    
    d1 = list(x_stuffs.values())[0]
    d2 = list(x_stuffs.values())[1]
    if len(y_stuffs) > 1:
        raise ValueError("x_stuffs is too large :/")
    return (d1, d2, list(y_stuffs.values())[0])


def plot_3d(plot_name, x_stuff, y_stuff, save=False):
    from matplotlib import cm
    #from matplotlib.ticker import LinearLocator
    import numpy as np

    if save:
        script_dir = os.path.dirname(__file__)
        save_file_path = os.path.join(script_dir, f"images/{plot_name}.png")

    data = process_data(x_stuff, y_stuff)
    
    from mpl_toolkits import mplot3d
    import numpy as np
    import matplotlib.pyplot as plt
    
    # defining all 3 axis
    x = np.array(data[0])
    y = np.array(data[1])
    z = np.array(data[2])

    fig = plt.figure()
    ax = plt.axes(projection ='3d')
    c = x + y
    #ax.scatter(x, y, z, c=c)
    ax.plot3D(x, y, z, c='purple')
    ax.set_title('line');
    ax.set_xlabel('ruu_size', fontsize=12)
    ax.set_ylabel('lsq_size', fontsize=12)
    ax.set_zlabel('total_energy', fontsize=12)

    plt.savefig(save_file_path) if save else plt.show()


line_colours = ['y', 'c', 'b', 'r', 'g', 'm', 'k']
def plot_sep_param_graphs(plot_name, x_stuff, y_stuff, save=False):
    if save:
        script_dir = os.path.dirname(__file__)
        save_file_path = os.path.join(script_dir, f"images/{plot_name}")

    figure_number = 1
    for x_label, x_values in x_stuff.items():
        plt.close()
        plt.figure(figure_number)
        colour_index = 0
        for y_label, y_values in y_stuff.items():
            plt.plot(x_values, y_values, label=y_label, marker='o', 
                     color=line_colours[colour_index])
            colour_index += 1

        plt.xscale('log', base=2)
        plt.legend()
        plt.xlabel(x_label)
        plt.ylabel("Performance") if len(y_stuff) > 1 else plt.ylabel(list(y_stuff.keys())[0])
        plt.title(f"Plot of {x_label} for {plot_name.split('-')[1]}")
        plt.savefig(save_file_path + (f"_fig{figure_number}.png" 
                    if len(y_stuff) > 1 else ".png")) if save else plt.show()
        figure_number += 1


def plot_sep_outc_graphs(plot_name, x_stuff, y_stuff, save=False):
    if save:
        script_dir = os.path.dirname(__file__)
        save_file_path = os.path.join(script_dir, f"images/{plot_name}")

    figure_number = 1
    for y_label, y_values in y_stuff.items():
        plt.close()
        plt.figure(figure_number)
        colour_index = 0
        for x_label, x_values in x_stuff.items():
            plt.plot(x_values, y_values, label=x_label, marker='o', 
                     color=line_colours[colour_index])
            colour_index += 1
            
        plt.xscale('log', base=2)
        plt.legend()
        plt.xlabel("Parameters") if len(x_stuff) > 1 else plt.xlabel(list(x_stuff.keys())[0])
        plt.ylabel(y_label)
        plt.title(f"Plot of {y_label} for {plot_name.split('-')[1]}")
        plt.savefig(save_file_path + (f"_fig{figure_number}.png" 
                    if len(x_stuff) > 1 else ".png")) if save else plt.show()
        figure_number += 1


def main():
    filename = "intro-vary_2params"
    script_dir = os.path.dirname(__file__)
    abs_file_path = os.path.join(script_dir, f"results/{filename}.txt")

    keep = ({},{'total_power_cycle_cc1'})

    with open(abs_file_path, 'r') as file:
        x_vals, y_vals = decode(file, keep)

    #plot_sep_outc_graphs(filename, x_vals, y_vals, save=True)
    #plot_sep_param_graphs(filename, x_vals, y_vals, save=True)
    plot_3d(filename, x_vals, y_vals, save=False)

#endregion

if __name__ == "__main__":
    main()

