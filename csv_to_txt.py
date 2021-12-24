import csv

csv_file = "G:\\Ayame\\EasyOcrTraining\\trainer\\all_data\\train\\content\\train\\labels.csv"
txt_file = "G:\\Ayame\\PaddleOCR\\train_data\\card_3_7k\\labels_train.txt"

my_output_file = open(txt_file, "w", encoding="utf8")
my_input_file = open(csv_file, "r", encoding="utf8")

for row in csv.reader(my_input_file):
    my_output_file.write("\t".join(row) + '\n')
my_output_file.close()