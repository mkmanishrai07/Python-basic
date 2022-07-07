
def GST_cal(op, np):

	return (((np - op) * 100) / op)
op = float(input("Enter op : "))
np = float(input("Enter np "))


print("GST = ",end='')

print(round(GST_cal(op, np)),end='')

print("%")


