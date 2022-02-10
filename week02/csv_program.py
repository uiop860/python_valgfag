import argparse
import csv

def print_file_content(file):
  with open(file) as file:
    content = file.read()
    print(content)

def write_list_to_file(output_file, list):
  with open(output_file,'w') as output_file:
    for id, item in enumerate(list):
      if id == len(list):
        output_file.write(item)
      else:
        output_file.write(item + '\n')
  
def read_csv(input_file):
  csv_list = []
  with open(input_file, 'r') as input_file:
    reader = csv.reader(input_file, delimiter=';')
    # header_row = next(reader)
    for row in reader:
      csv_list.append(row)
  print(csv_list)
      
    

if __name__ == '__main__':
  
  read_csv("data.csv")
  # write_list_to_file('test.txt',['test','abe','abe','abe','abe','abe'])
  
  # parser = argparse.ArgumentParser(description='')
  # parser.add_argument('file',help='The csv file to read')
  
  # args = parser.parse_args()
  
  # print_file_content(args.file)
