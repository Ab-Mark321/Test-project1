sales=[200,45,567,243,450,"abc",700,"price"]

with open ("sales.txt", "w") as sales_file:
    for sale in sales:
        sales_file.write(str(sale)+"\n")

with open ("sales.txt", "r") as sales_file:
    lines=sales_file.readlines()

reports=[]
for line in lines:
    try:
        reports.append(int(line))
    except ValueError:
        continue
total=0
for report in reports:
    total+=report  

print(f"your total sale of this month is {total}.\n")