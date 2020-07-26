import fastai
from fastai import *
from fastai.text import *

DATA_CLASSES = ["predatory", "safe", "spam"]
learn = load_learner("exports/models/safety")

def predict(text):
  return DATA_CLASSES[learn.predict(text)[1]]