std = input("Enter the name of student : ")
def stdReport():
    cd = float(input("Enter marks which gain in PPS : "))
    ajp = float(input("Enter marks which gain in AJP : "))
    mpi = float(input("Enter marks which gain in MPI : "))
    se = float(input("Enter marks which gain in SE : "))
    toc = float(input("Enter marks which gain in TOC : "))
    return ((cd+ajp+mpi+se+toc)/5)
print(std,",this is your marks = :", stdReport(),"%")
