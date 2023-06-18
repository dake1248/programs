import csv

csv_w=open("3.csv",'w',newline='')
wc=csv.writer(csv_w)
wc.writerow(['date','follow','unfollow'])

import random

for i in range(100):
	wc.writerow([str(random.gauss(20,2))]+[str(random.gauss(20,2))]+[str(random.gauss(20,2))])

csv_w.close()