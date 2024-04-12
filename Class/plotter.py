import os
import matplotlib.pyplot as plt
import pandas as pd

class Plotter:
    def draw_plots(self, json_file_path):
        plot_paths = []
        data = pd.read_json(json_file_path)
        for column in data.columns:
            if pd.api.types.is_numeric_dtype(data[column].dtype):
                plt.figure()
                data[column].plot()
                plt.title(column)
                plot_path = os.path.join('plots', f'{column}.png')
                plt.savefig(plot_path)
                plt.close()
                plot_paths.append(plot_path)
        return plot_paths
