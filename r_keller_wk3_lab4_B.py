
#opens file
infile = open('/Users/rkeller13/Python Files/lab4Btext.txt')

#reads lines and places them in lists
lineList = infile.readlines()
line1 = lineList[0]
line2 = lineList[1]
line3 = lineList[2]

#removes \n from end of line, may not be necessary
line1 = line1.strip("\n")
line2 = line2.strip("\n")
line3 = line3.strip("\n")

#separates each word in each line to their own lists
line1Sep = line1.split(" ")
line2Sep = line2.split(" ")
line3Sep = line3.split(" ")

#calculates salary increase
ln1SalInc = float(line1Sep[2]) * float(line1Sep[3]) / 100
ln2SalInc = float(line2Sep[2]) * float(line2Sep[3]) / 100
ln3SalInc = float(line3Sep[2]) * float(line3Sep[3]) / 100

#adds increase to original salary
ln1UpdSal = ln1SalInc + float(line1Sep[2])
ln2UpdSal = ln2SalInc + float(line2Sep[2])
ln3UpdSal = ln3SalInc + float(line3Sep[2])
                              

#opens file to write output
outfile = open('/Users/rkeller13/Python Files/lab4Boutput.txt', 'w')

#formats and writes output, separated for ease of reading code
#I'm inferring that the first and last names should be
#15 total characters regardless, which means if they are less, there will be spaces
outfile.write("{:15} {:15} {:.2f} {:.2f} {:.2f} \n".format(line1Sep[1], line1Sep[0], float(line1Sep[2]), ln1UpdSal, ln1SalInc))
outfile.write("{:15} {:15} {:.2f} {:.2f} {:.2f} \n".format(line2Sep[1], line2Sep[0], float(line2Sep[2]), ln2UpdSal, ln2SalInc))
outfile.write("{:15} {:15} {:.2f} {:.2f} {:.2f} \n".format(line3Sep[1], line3Sep[0], float(line3Sep[2]), ln3UpdSal, ln3SalInc))
outfile.close()


#check work
outfile2 = open('/Users/rkeller13/Python Files/lab4Boutput.txt')
lineList2 = outfile2.readlines()

