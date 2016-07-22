import csv
import numpy
import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime
from file_info import file_info
import pandas as pd



class File:
	def __init__(self, name, columns, quantity, unit = None, converter = None):
		self.name = name
		self.columns = [quantity + " " + col for col in columns]
		self.quantity = quantity
		self.unit = unit
		self.converter = converter
		self.start, self.end = self._find_period()

	def __str__(self):
		return self.quantity
	
	def _find_period(self):
		self.dataframe = pd.read_csv(self.name, 
									 sep = ";",
									 names = ["status"] + self.columns,
									 index_col = 0,
									 header = None)
		
		self.dataframe.index = pd.to_datetime(self.dataframe.index, unit='s')
		start = self.dataframe.index[0]
		end = self.dataframe.index[-1]
		return start, end

	def _get_columns(self, start, end, columns):
		df = self.dataframe.loc[:, columns]
		return df[numpy.logical_and(start < df.index, df.index < end)]



def get_files():
	return [File(**kwargs) for kwargs in file_info]

def plot_files(start, end, files, columns_list):
	ax = None
	for file, columns in zip(files, columns_list):
		df = file._get_columns(start, end, columns) 
		ax = df.plot(ax = ax)
	plt.show()

