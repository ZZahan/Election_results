
# The data we need to retive.
# 1. Total number of votes cas
# 2. A Complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular voie.
import csv

import os

# Assign a variable tof the file load and the path.


file_to_load = 'Resources/election_results.csv'


#Open the election results and read the file

# with open(file_to_load) as election_data:
    
    
#     csv_reader = csv.reader(election_data, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are {", ".join(row)}')
#             line_count += 1
#         else:
#            print(row)
#            line_count += 1
#     print(f'Processed {line_count} lines.')

    # To do : perfom analysis.
    
    
    

# exit(0)

#Assign a variable for the file to load and the path.

file_to_load = os.path.join("Resources", "election_results.csv")

#Open the election results and read the file.

# with open(file_to_load) as election_data:
    
    
    #print the file object.
    # print(election_data)
    
    # Create a filename variable to the direct or indirect path to the file.
    
    # file_to_save = os.path.join("analysis", "election_analysis.txt")
    
    # # Using the open() function with the "w" mode we wil write data to the file.
    
    # open(file_to_save, "w")
    
    # # Create a files name variable to a direct or indirect path to the file.
    
    # file_to_save = os.path.join("analysis", "election-resluts.txt")
    
    
    # # Use the open statement to open the file a text file.
    
    # outfile = open(file_to_save, "w")
    
    # # Write same date to the file.
    
    # outfile.write("Hello World")
    
    # #Close the file
    
    # outfile.close()
    
    # Create a filename variable to a direct or indirect pth to the file.
    
file_to_save = os.path.join("analysis", "election_analysis.txt")
    
    
    # using the with statment open the file as text file.
with open(file_to_save, "w") as txt_file:
        
    
        #Write saem data to the file.
    # txt_file.write("Hello World, ")
        
        
            # Wirte three counties to the file
        
    # txt_file.write ("Arapahoe, ")
    # txt_file.write("Denver, ")
    # txt_file.write("Jefferson")
        
        # Write three counties to the file.
        
    # txt_file.write("Arapahoe, ")
    # txt_file.write("Denver, ")
    # txt_file.write("Jefferson")
    
    # Wirte three counties to the file.
   
    # txt_file.write("Arapahoe, denver, Jefferson")
        
    
   # Write three counties to the file.
   
    
    
    txt_file.write("Counties in the Election\n-\nArapahoe\nDenver\nJefferson") 
    
    # Add our dependencies 
    
    import csv
    
    import os
    
    # Assign a variable to load a file from a path.
    
    file_to_load = os.path.join("Resources", "election_results.csv")
    
    # Assign a variable to save the file to a path.
    
    file_to_save = os.path.join("analysis", "election_analysis.txt")
    
    
    # Open the election resluts and read the file.
    
    with open(file_to_load) as election_data:
        
        #To do: read and analyze the data here.
        
        # read the file object with the reader function.
    
        file_reader = csv.reader(election_data)

        # Print each rwo in the CSV file.
    
        # for row in file_reader:
            
           
    
            # print(row[0])
            
        # Read the file with the reader function.
    
        file_reader = csv.reader(election_data)
    
        # Print the dearder row.
    
        headers = next(file_reader)
    
        print(headers)
        
        
                   
            
            
        
    
    
    
    
    