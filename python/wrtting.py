# cities = ["Adelaie",'Alice Springs','Darwin','melbourne','Sydney']

# with open("cities.txt",'w') as city_files:
#     for city in cities:
#         print(city, file=city_files)

# cities = []
# with open("cities.txt",'r') as city_files:
#     for city in city_files:
#         cities.append(city.strip("\n"))

# print(cities)
# for city in cities:
#     print(city)

# imelda = "More Mayhem",'Imelda May',"2011",(
#     (1,"pulling the rug"),(2,"Psycho"),(3,"Mayhem"),(4,"Kentish Town waltz"))

# with open("imelda3.txt",'w') as imelda_file:
#     print(imelda,file=imelda_file)

with open ("imelda3.txt",'r') as imelda_file:
    contents = imelda_file.readline()

imelda = eval(contents)

print(imelda)
title,artist,year,tracks =imelda
print(title)
print(artist)
print(year)
