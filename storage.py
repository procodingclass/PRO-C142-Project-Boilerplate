import csv

all_articles = []

file_pointer = open('articles.csv' , encoding='utf-8')
file_reader = csv.reader(file_pointer)
column_header = next(file_reader)
for article in file_reader:
    all_articles.append(article)
file_pointer.close()

liked_articles = []
not_liked_articles = []