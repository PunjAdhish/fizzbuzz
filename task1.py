def input_option():
	target_file=input("Book1 Book2 Book3....:")
	check=0
	if target_file=="Book1":
		fread=open("Book1.txt",'r')
	elif target_file=="Book2":
		fread=open("Book2.txt",'r')
	elif target_file=="Book3":
		fread=open("Book3.txt",'r')
		check=1



