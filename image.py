import pandas as pd
from google_images_download import google_images_download

path = "/home/raja/Documents/Dev/Python/sheet1.csv"
def load_dataset(path):
    return pd.read_csv(path)

def download_images_url(keywords,limit,file_name):
    response = google_images_download.googleimagesdownload()
    arguments = {"keywords":keywords,"limit":limit,"print_urls":True}
    path   = response.download(arguments)
    with open("{}.txt".format(file_name),"W+") as f:
        f.write(str(path))

def download(limit=4):
    df = load_dataset(path)
    while(count<=4):
     for ele in df.iterrows():
        download_images_url(ele.collegeName,4,ele.college_id)
        count+=1
