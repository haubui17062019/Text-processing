import csv

with open("./nemo_text_processing/text_normalization/vi/data/address/address_word.tsv", encoding="utf-8") as label_tsv:
    labels = list(csv.reader(label_tsv, delimiter="\t"))

for x, y in labels:
    pass
print(labels[0])    
