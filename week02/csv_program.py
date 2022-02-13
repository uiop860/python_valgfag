import argparse
import csv

def print_file_content(file):
  with open(file) as file:
    content = file.read()
    print(content)

def write_list_to_file(output_file, list):
  with open(output_file,'w') as output_file:
    for id, row in enumerate(list):
      if id != 0:
        output_file.write('\n')
      for id, item in enumerate(row):
        if id != len(item):
          output_file.write(item.strip() + ',')
        else:
          output_file.write(item)
  
def read_csv(input_file):
  csv_list = []
  with open(input_file, 'r') as input_file:
    reader = csv.reader(input_file, delimiter=';')
    # header_row = next(reader)
    for row in reader:
      csv_list.append(row)
  return csv_list
      
    

if __name__ == '__main__':
  
  # read_csv("data.csv")
  # write_list_to_file('test.txt',['test','abe','abe','abe','abe','abe'])
  
  parser = argparse.ArgumentParser(description='')
  parser.add_argument('file',help='The csv file to read')
  parser.add_argument('-o','--output', help='The output file to write')
  args = parser.parse_args()
  
  if args.output:
    csv_list = read_csv(args.file)
    write_list_to_file(args.output, csv_list)
  else:
    print_file_content(args.file)
