def splitRoute():									#definition for subroutine
 route = []										#creates an empty list
 #f=open('http://www.mdl.nws.noaa.gov/~naefs_ekdmos/text/naefs_tempcdf_00.txt/','r')	#grab the txt file and opens it
 #f=open('http://www.ems.psu.edu/~young/meteo473/Data/EKDMOS00.txt/','r') 
 f=open("/home/meteo/sdg152/Meteo_473/MS3/AllStations.txt","r")
 for line in f.readlines():								#loops through all of the lines in f
  line = line.strip('>')								#gets rid of something on the end
  line = line.replace("\t","")								#gets rid of the escape character t
  line = line.replace("\n","")								#gets rid of the escape character n
  apple = line.split()									#splits each line off
  route.append([apple])									#appends each line to the end of the list apple
 f.close()										#closes the file f
 return route										#returns the whole list appended inside apple
paul = []										#creates an empty list
paul = splitRoute()									#calls the function and puts it into a variable

Temp = paul[1][0]									#puts a single line in a variable
print Temp 										#This prints the full line, from the file in single quotes
apple = float(Temp[2])									#changes string to floating point number
pear = float(Temp[3])
print type(apple)									#prints type as a check
print type(pear)
pineapple = pear+(2*(apple-pear))							#math works, gotta figure another way to add it to the list
Temp[:2] = pineapple									#the math, doesn't work
#print Temp[2]	
#apple[:15] = apple[13]+(2*(apple[14]-apple[13]))
print pineapple
#n = (Temp[14]-Temp[2])/0.10		#number of bins	
#T = Temp[2] 				#Sets T for incrementation
#Ntemp[0] = Temp[2]		 	#Sets new temp for zero value
#CDF[2] = 0     				#sets the CDF
#Tbot = Temp[2]  		  	#sets the lower bound on temp
#Cbot = cdf[0]				#sets the lower bound on cdf
#j = 1					#counter for changing Ttop and Ctop
#Ttop = Temp[j]				#sets the upper bound on temp
#Ctop = cdf[j]				#sets the upper bound on cdf
#k = 0					#counter for differnece, pdf and temp

#for i in range (n):				#we are going to loop through n times, all of the bins

#  	T = T + 0.1						#increment temperature

# 	if T > Ttop:						#if what we are incrementing equals the top of the bin
# 		j = j + 1						#increment my changer
#      		Tbot = Ttop						#change top to bottom for temp
#      		Ttop = Temp[j]					#and create a new top for temp
#      		Cbot = Ctop						#Change top to bottom for cdf
#      		Ctop = cdf[j]						#and create a new top for cdf
#CDF[i]=Cbot +(((T-Tbot)/(Ttop-Tbot))*(Ctop-Cbot))	#this is my interpolation
#Ntemp[i] = T3						#creates the array for incremented temp
#pdf[i] = CDF[i] - CDF[k]					#does the difference for the pdf
#Mid[i] = (Ntemp[i]+Ntemp[k])/2				#calculate middle of the bin
#k = k + 1							#increment the difference counter
#price[i] = 1.36 *(abs(Mid[i]-55)) +20			#price of the middle
