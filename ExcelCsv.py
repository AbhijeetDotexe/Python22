import csv
data=open('example.csv',encoding='utf-8')
csv_data=csv.reader(data)
data_lines=list(csv_data)
#print(data_lines)
# for i in data_lines[1:]:
#     print(i[3])# TO print all the email address

# TO display the full name
# for i in data_lines[1:]:
#     print(i[1]+" "+i[2])
file_to_read=open("to_save_file.csv",mode='w',newline='')
csv_writer=csv.writer(file_to_read,delimiter=' ')
csv_writer.writerow(['a','b','c'])
csv_writer.writerows([[1,2,3],['4','5','6']])
file_to_read.close()
f= open('to_save_file.csv',mode='a',newline='')
csv_writer=csv.writer(f)
csv_writer.writerow(['7','8','9'])
f.close()