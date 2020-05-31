# Welcome to the Song Recommender

In this repository sat a project that exploited the Million Song Dataset to build a Song Recommendation Engine. Other than other recommendation systems that either used content based or collaborative filtering techinques, this Recommender focuses on the intrinsic features embedded in the beats, rhythms, and vocals of a song. Such features can be extracted using the mel frequency cepstral coefficients (MFCCs).

The repository contains the following files:

* [hdf5_gathers.py](hdf5_gathers.py)
* [hdf5_json_all.py](hdf5_json_all.py)
* [EDA.ipynb](EDA.ipynb)
* [Recommender.ipynb](Recommender.ipynb)
* [Results GUI.ipynb](Results%20GUI.ipynb)
* [Million Song Slides](Million%20Song%20slides.pdf)

### The *[Gather](hdf5_gathers.py)* & *[Json](hdf5_json_all.py)* .py Files

These 2 .py files requires a ```python 2.7``` environment. The database is stored on AWS as a ```HDF5``` format. After the data is mounted to my Google Cloud bucket, it has to be transformed into a different format. While the ```hdf5_gathers.py```  is used to extract the features, the ```hdf5_json_all.py``` tranfroms the features into ```JSON``` format. To run these scripts, just simply type the command in your terminal:

```linux
python hdf5_json_all.py
```

### The *[EDA](EDA.ipynb)* Notebook

In this notebook, we created some visualizations for the dataset. The size of this notebook is large as it shows the plots. Please download and and open it on your local laptop.

### The *[Recommender](Recommender.ipynb)* & the *[Result GUI](Results%20GUI.ipynb)* NoteBook

The Recommender notebook contains the main part of our project, data modeling. We used ```pySpark``` to handle the big data. The Result GUI shows a GUI demo of the recommender using a sample of the results.

### The [Slides](Million%20Song%20slides.pdf) PDF

This is the presentation slides we used for our project presentation.
