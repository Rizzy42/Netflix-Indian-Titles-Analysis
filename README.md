# Netflix Indian Titles Analysis
&nbsp;&nbsp;&nbsp;*An exploration of how the percentage of Indian titles on 
Netflix has changed, between 2000 and 2022.* (PS: This is my first dataset analysis!)
## Getting Started
This project has been written to be as self-contained as possible, but to have the smoothest experience you'll need [Anaconda](anaconda.com) or [Miniconda](docs.conda.io/en/latest/miniconda.html). If this is not possible, this project's dependencies have been tested to work on [Python 3.10](https://www.python.org/downloads/release/python-3104/).
### Setting up the Environment
If you're using Anaconda/Miniconda, run the following in a shell:
```
$ conda env create -f pkgs/environment.yml
```
If you're using Python and Pip:
```
$ pip install -r requirements.txt
```

### Obtaining the Dataset
```utils.data``` provides the ```download_data``` function for obtaining the latest copy of the [Netflix Titles Dataset on Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows) using the [opendatasets](https://pypi.org/project/opendatasets/) library. This method requires a Kaggle API Key to work.  
1. First, sign in to [Kaggle](kaggle.com)
2. Click on your profile picture on the top right and select "Account"
3. Scroll down to the "API" section and click "Generate New API Token"
4. Download "kaggle.json" into the root of this repo

If the above method is not desired, this repo includes a copy of the dataset in ```data/``` that is accurate as of August 2022. Skipping the ```download_data``` cell in the notebook will use the local copy.