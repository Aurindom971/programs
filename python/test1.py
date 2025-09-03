import pickle as p 

# Open the file
f = open("cus_booking_detail.dat", "rb")
cnt=0
try:
    while True:
        pb=p.load(f)
        cnt+=1
except EOFError:
    print("Total no people travelled till now: ",cnt)