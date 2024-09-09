import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
import tkinter as tk

class GPSVis(object):
    """
    Class for GPS data visualization using pre-downloaded OSM map in image format.
    """
    def __init__(self, data_path, map_path, points):
        """
        :param data_path: Path to file containing GPS records.
        :param map_path: Path to pre-downloaded OSM map in image format.
        :param points: Upper-left, and lower-right GPS points of the map (lat1, lon1, lat2, lon2).
        """
        self.data_path = data_path
        self.points = points
        self.map_path = map_path

        self.result_image = Image
        self.x_ticks = []
        self.y_ticks = []

    def plot_map(self, output='save', save_as='resultMap.png'):
        """
        Method for plotting the map. You can choose to save it in file or to plot it.
        :param output: Type 'plot' to show the map or 'save' to save it.
        :param save_as: Name and type of the resulting image.
        :return:
        """
        self.get_ticks()
        fig, axis1 = plt.subplots(figsize=(10, 10))
        axis1.imshow(self.result_image)
        axis1.set_xlabel('Longitude')
        axis1.set_ylabel('Latitude')
        axis1.set_xticklabels(self.x_ticks)
        axis1.set_yticklabels(self.y_ticks)
        axis1.grid()
        if output == 'save':
            plt.savefig(save_as)
        else:
            plt.show()

    def create_image(self, color, width=2):
        """
        Create the image that contains the original map and the GPS records.
        :param color: Color of the GPS records.
        :param width: Width of the drawn GPS records.
        :return:
        """
        data = pd.read_csv(self.data_path, names=['LATITUDE', 'LONGITUDE'], sep=',')

        self.result_image = Image.open(self.map_path, 'r')
        img_points = []
        gps_data = tuple(zip(data['LATITUDE'].values, data['LONGITUDE'].values))
        for d in gps_data:
            x1, y1 = self.scale_to_img(d, (self.result_image.size[0], self.result_image.size[1]))
            img_points.append((x1, y1))
        draw = ImageDraw.Draw(self.result_image)
        draw.line(img_points, fill=color, width=width)

    def scale_to_img(self, lat_lon, h_w):
        """
        Conversion from latitude and longitude to the image pixels.
        It is used for drawing the GPS records on the map image.
        :param lat_lon: GPS record to draw (lat1, lon1).
        :param h_w: Size of the map image (w, h).
        :return: Tuple containing x and y coordinates to draw on map image.
        """
        old = (self.points[1], self.points[0])
        new = (0, h_w[1])
        y = ((lat_lon[0] - old[0]) * (new[1] - new[0]) / (old[1] - old[0])) + new[0]
        old = (self.points[1], self.points[3])
        new = (0, h_w[0])
        x = ((lat_lon[1] - old[0]) * (new[1] - new[0]) / (old[1] - old[0])) + new[0]
        # y must be reversed because the orientation of the image in the matplotlib.
        # image - (0, 0) in upper left corner; coordinate system - (0, 0) in lower left corner
        return int(x), h_w[1] - int(y)

    def get_ticks(self):
        """
        Generates custom ticks based on the GPS coordinates of the map for the matplotlib output.
        :return:
        """
        self.x_ticks = map(
            lambda x: round(x, 4),
            np.linspace(self.points[1], self.points[3], num=7))
        y_ticks = map(
            lambda x: round(x, 4),
            np.linspace(self.points[2], self.points[0], num=8))
        # Ticks must be reversed because the orientation of the image in the matplotlib.
        # image - (0, 0) in upper left corner; coordinate system - (0, 0) in lower left corner
        self.y_ticks = sorted(y_ticks, reverse=True)

    def draw_points(self, points, color='red', radius=3):
        """
        Draw points on the map.
        :param points: List of tuples containing latitude and longitude of the points.
        :param color: Color of the points.
        :param radius: Radius of the points.
        :return:
        """
        draw = ImageDraw.Draw(self.result_image)
        for point in points:
            x, y = self.scale_to_img(point, (self.result_image.size[0], self.result_image.size[1]))
            draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=color)

    def draw_line(self, start_point, end_point, color='green', width=2):
        """
        Draw a line between two points on the map.
        :param start_point: Tuple containing latitude and longitude of the start point.
        :param end_point: Tuple containing latitude and longitude of the end point.
        :param color: Color of the line.
        :param width: Width of the line.
        :return:
        """
        draw = ImageDraw.Draw(self.result_image)
        start_x, start_y = self.scale_to_img(start_point, (self.result_image.size[0], self.result_image.size[1]))
        end_x, end_y = self.scale_to_img(end_point, (self.result_image.size[0], self.result_image.size[1]))
        draw.line((start_x, start_y, end_x, end_y), fill=color, width=width)


vis = GPSVis(data_path='data.csv',
             map_path='map.png',
             points=(-48.0357, -26.0645, -46.6806, -22.8557))
vis.create_image(color=(0, 0, 255), width=3)
vis.draw_points([(-47.0608, -23.9369), (-46.3250, -23.5500)])  # Example points to draw
vis.draw_line((-47.0608, -23.9369), (-46.3250, -23.5500))  # Example line to draw
vis.plot_map(output='save')


def plot_path():
    start_lat = float(entry_start_lat.get())
    start_lon = float(entry_start_lon.get())
    end_lat = float(entry_end_lat.get())
    end_lon = float(entry_end_lon.get())
    
    vis = GPSVis(data_path='data.csv', map_path='map.png', points=(-48.0357, -26.0645, -46.6806, -22.8557))
    vis.create_image(color=(0, 0, 255), width=3)
    vis.draw_points([(start_lat, start_lon), (end_lat, end_lon)])
    vis.draw_line((start_lat, start_lon), (end_lat, end_lon))
    vis.plot_map(output='show')

# Criar a janela principal
root = tk.Tk()
root.title("Traçar Caminho no Mapa")

# Criar os widgets para entrada de coordenadas
tk.Label(root, text="Latitude de Início:").grid(row=0, column=0)
entry_start_lat = tk.Entry(root)
entry_start_lat.grid(row=0, column=1)

tk.Label(root, text="Longitude de Início:").grid(row=1, column=0)
entry_start_lon = tk.Entry(root)
entry_start_lon.grid(row=1, column=1)

tk.Label(root, text="Latitude de Fim:").grid(row=2, column=0)
entry_end_lat = tk.Entry(root)
entry_end_lat.grid(row=2, column=1)

tk.Label(root, text="Longitude de Fim:").grid(row=3, column=0)
entry_end_lon = tk.Entry(root)
entry_end_lon.grid(row=3, column=1)

# Botão para traçar o caminho
btn_plot = tk.Button(root, text="Traçar Caminho", command=plot_path)
btn_plot.grid(row=4, columnspan=2)

root.mainloop()