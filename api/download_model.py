from transformers import pipeline
import os

# downloading the GPT-Neo model on docker build
nlp = pipeline("text-generation", model=os.environ['GPT_MODEL'])