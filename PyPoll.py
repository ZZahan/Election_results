
# The data we need to retive.
# 1. Total number of votes cas
# 2. A Complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular voie.
import csv

import os

# Assign a variable tof the file load and the path.


#file_to_load = os.path.join"..", "Resources/election_results.csv")


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
        
    # Add our dependencies
    
    import csv
    
    import os
    
    # Assign a variable to load a file from a path.
    
    file_to_load = os.path.join("Resources", "election_results.csv")
    
    # Assign a variable to save the file to a path.
    
    file_to_save = os.path.join("analysis", "election_analysis.txt")
    
    # Open the election result and read the file.
    
    
    # Initialize a total vote counter.
    
    total_votes = 0
    
    # Candidate options and candidate votes
    
    candidate_options = []
    
    # 1. Declare the empty disctionary.
    
    candidate_votes ={}
    
    #Winning Candidate and Winning Count Tracker
    
    winning_candidate = ""
            
    winning_count = 0
            
    winning_percentage = 0
    
    
    # Open the election results and read the file
    
    with open(file_to_load) as election_data:
        
        file_reader = csv.reader(election_data)
        
        # Read the hearder row.
        
        headers = next(file_reader)
        
        
        # Print each row in the CSV file.
        
        for row in file_reader:
            
            # Add to the total vote count.
            
            total_votes += 1
            
            
            # Print the candidate name from each row.
        
            candidate_name = row[2]
            
            # If the candidate does not match any existing candidate...
            
            if candidate_name not in candidate_options:
        
            # Add the candidate name to the cadidate list.  
            
                candidate_options.append(candidate_name) 
                
                # 2.Begin tracking the candidate's vote count.
                
                candidate_votes[candidate_name] = 0
                
            # Add a vote to that candidate's count.
            candidate_votes[candidate_name] += 1
            
            
        # Print the candidate vote dictionary.
        print(candidate_votes)
            
            
            # Determine the percentage of tvotes for each candidate by looing throgh the coutns.
            
            # 1. Iterate  through the candidate list.
            
        for candidate_name in candidate_votes:
            
            # 2. Retive vote count of a candidate.
            votes = candidate_votes.get(candidate_name)
            
            # 3. Calculate the percentage of votes.
            vote_percentage = float(votes) / float(total_votes) * 100   
    
            # 4. Print the candidate's name, cote count, percentage of 
            # votes to the teriminal.
            
            # Deterimine winning vote count and candidate
            
            Output= f"{candidate_name}: {vote_percentage:.1f}% {votes:,}\n"
            print(Output)
            
            # Determin if the votes is greater than the winning count.
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                
                # If true then set winning_count = votes and winning_percent = 
                # vote_percentage.
                # If (votes> winning_count) and (vote_percentage > winning_percentage)=
                winning_count = votes
                
                winning_percentage = vote_percentage
                
                # And, set the winning_candidate equal to the candidate's name.
                winning_candidate = candidate_name
            
            # To do: print out the winning candidate, vote count and percentage to
            # terminal .
                
                     
            winning_candidate_summary = (
                
                    f"----------------------------\n"
                
                    f"Winner: {winning_candidate}\n"
                
                    f"Winner Vote Count: {winning_count:,}\n"
                
                    f"Winning Percentage: {winning_percentage:.1f}%\n"
                
                    f"------------------------------\n")
                
        print(winning_candidate_summary)
                
            
                        
        
            
       
            
   
    
        
                   
            
            
        
    
    
    
    
    