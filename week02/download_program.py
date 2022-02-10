import argparse
from my_notebooks.modules import webget

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A program that downloads a URL and stores it locally')
    parser.add_argument('url', help='The URL to process')
    parser.add_argument('-d','--destination', help='The destination for the download')

    args = parser.parse_args()
    if args.destination:
      test = webget.download(args.url,args.destination)
    else:
      filename = args.url.split('/')
      extension = filename[len(filename)-1].split('.')
      filename = extension[0]
      extension = extension[len(extension)-1]
      test = webget.download(args.url,"my_notebooks/week02/" + filename + "." + extension)
    # print(args.url.split('/'))
    
    # python -m my_notebooks.week02.download_program https://hackernews.com -d my_notebooks/week02/default_file.dat
    
    # print(test)
  
    
    
    