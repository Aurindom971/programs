import pickle as p 


def staff_signup():
    f=open("staff.dat","ab")
    while True:
        info=[]
        emp_id=input("Employee ID: ")
        nm=input("Enter Name: ")
        gen=input("Enter Gender: ")
        dob=input("Enter Date of Birth in DD/MM/YYYY Format: ")
        ph=input("Enter Phone No.: ")
        password=input("Enter password: ")
        c_password=input("Confirm your password: ")
        b_no=input("Enter Badge No: ")
        if len(emp_id)==8 and len(b_no)==6 and password==c_password:
            info=[emp_id,nm,gen,dob,password,b_no]
            p.dump(info,f)
            ch=input("Want to add more staff ? Y/N")
            if ch.upper()=="N":
                break
        else:
            print("Invalid details")
    f.close()
staff_signup()