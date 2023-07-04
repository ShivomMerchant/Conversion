###########################################################
    #  Computer Project #1
    #
    #  Gather user input
    #    Print input statement
    #    Calculate meters
    #       Round to 3 decimal
    #   Repeat for feet,miles,furlongs, and time
    #   Print conversions
    ###########################################################

#asking user for number of rods
#convert string to integer
numrods_str = input("Input rods: \n")
numrods_float = float(numrods_str)
print("You input",numrods_float,"rods.\n")

#multipy number of rods by meter conversion
#rounding number to 3 decimal points
print("Conversions")
m_float = float(numrods_float*5.0292)
meters = float(round( m_float, 3 ))
print("Meters:", meters)

#divide meters by feet conversion 
f_float = float(m_float*(1/0.3048))
feet= float(round(f_float, 3))
print("Feet:", feet)

#divide meters by miles conversion
mil_float = float(m_float*(1/1609.34))
miles = float(round(mil_float, 3))
print("Miles:", miles)

#divide number of rods by furlong conversion 
fur_float = float(numrods_float*(1/40))
furlongs = float(round(fur_float, 3))
print("Furlongs:", furlongs)

#convert 3.1 miles/hour to miles/minute
#divide by miles/minute conversion
min_float = float(mil_float*(1/(3.1/60)))
minutes = float(round(min_float, 3))
print("Minutes to walk", numrods_float ,"rods:", minutes)
