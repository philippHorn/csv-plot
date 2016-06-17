import csv
import matplotlib.pyplot as plt
from datetime import datetime

class File:
	def __init__(self, name, columns, quantity, unit = None, converter = None):
		self.name = name
		self.columns = columns
		self.quantity = quantity
		self.unit = unit
		self.converter = converter
		self.start, self.end = self._find_period()

	def __str__(self):
		return self.quantity
	
	def _find_period(self):
		with open(self.name) as file:
			reader = csv.reader(file, delimiter=';')
			start = int(next(reader)[0])
			end = int(list(reader)[-1][0])
			start, end = datetime.fromtimestamp(start), datetime.fromtimestamp(end)
			return start, end

	def _plot_columns(self, start, end, columns):
		times = []
		# get the corresponding index for the csv-file, moved by one since the first column is the time
		get_column_index = lambda col: self.columns.index(col) + 1
		indices = [get_column_index(col) for col in columns]

		with open(self.name) as fh:
			times = []
			quantities = [[] for _ in indices]
			reader = csv.reader(fh, delimiter=';')
			for row in reader:
				time = datetime.fromtimestamp(int(row[0]))
				if not (start <= time <= end): 
					continue

				times.append(time)
				for index, lst in zip(indices, quantities):
					if self.converter:
						lst.append(self.converter(int(row[index])))
					else:
						lst.append(int(row[index]))
			for quantity in quantities:
				plt.plot(times, quantity)

def get_files():
	return [File("csv/48.10391.0.0.12000-3.csv", ["Code", "Status"], "Zustand"),
			File("csv/48.10391.0.0.12008-4.csv", ["min", "mittel", "max"], "Leistung soll", unit = "%", converter = lambda x: x/10.0),
			File("csv/48.10391.0.0.12165-4.csv", ["min", "mittel", "max"], "Abgasgebläse", unit = "U/min"),
			File("csv/48.10391.0.11094.0-4.csv", ["min", "mittel", "max"], "Primärluft", unit = "%", converter = lambda x: x/10.0),
			File("csv/48.10391.0.11095.0-4.csv", ["min", "mittel", "max"], "Sekundärluft", unit = "%", converter = lambda x: x/10.0),
			File("csv/48.10391.0.11094.0-4.csv", ["min", "mittel", "max"], "Restsauerstoff", unit = "%", converter = lambda x: x/100.0),
			File("csv/48.10391.0.11109.0-4.csv", ["min", "mittel", "max"], "Kessel T.", unit = "°C", converter = lambda x: x/10.0),
			File("csv/48.10391.0.11110.0-4.csv", ["min", "mittel", "max"], "Abgas T.", unit = "°C", converter = lambda x: x/10.0),
			File("csv/48.10391.0.11160.0-4.csv", ["min", "mittel", "max"], "Rücklauf T.", unit = "°C", converter = lambda x: x/10.0),
			File("csv/120.10251.0.11153.0-4.csv", ["min", "mittel", "max"], "Puffer Oben", unit = "°C", converter = lambda x: x/10.0),
			File("csv/120.10251.0.11155.0-4.csv", ["min", "mittel", "max"], "Puffer Unten", unit = "°C", converter = lambda x: x/10.0)
		]
def plot_files(start, end, files, columns_list):
	get_column_index = lambda file, col: file.columns.index(col) + 1
	for file, columns in zip(files, columns_list):
		file._plot_columns(start, end, columns)
	plt.show()

