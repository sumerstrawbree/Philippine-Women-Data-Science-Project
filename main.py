# This code is written in python
# The pandas library is used for data processing and to read data files
import pandas as pd 
#The matplotlib library is used to plot histograms and scatter plots
import matplotlib.pyplot as plt
# The GWCutilities has functions to help format data printed to the console
import GWCutilities as util

# Read a comma separated values (CSV) files into a variable
# as a pandas DataFrame
lwd=pd.read_csv("livwell135.csv")


print("The Philippines is a country in Southeast Asia, consisting of 7,641 islands with Manila as its capital, has 94.8% national electricity access.\n") 

print("However, high electricity costs make it hard for Filipino households, spending 15.7% of their income on electricity. For women, these costs can result in more physical labor around the house.\n")

print("Although female labor force participation increased from 50% in 2013 to 52.3% in 2023, marriage and caring for young children make employment more difficult.\n")

print("Reliable electricity can help women become more economically confident by supporting their businesses, families, and financial stability.\n")

input("Press return to continue.\n")

# Print out the number of rows and columns
print(lwd.shape)

#  basic colors:
# 'blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black', 'white'

# create a scatter plot
oneCountryBooleanList = lwd["country_name"]=="Philippines"

oneCountryData = lwd.loc[oneCountryBooleanList]

plt.scatter(oneCountryData["year"],oneCountryData["EI_women_elec_p"],color="magenta")

# add a title to the plot
plt.title("Percent of Women Living in a Household with Electricity")

#Label the x-axis
plt.xlabel("Year")

# label the y-axis
plt.ylabel("Women living in a household with electricity (%)")

# set the range for the y-axis
plt.ylim(0,100)

# show the plot
plt.show()

print(oneCountryData["EI_women_elec_p"])

print("\nResearch Question: How does access to electricity affect women's economic opportunities and labor force participation in the Philippines?")
