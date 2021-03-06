Problem_Set_3

   # Problem_1
#This script opens a file, uses a for loop to read through the file line by line 
#and calculate the maximum water level and the date in which it was observed. 

def main():
    filepath = 'CO-OPS__8729108__wl.csv'
    maximum = 0
    with open('CO-OPS__8729108__wl.csv','r') as fp:
        for line in fp:
            line_bits = line.split(",")
           # print (line_bits)
            try:   
                next_item = float(line_bits[1])
            except:
                continue
            if next_item > maximum:
                maximum = next_item
                date = line_bits[0]
    print(maximum, date)
    
    main()
    
    
    
    # Problem_2
#This script imports pandas and opens a file into the pandas dateframe.
#It then calculates the maximum water level with the date and time it was observed.

    import pandas as pd

df = pd.read_csv('CO-OPS__8729108__wl.csv')

df.loc[df[' Water Level'].idxmax()]



    # Problem_3
#This script opens a file, calculates the fastest rise in water level per 6-minute period between measurements 
#and provides the time and date in which it was observed as well as the change in water level during that period.

    maximum = 0
    previous_line = 0
    maxdiff = 0
    with open('CO-OPS__8729108__wl.csv','r') as fp:
        for line in fp:
            line_bits = line.split(",")
           # print (line_bits)
            try:   
                next_item = float(line_bits[1])
                
            except:
                continue
            if next_item > maximum:
                maximum = next_item
                date = line_bits[0]
            
            diff = previous_line - next_item
            
            if diff > maxdiff:
                maxdiff = diff
                datemax = line_bits[0]
            previous_line = next_item
                
    print(maximum, date)
    print(maxdiff, datemax)

