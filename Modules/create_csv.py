import csv
import os
import re

output_file = open("k:/Andrew/vkr/example/1600.csv", 'w')
csv_out = csv.writer(output_file)
path_f = 'k:/Andrew/vkr/example/f1001/'
path_err = 'k:/Andrew/vkr/example/err2_1600_csv.txt'
f_err = open(path_err, 'w', encoding='utf-8')
list_f = os.listdir(path_f)
for el in list_f:
    try:
        f = open(path_f + el, 'r', encoding='utf-8')
        struct = []
        str00 = f.readline()
        str0 = str(re.match(r'\d\d', str00).group(0))
        struct.append(str0.replace('\n','').strip())
        str1 = f.readline()
        struct.append(str1.replace('\n','').strip())

        str2 = f.read().replace('\n', ' ')
        str2 = str2.lower()
        res = re.findall(r"\b([а-яё]+)", str2)
        str2 = ' '.join(res)
        struct.append(str2.strip())
        csv_out.writerow(struct)
        f.close()
    except:
        f_err.write(str(el) + '\n')
        f.close()
        pass
output_file.close()



# output_file = open("probe.csv", 'r')
# csv_out = csv.reader(output_file, delimiter=',')
# for row in csv_out:
#     if(row != []):
#         print(row[0])
# output_file.close()