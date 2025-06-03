from transformers import pipeline
from PIL import Image

classifier = pipeline("image-classification", model="./plantvillage-model")


image = Image.open("leaf.jpg")
results = classifier(image)

for r in results:
    print(f"{r['label']} - confidence: {r['score']*100:.2f}%")
