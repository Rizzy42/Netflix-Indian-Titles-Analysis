import opendatasets as od
from shutil import move, rmtree
from pandas import read_csv

def download_dataset():
	try:
		rmtree("data")
	except FileNotFoundError:
		print("Data not found, creating new data directory\n")

	od.download("https://www.kaggle.com/shivamb/netflix-shows/notebooks", force=True)
	move("netflix-shows", "data")
	
if __name__ == "__main__":
	download_dataset()