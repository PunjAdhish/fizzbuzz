fread=open('Book1.txt','r')
fread=open('Book2.txt','r')
fread=open('Book3.txt','r')
fread=open('/home/student/desktop/Desktop/fizzbuzz-adhishpunjb00747348/fizzbuzz' ,'r')
fw1=open('bookXuniqu.list','a+')
fw2=open('raarewords.list','a+')
for i  in fr1.readlines():
        dict_check1.append(i.split(" "))
for i in fr2.readlines():
        dict_check2.append(i.split(" "))
for i in fr3.readlines():
        dict_check3.append(i.split(" "))
for i in dict_check1:
		if i in frc.word():
		else:
			fw1.write(i)
for i in dict_check2:
                if i in frc.word():
                else:
                        fw2.write(i)
for i in dict_check3:
                if i in frc.word():
                else:
                        fw3.write(i)

