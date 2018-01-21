import pandas as pd

import csv

from collections import Counter

def create_ids():
    idsA = open("Files for Danielle/Human_GeCKOv2_Library_A_09Mar2015.csv")
    idsB = open("Files for Danielle/Human_GeCKOv2_Library_B_09Mar2015.csv")
    reader = csv.reader(idsA)
    sequence = {}
    for row in reader:
        sequence[row[2]]= row[1]
    reader = csv.reader(idsB)
    for row in reader:
        sequence[row[2]]= row[1]
    idsA_df = pd.read_csv("Files for Danielle/Human_GeCKOv2_Library_A_09Mar2015.csv")
    idsB_df = pd.read_csv("Files for Danielle/Human_GeCKOv2_Library_B_09Mar2015.csv")
    frames=[idsA_df,idsB_df]
    sequence_df = pd.concat(frames, ignore_index=True)
    sequence_df.drop("Unnamed: 3",axis=1,inplace=True)
    return sequence, sequence_df

def find_start_index(data,start,length,tries,id_dict):
    good = []
    start_index = 0
    num_hits = 0
    for j in range(tries):
        for i in range(0,len(data)):
            if data[i][start+j:start+length+j] in id_dict:
                good.append(id_dict[data[i][start+j:start+length+j]])
        if len(good) > num_hits:
            num_hits = len(good)
            start_index = start+j
        good=[]
    return start_index

def get_hits(data,start_index,length,id_dict):
    hit_list = []
    for i in range(0,len(data)):
            if data[i][start_index:start_index+length] in id_dict:
                hit_list.append(id_dict[data[i][start_index:start_index+length]])
    return hit_list
    
def create_df(hit_list,id_df):
    hits_temp = Counter(hit_list)
    hit_df = pd.DataFrame.from_dict(hits_temp, orient='index').reset_index()
    hit_df.rename(index=str, columns={"index":"UID",0:"hits"}, inplace=True)
    hit_df["gene_id"]=""
    for index, row in hit_df.iterrows():
        row["gene_id"]=id_df.loc[id_df["UID"]==row["UID"]]["gene_id"].get_values()[0]
    hit_df["gene_id"] = hit_df.apply(lambda row: id_df.loc[id_df["UID"]==row["UID"]]["gene_id"].get_values()[0], axis=1)
    return hit_df
    
ids_dict, ids_df = create_ids()"

content = open("File.fastq").readlines()[1::4]

si = find_start_index(content,25,20,20,ids_dict)

hits = get_hits(content,si,20,ids_dict)

df = create_df(hits,ids_df)

df.to_csv(path_or_buf="File.csv")
