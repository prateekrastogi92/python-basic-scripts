import os
import sys

import re

text_to_rep = "unix"

with open("replace_word_input.txt", "r+") as file_to_open:
   new_file = file_to_open.read().replace(text_to_rep, "Linux")
with open("replace_word_input.txt", "w") as file_to_open:
  file_to_open.write(new_file) 
