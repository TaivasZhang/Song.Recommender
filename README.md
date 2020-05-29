# Welcome to the Song Recommender

In this repository sat a project that exploited the Million Song Dataset to build a Song Recommendation Engine. Other than other recommendation systems that either used content based or collaborative filtering techinques, this Recommender focuses on the intrinsic features embedded in the beats, rhythms, and vocals of a song. Such features can be extracted using the mel frequency cepstral coefficients (MFCCs).

The repository contains the following files:

* hdf5_gathers.py
* hdf5_json_all.py
* EDA.jpynb
* Recommender.jpynb
* Results GUI.jpynb
* Million Song slides.pdf

## The *Gather* & *Json* ```.py``` Files

These 2 .py files requires a ```python 2.7``` environment. The database is stored on AWS as a ```HDF5``` format. After the data is mounted to my Google Cloud bucket, it has to be transformed into a different format. While the ```hdf5_gathers.py``` is used to extract the features, the ```hdf5_json_all.py``` tranfroms the features into ```JSON``` format. To run these scripts, just simply type the command in your terminal:

```linux
python hdf5_json_all.py
```
