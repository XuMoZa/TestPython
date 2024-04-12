import pandas as pd
from Class.plotter import Plotter



def draw_plots(json_file_path):
    plotter = Plotter()
    return plotter.draw_plots(json_file_path)


json_file_path = 'static/Test.json'
plot_paths = draw_plots(json_file_path)
print(plot_paths)
