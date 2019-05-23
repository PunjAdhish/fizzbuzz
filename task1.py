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
	else:
		target_file=input("Please Enter Valid Book entry")
		check=0
	input_page(fr)
input_option()
def input_page(fr):
	 fw=open("NewFile.txt",'w')
	 count=0  #set counter



