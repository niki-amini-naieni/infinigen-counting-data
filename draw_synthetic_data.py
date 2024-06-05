import glob
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import json
import cv2

new_data_files = glob.glob("*.json")

for f_name in new_data_files:
  with open(f_name) as f:
    metadata = json.load(f)
  im = Image.open(metadata["filename"]).resize((metadata["width"], metadata["height"]))
  plt.imshow(im)
  for box in metadata["detection"]["instances"]:
    plt.scatter((box[0] + box[2])/2, (box[1] + box[3])/2, c='r', s=1)
    plt.gca().add_patch(
              Rectangle(
                  (box[0], box[1]),
                  box[2] - box[0],
                  box[3] - box[1],
                  edgecolor="red",
                  facecolor="none"
              )
          )
    
  for box in metadata["exemplars"]:
    plt.scatter((box[0] + box[2])/2, (box[1] + box[3])/2, c='g', s=1)
    plt.gca().add_patch(
              Rectangle(
                  (box[0], box[1]),
                  box[2] - box[0],
                  box[3] - box[1],
                  edgecolor="green",
                  facecolor="none"
              )
          )
    
  
  plt.savefig(f_name[:-4] + "png")
  plt.close()
