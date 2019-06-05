import os
import sys

import re

text_to_rep = input("Enter text to replace")
text_after = input("Enter the text to replace with")
nfile=input("Enter the file name")
with open(nfile, "r+") as file_to_open:
   new_file = file_to_open.read().replace(text_to_rep,text_after)
with open(nfile, "w") as file_to_open:
  file_to_open.write(new_file) 
