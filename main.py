import os 
import csv
#Initialize variables and lists: total_votes, candidate_options
votes = 0 
total_votes = 0
candidate_options = []
candidate_votes = {}
county_list = []
county_votes = {}
winner = ""
winning_count_county = 0
winning_percentage = 0

# Open the election results and read the file.

csv_path = os.path.join("./election_data.csv")
# add a file to save  the anaylsis 
file_to_save = os.path.join("./election_analysis.txt")
with open (csv_path) as csvfile: 
    csvreader =csv.reader(csvfile, delimiter= ",")
    print(csvreader)
    csv_header = next(csvreader)
    print(f"csv_header: {csv_header}")
#create loop 
    for row in csvreader:
        total_votes = total_votes + 1
        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_list:

            # 4b: Add the existing county to the list of counties.
            county_list.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0

        # 5: Add a vote to that county's vote count.
            county_votes[county_name] = county_votes[county_name] + 1


# Save the results to our text file.
    #with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
        election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n")
        #f"county Votes:\n")
    print(election_results, end="")

    #Write a for loop to get the county from the county dictionary.
    for county_name in county_votes:
        county_vote_count = county_votes.get(county_name)
        county_vote_percentage = float(county_vote_count) / float(total_votes) * 100
        county_results = (f"{county_name}: {county_vote_percentage:.1f}% ({county_vote_count:,})\n")
        print(county_results)         
        #Write an if statement to determine the winning county and get its vote count.
    if (county_vote_count > winning_count_county) and (county_vote_percentage > winning_percentage):
        winning_count_county = county_vote_count
        winning_county = county_name
       

    #Print the county with the largest turnout to the terminal.
    winning_county_summary = (
        f"-------------------------\n"
        f"-------------------------\n")
    print(winning_county_summary)

    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        print(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (str(votes) > winning_county) and (vote_percentage > winning_percentage):
            winning_county= votes
            winner = candidate_name
            winning_percentage = vote_percentage


    # Save the winning candidate's name to the text file
    #txt_file.write(winning_candidate_summary)