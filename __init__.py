#import shutil
import folder_paths
import os, sys, subprocess

try:
  print("### Loading: Save img extra data")
  from .Save_img_extra_data import NODE_CLASS_MAPPINGS
except:
  img_path = os.path.dirname(__file__)
  from .Save_img_extra_data import NODE_CLASS_MAPPINGS

comfy_path = os.path.dirname(folder_paths.__file__)

__all__ = ['NODE_CLASS_MAPPINGS']
