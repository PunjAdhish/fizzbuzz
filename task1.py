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
	word="" #declaring word as empty  string
	fw=open("NewFile.txt",'w')
	count=0  #set counter
	pages=input("Enter starting page number")
	pagend=input("Enter Ending page number")
	for word in range(0,(25*pages),+1):
	count+=1
	if count>=(25*pages) and count<=(25*pagend):
		for j in i:
			if j=='o' or j=='O':
				J='0'
			elif j=='e' or j=='E'
				j='3'
			elif j=='i' or j=='I'
				j='1'





