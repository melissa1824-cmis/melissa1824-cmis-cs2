myName = "Melissa" #variable containing my name.
myAge = 16 + float(11)/12 #variable containing my age in years as a decimal.
myHeight = 1.61 #variable containing my height in meters.
sqLength = 2 #variable containing the length of one side of a square.
rectLength = 6 #variable containing the length of a rectangle.
rectHeight = 4 #variable containing the height of the same rectangle. 
ageMonths = myAge * 12 #variable containing my age in months.
yearsToLive = 74 - myAge #variable containing the number of years I have left to live.
convertCmToFt = myHeight * 0.0328084 #variable containing the conversion of meters to foot.
heightFeet = convertCmToFt * 100 #variable containing my height in feet.
AverageHeight = 1 + float(59)/100 #variable containing the average height of someone of my sex and age in my homecountry, in meters.
differenceAverageHeight = myHeight - AverageHeight #variable containing the difference in my height from the average height in meters, of someone my age and sex in my home country.
areaSquare  = sqLength * sqLength #variable containing the area of a square with the side created before.
volCube = sqLength * sqLength * sqLength #variable containing the volume of a cub with the side length created before. 
halfVol = volCube/2.0 #variable containing half the volume of a cube with the side created before.
areaRect = rectLength * rectHeight #variable containing the area of the rectangle with the height and side lengths created before.
ninthRect = areaRect * 1/9.0 #variable containing one-ninth of the area of the the rectangle with the height and side lengths created before. 
print "I am " +str(myAge)+ " years old at the moment. I am " +str(ageMonths)+ " months old. I have around " +str(yearsToLive)+ " years to live according to the average lifespan. I am " +str(heightFeet)+ " feet in standard measure."
print "Hi. My name is" ,myName, ". I am" ,myHeight, "meters tall. In American measurements, my height is ",heightFeet, "feet. I am" ,myAge, "years old, so according to the average life span, I have" ,yearsToLive, "more years to live."
winkyFace = ";)" #winkyface
print winkyFace * 10000


