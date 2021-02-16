def main(): 
    # Input the filename repetedly until a correct file name and extension is entered
    # FileNotFoundError exception is handled and user is invoked to input correct filename
    one=list()
    two=list()
    three=list()
    diff=list()
    final=list()
    missdest=list()
    repeat='y'
    while (repeat=='y' or repeat=='Y'):
        try:
            file_name=input('Enter first filename: ')
            f=open(file_name, 'r')
            repeat='n'
        except FileNotFoundError:
            print('Enter a valid file name and extension')

    for i in f:
        lines=f.readlines()
        count=len(lines)
        for index in range(0,count):
            line = lines[index]
            file_list=line.split(',')
            one.extend(file_list)
    f.close()
    repeat='y'
    while (repeat=='y' or repeat=='Y'):
        try:
            file_name=input('Enter second filename: ')
            f=open(file_name, 'r')
            repeat='n'
        except FileNotFoundError:
            print('Enter a valid file name and extension')

    for i in f:
        lines=f.readlines()
        count=len(lines)
        for index in range(0,count):
            line = lines[index]
            file_list=line.split(',')
            two.extend(file_list)
    f.close()
    repeat='y'
    while (repeat=='y' or repeat=='Y'):
        try:
            file_name=input('Enter third filename: ')
            f=open(file_name, 'r')
            repeat='n'
        except FileNotFoundError:
            print('Enter a valid file name and extension')

    for i in f:
        lines=f.readlines()
        count=len(lines)
        for index in range(0,count):
            line = lines[index]
            file_list=line.split(',')
            three.extend(file_list)
    f.close()

    for i in range (0, len(one)):
        one[i]=one[i].strip()
        
    for i in range (0, len(two)):
        two[i]=two[i].strip()
        
    for i in range (0, len(three)):
        three[i]=three[i].strip()
    
    for i in range (0, len(one)):
        if one[i] not in two:
            diff.append(one[i])
            
    for i in range (0, len(diff)):
        if diff[i] not in three:
            final.append(diff[i])
            
    f=open("Result1.txt",'w')
    
    for i in range (0, len(final)):
        f.write(final[i])
        f.write("\n")
        
    f.close()

    for i in range (0, len(one)):
        if one[i] not in three:
            missdest.append(one[i])

    f=open("Result2.txt", "w")

    for i in range (0, len(missdest)):
        f.write(missdest[i])
        f.write("\n")
    f.close()

    print(len(one))
    print("")
    print(len(three))
main()
        
