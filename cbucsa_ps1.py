"""
Name: Christopher Bucsa
"""
import math
"""
Problem 1
"""
print("\n",40*"-","\n","Problem 1:\n",40*"-")

# 1a
a = (4) + (5/4)  # New binding
print(f"(a): {a:.4f}")

# 1b
b = 19 * (48 ** -4.0) # New binding
print(f"(b): {b:.4f}")

# 1c
pi = math.pi # New binding 
c = (math.cos(pi)**2)  + (math.sin(pi)**2) # New binding
print(f"(c): {c:.4f}")

# 1d
e = math.e # New binding
d = ((1) / math.sqrt(2 * pi)) * (e**1.5) # New binding 
print(f"(d): {d:.4f}")

# 1e
e = -(4 + 5**3 - 0.39) / (2**4 * 17.26) # New binding 
print(f"(e): {e:.4f}")

"""
Problem 2
"""
print("\n",40*"-","\n","Problem 2:\n",40*"-")

print("""
a) "data4analysis" is a legal variable name in python. However, a bit lengthy, maybe shorten to "data".
b) "7mac11" illegal, can't start with digit. Remove leading "7", or replace 7 with word "seven" and add underscores..."seven_mac_11".
c) "iHeartData!" llegal, can't have special characters.  Simply remove the "!". 
d) "j" legal name, however, usually used as looping variable so not a great name unless you're using it for loops. Otherwise, needs to be more descriptive, too generic. 
e) "data-set" illegal name because it contains special character "-".  Replace hyphen with "_" or condense to "data".
f) "data set" illegal because it uses a space.  Add an underscore in between to form "data_set". 
g) "len" is a legal variable name, but not a good one because there is a "len()" function in python.  
h) "thisOldVariable" is a legal variable name.  I think it's a bit lengthy.  Might be better to change it to "oldVariable" or simply "old".
i) "variablesRgr8" is legal but not descriptive enough.  Others reading your code might have a difficult time interpreting it.
j) "this_is_a_variable_i_will_use_for_analysis_results" is legal but way too lengthy.  Needs to be condensed because having to type that everytime is too time consuming. "analysis_results" would be better.. 
      """)


"""
Problem 3
"""
print("\n",40*"-","\n","Problem 3:\n",40*"-")
s = "Computers are good at following instructions, but not at reading your mind." # Create string and assign to variable(identifier)

# 3a
print("(a): Our String, s, contains ",len(s), " elements.") # Using len() function to count the number of elements in the string 

# 3b
print("(b): In our string, the letter 'o' appears ", s.count("o"), " times.") # Using count method to count number of occurences for letter 'o'

# 3c
print("(c): The first occurence of the letter 'g' in our string is at index ", g_index := s.find("g")) # Can use walrus operator to quickly create a variable quickly.  Also, find() method used to find index of first occurence of 'g'.

# 3d
print("(d):", s[g_index : 18]) # Slicing, since g_index returns an int it's basically the number 14.  So we're saying to print from index 14 - 17 (since index used at end is not included)

# 3e
s = s.replace("C","c") # Since strings are immutable, we must update the variable "s" in order to change the C to lowercase c
print("(e):", s)
"""
Problem 4
"""
print("\n",40*"-","\n","Problem 4:\n",40*"-")

x = 3
y = 9
z = "2.4"
a = True 

# 4a
print("(a):", x/y)

# 4b
print("(b):", x//y) # Floors expression

# 4c
print("(c):", x%y)

# 4d
print("(d): An error would occur processing (y/z * z) due to the fact that strings can only be multiplied by ints.  The result of y/z would be a floating point 3.0")

# 4e
print("(e):",float(x) / float(z))

# 4f
print("(f): An error would occur while trying to cast z to an int due to the fact that its numeric value is 2.4 and not an integer.")

# 4g
print("(g):", a + x)

# 4h
print("(h):", a + a)

# 4i
print("(i):", x/y < 0.3)

# 4j
print("(j):", str(3) > z)
"""
Problem 5
"""
print("\n",40*"-","\n","Problem 5:\n",40*"-")

# 1a
newtons_constant = 6.67e-11
earth_mass = 5.97e24
time_seconds = 5400 # 90 minutes to seconds
time_seconds2 = 2700 # 45 minutes to seconds
time_seconds3 = 86148
earth_radius = 6371000 # 6371 kilometers to meters
altitude = (newtons_constant*earth_mass*(time_seconds**2)/(4*pi**2))**(1/3) - earth_radius # Satellite distance, in meters, from Earth's surface
altitude2 = (newtons_constant*earth_mass*(time_seconds2**2)/(4*pi**2))**(1/3) - earth_radius
altitude3 = (newtons_constant*earth_mass*(time_seconds3**2)/(4*pi**2))**(1/3) - earth_radius

print("(5a): Altitude of a satellite rotating Earth once every 90 minutes: ",
      altitude,"meters from surface.")

print("(5a): Altitude of a satellite rotating Earth once every 45 minutes: ",
      altitude2,"meters from surface.")

print("(5a): We can infer that it's possible for a satellite to orbit Earth " 
      "once every 90 minutes, but not every 45 minutes as indicated by the " 
      "negative output. Most likely because of the significant amount of " 
      "pressure and atmospheric drag.")

print("(5b): I suspect that there will be a tremendous increase in altitude"
      "(for a sidereal day) when compared with the previous part. Plugging in " 
      "86148 seconds(23.93 hours) into our altitude equation results in an " 
      "altitude of: ", altitude3,"meters from Earth's surface. Just as I "
      "suspected.")
