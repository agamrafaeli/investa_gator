#!/usr/bin/python

# Downloads and installs stanford-ner.
# TODO: requires WGET, so currently doesn't run on windows...
import os

os.chdir("full_app")
os.system("wget http://nlp.stanford.edu/software/stanford-ner-2015-12-09.zip")
os.system("unzip stanford-ner-2015-12-09.zip")
os.system("rm stanford-ner-2015-12-09.zip")
os.chdir("..")
