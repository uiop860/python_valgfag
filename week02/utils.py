import os
import argparse
import json

def get_file_names(folderpath,out= "output.txt"):
  """ takes a path to a folder and writes all filenames in the folder to a specified output file"""
  files = os.listdir(folderpath)
  with open(out,'w') as outfile:
    for f in files:
      outfile.write(f + "\n")

def get_all_file_names(folderpath,out= "output.txt"):
  """takes a path to a folder and write all filenames recursively (files of all sub folders to)"""
  file_names = {}
  
  def recursion(path,):
    nonlocal file_names
    files = os.listdir(path)
    file_names[path] = []
    for file in files:
      if len(file.split('.')) == 1:
        recursion(path+"/"+file)
      else:
        file_names[path].append(file)
  recursion(folderpath)
  with open(out, 'w') as outfile:
    outfile.write(json.dumps(file_names, sort_keys=True, indent=4))
  ## python utils.py get_all_file_names -p ../../my_notebooks
          
def print_line_one(file_names):
  """takes a list of filenames and print the first line of each"""
  files = file_names.split(',')
  for file in files:
    with open(file, 'r') as input_file:
      print(next(input_file))
  

def print_emails(file_names):
  """takes a list of filenames and print each line that contains an email (just look for @)"""

def write_headlines(md_files, out="output.txt"):
  """takes a list of md files and writes all headlines (lines starting with #) to a file"""
    
if __name__ == '__main__':
  parser = argparse.ArgumentParser(description="")
  parser.add_argument("option",help="What option to choose")
  parser.add_argument("-p","--path",help="Path to get files from", default="./")
  parser.add_argument("-o","--output", help="Path to save output to")
  
  args = parser.parse_args()
  
  if args.option == "get_file_names":
    get_file_names(args.path)
  elif args.option == "get_all_file_names":
    get_all_file_names(args.path)
  elif args.option == "print_line_one":
    print_line_one(args.path)