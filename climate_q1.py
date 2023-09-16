import sqlite3
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect("climate.db")
cursor = conn.cursor()

# Fetch data from the database and populate lists 
cursor.execute("SELECT years, co2, temp FROM climate_data")
rows = cursor.fetchall()
for row in rows:
    years.append(row[0])
    co2.append(row[1])
    temp.append(row[2])

# Close the database connection
conn.close()

years = []
co2 = []
temp = []

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.show() 
plt.savefig("co2_temp_1.png") 
