
import json
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_espn_logo():
    print("EEEEEEE  SSSSSSS  PPPPPPP   NNN   NNN")
    print("E        S         P     PP  NNNN  NNN")
    print("E        S         PPPPPPP   NN NNNNNN")
    print("EEEEEEE   SSSSSS   P         NN  NNNN")
    print("E               S  P         NN   NNN")
    print("E               S  P         NN    NN")
    print("EEEEEEE  SSSSSSS   P         NN    NN")
    print("")


def opening():
    print("Welcome to the March Madness Simulator!")
    print("This program will simulate the 2021 NCAA March Madness Tournament")
    print("")
    print_espn_logo()


def attribute_statistics_with_teams_playing(team_array, json_array):
    for data in json_array:
        for team in data:
            for team_playing in team_array:
                if team_playing == team['Team']:
                    team_array[team_array.index(team_playing)] = team
    return team_array

def calcute_win_probability(team1, team2):
    team1_chances = 0
    team2_chances = 0

    if(team1['GP'] > team2['GP']):
        team1_chances += 1
    if (team1['GP'] < team2['GP']):
        team2_chances += 1
    
    if (team1['PTS'] > team2['PTS']):
        team1_chances += 1
    if (team1['PTS'] < team2['PTS']):
        team2_chances += 1

    if (team1['FG%'] > team2['FG%']):
        team1_chances += 1
    if (team1['FG%'] < team2['FG%']):
        team2_chances += 1

    if (team1['3P%'] > team2['3P%']):
        team1_chances += 1
    if (team1['3P%'] < team2['3P%']):
        team2_chances += 1

    if (team1['FT%'] > team2['FT%']):
        team1_chances += 1
    if (team1['FT%'] < team2['FT%']):
        team2_chances += 1

    if (team1['REB'] > team2['REB']):
        team1_chances += 1
    if (team1['REB'] < team2['REB']):
        team2_chances += 1
    
    if (team1['AST'] > team2['AST']):
        team1_chances += 1
    if (team1['AST'] < team2['AST']):
        team2_chances += 1

    if (team1['STL'] > team2['STL']):
        team1_chances += 1
    if (team1['STL'] < team2['STL']):
        team2_chances += 1

    if (team1['BLK'] > team2['BLK']):
        team1_chances += 1
    if (team1['BLK'] < team2['BLK']):
        team2_chances += 1

    if (team1['TO'] > team2['TO']):
        team2_chances += 1
    if (team1['TO'] < team2['TO']):
        team1_chances += 1
    
    if (team1['PF'] > team2['PF']):
        team2_chances += 1
    if (team1['PF'] < team2['PF']):
        team1_chances += 1

    # compare the chances of each team winning
    if (team1_chances > team2_chances):
        return team1
    else :
        return team2


clear_screen()
opening()

# Open the JSON file
with open('basketball_stats.json') as file:
    # Load the contents of the file into a variable
    json_data = json.load(file)



# Teams playing
south_group = ["Alabama Crimson Tide", "Texas A&M-Corpus Christi Islanders", 
"West Virginia Mountaineers", "Maryland Terrapins", 
"Charleston Cougars", "San Diego State Aztecs", 
"Furman Paladins", "Virginia Cavaliers", 
"NC State Wolfpack", "Creighton Bluejays",
 "UC Santa Barbara Gauchos", "Baylor Bears", 
 "Missouri Tigers", "Utah State Aggies", 
 "Arizona Wildcats", "Princeton Tigers"]


east_group = ["Texas Southern Tigers", "Purdue Boilermakers", "Memphis Tigers", "Florida Atlantic Owls",
 "Duke Blue Devils", "Oral Roberts Golden Eagles",
 "Tennessee Volunteers", "Louisiana Ragin' Cajuns",
 "Providence Friars", "Kentucky Wildcats",
 "Kansas State Wildcats", "Montana State Bobcats",
 "Michigan State Spartans", "USC Trojans",
 "Vermont Catamounts", "Marquette Golden Eagles"]

west_group = ["Howard Bison", "Kansas Jayhawks",
 "Arkansas Razorbacks", "Illinois Fighting Illini",
 "Saint Mary's Gaels", "VCU Rams",
 "Iona Gaels", "UConn Huskies",
 "Arizona State Sun Devils", "TCU Horned Frogs",
 "Grand Canyon Lopes", "Gonzaga Bulldogs", 
 "Boise State Broncos", "Northwestern Wildcats",
 "UNC Asheville Bulldogs", "UCLA Bruins"]

midwest_group = ["Northern Kentucky Norse", "Houston Cougars",
"Iowa Hawkeyes", "Auburn Tigers",
"Drake Bulldogs", "Miami Hurricanes",
"Kent State Golden Flashes", "Indiana Hoosiers",
"Pittsburgh Panthers", "Iowa State Cyclones", 
"Xavier Musketeers", "Kennesaw State Owls", 
"Penn State Nittany Lions", "Texas A&M Aggies",
"Texas Longhorns", "Colgate Raiders"]


# Attributing statistics from JSON file with the teams playing
south_group = attribute_statistics_with_teams_playing(south_group, json_data)
east_group = attribute_statistics_with_teams_playing(east_group, json_data)
west_group = attribute_statistics_with_teams_playing(west_group, json_data)
midwest_group = attribute_statistics_with_teams_playing(midwest_group, json_data)


# SOUTH
print("-------------------- SOUTH ---------------------")
south_winner1 = calcute_win_probability(south_group[0], south_group[1])
print("From the South group 1, the winner is: " + south_winner1['Team'] + "")

south_winner2 = calcute_win_probability(south_group[2], south_group[3])
print("From the South group 2, the winner is: " + south_winner2['Team'] + "")

south_winner3 = calcute_win_probability(south_group[4], south_group[5])
print("From the South group 3, the winner is: " + south_winner3['Team'] + "")

south_winner4 = calcute_win_probability(south_group[6], south_group[7])
print("From the South group 4, the winner is: " + south_winner4['Team'] + "")

south_winner5 = calcute_win_probability(south_group[8], south_group[9])
print("From the South group 5, the winner is: " + south_winner5['Team'] + "")

south_winner6 = calcute_win_probability(south_group[10], south_group[11])
print("From the South group 6, the winner is: " + south_winner6['Team'] + "")

south_winner7 = calcute_win_probability(south_group[12], south_group[13])
print("From the South group 7, the winner is: " + south_winner7['Team'] + "")

south_winner8 = calcute_win_probability(south_group[14], south_group[15])
print("From the South group 8, the winner is: " + south_winner8['Team'] + "")

south_quarterfinals1 = calcute_win_probability(south_winner1, south_winner2)
print("From the South quarterfinals 1, the winner is: " + south_quarterfinals1['Team'] + "")

south_quarterfinals2 = calcute_win_probability(south_winner3, south_winner4)
print("From the South quarterfinals 2, the winner is: " + south_quarterfinals2['Team'] + "")

south_quarterfinals3 = calcute_win_probability(south_winner5, south_winner6)
print("From the South quarterfinals 3, the winner is: " + south_quarterfinals3['Team'] + "")

south_quarterfinals4 = calcute_win_probability(south_winner7, south_winner8)
print("From the South quarterfinals 4, the winner is: " + south_quarterfinals4['Team'] + "")

south_semifinal1 = calcute_win_probability(south_quarterfinals1, south_quarterfinals2)
print("From the South semifinals 1, the winner is: " + south_semifinal1['Team'] + "")

south_semifinal2 = calcute_win_probability(south_quarterfinals3, south_quarterfinals4)
print("From the South semifinals 2, the winner is: " + south_semifinal2['Team'] + "")

south_final = calcute_win_probability(south_semifinal1, south_semifinal2)
print("From the South finals, the winner is: " + south_final['Team'] + "")
print(" ------------------------------ ")


# WEST
print("-------- WEST GAMES! --------")
west_winner1 = calcute_win_probability(west_group[0], west_group[1])
print("From the West group 1, the winner is: " + west_winner1['Team'] + "")

west_winner2 = calcute_win_probability(west_group[2], west_group[3])
print("From the West group 2, the winner is: " + west_winner2['Team'] + "")

west_winner3 = calcute_win_probability(west_group[4], west_group[5])
print("From the West group 3, the winner is: " + west_winner3['Team'] + "")

west_winner4 = calcute_win_probability(west_group[6], west_group[7])
print("From the West group 4, the winner is: " + west_winner4['Team'] + "")

west_winner5 = calcute_win_probability(west_group[8], west_group[9])
print("From the West group 5, the winner is: " + west_winner5['Team'] + "")

west_winner6 = calcute_win_probability(west_group[10], west_group[11])
print("From the West group 6, the winner is: " + west_winner6['Team'] + "")

west_winner7 = calcute_win_probability(west_group[12], west_group[13])
print("From the West group 7, the winner is: " + west_winner7['Team'] + "")

west_winner8 = calcute_win_probability(west_group[14], west_group[15])
print("From the West group 8, the winner is: " + west_winner8['Team'] + "")

west_quarterfinals1 = calcute_win_probability(west_winner1, west_winner2)
print("From the West quarterfinals 1, the winner is: " + west_quarterfinals1['Team'] + "")

west_quarterfinals2 = calcute_win_probability(west_winner3, west_winner4)
print("From the West quarterfinals 2, the winner is: " + west_quarterfinals2['Team'] + "")

west_quarterfinals3 = calcute_win_probability(west_winner5, west_winner6)
print("From the West quarterfinals 3, the winner is: " + west_quarterfinals3['Team'] + "")

west_quarterfinals4 = calcute_win_probability(west_winner7, west_winner8)
print("From the West quarterfinals 4, the winner is: " + west_quarterfinals4['Team'] + "")

west_semifinal1 = calcute_win_probability(west_quarterfinals1, west_quarterfinals2)
print("From the West semifinals 1, the winner is: " + west_semifinal1['Team'] + "")

west_semifinal2 = calcute_win_probability(west_quarterfinals3, west_quarterfinals4)
print("From the West semifinals 2, the winner is: " + west_semifinal2['Team'] + "")

west_final = calcute_win_probability(west_semifinal1, west_semifinal2)
print("From the West finals, the winner is: " + west_final['Team'] + "")
print(" ------------------------------ ")

# EAST
print("-------- EAST GAMES! --------")
east_winner1 = calcute_win_probability(east_group[0], east_group[1])
print("From the East group 1, the winner is: " + east_winner1['Team'] + "")

east_winner2 = calcute_win_probability(east_group[2], east_group[3])
print("From the East group 2, the winner is: " + east_winner2['Team'] + "")

east_winner3 = calcute_win_probability(east_group[4], east_group[5])
print("From the East group 3, the winner is: " + east_winner3['Team'] + "")

east_winner4 = calcute_win_probability(east_group[6], east_group[7])
print("From the East group 4, the winner is: " + east_winner4['Team'] + "")

east_winner5 = calcute_win_probability(east_group[8], east_group[9])
print("From the East group 5, the winner is: " + east_winner5['Team'] + "")

east_winner6 = calcute_win_probability(east_group[10], east_group[11])
print("From the East group 6, the winner is: " + east_winner6['Team'] + "")

east_winner7 = calcute_win_probability(east_group[12], east_group[13])
print("From the East group 7, the winner is: " + east_winner7['Team'] + "")

east_winner8 = calcute_win_probability(east_group[14], east_group[15])
print("From the East group 8, the winner is: " + east_winner8['Team'] + "")

east_quarterfinals1 = calcute_win_probability(east_winner1, east_winner2)
print("From the East quarterfinals 1, the winner is: " + east_quarterfinals1['Team'] + "")

east_quarterfinals2 = calcute_win_probability(east_winner3, east_winner4)
print("From the East quarterfinals 2, the winner is: " + east_quarterfinals2['Team'] + "")

east_quarterfinals3 = calcute_win_probability(east_winner5, east_winner6)
print("From the East quarterfinals 3, the winner is: " + east_quarterfinals3['Team'] + "")

east_quarterfinals4 = calcute_win_probability(east_winner7, east_winner8)
print("From the East quarterfinals 4, the winner is: " + east_quarterfinals4['Team'] + "")

east_semifinal1 = calcute_win_probability(east_quarterfinals1, east_quarterfinals2)
print("From the East semifinals 1, the winner is: " + east_semifinal1['Team'] + "")

east_semifinal2 = calcute_win_probability(east_quarterfinals3, east_quarterfinals4)
print("From the East semifinals 2, the winner is: " + east_semifinal2['Team'] + "")

east_final = calcute_win_probability(east_semifinal1, east_semifinal2)
print("From the East finals, the winner is: " + east_final['Team'] + "")
print(" ------------------------------ ")



# MIDWEST
print("-------- MIDWEST GAMES! --------")
midwest_winner1 = calcute_win_probability(midwest_group[0], midwest_group[1])
print("From the Midwest group 1, the winner is: " + midwest_winner1['Team'] + "")

midwest_winner2 = calcute_win_probability(midwest_group[2], midwest_group[3])
print("From the Midwest group 2, the winner is: " + midwest_winner2['Team'] + "")

midwest_winner3 = calcute_win_probability(midwest_group[4], midwest_group[5])
print("From the Midwest group 3, the winner is: " + midwest_winner3['Team'] + "")

midwest_winner4 = calcute_win_probability(midwest_group[6], midwest_group[7])
print("From the Midwest group 4, the winner is: " + midwest_winner4['Team'] + "")

midwest_winner5 = calcute_win_probability(midwest_group[8], midwest_group[9])
print("From the Midwest group 5, the winner is: " + midwest_winner5['Team'] + "")

midwest_winner6 = calcute_win_probability(midwest_group[10], midwest_group[11])
print("From the Midwest group 6, the winner is: " + midwest_winner6['Team'] + "")

midwest_winner7 = calcute_win_probability(midwest_group[12], midwest_group[13])
print("From the Midwest group 7, the winner is: " + midwest_winner7['Team'] + "")

midwest_winner8 = calcute_win_probability(midwest_group[14], midwest_group[15])
print("From the Midwest group 8, the winner is: " + midwest_winner8['Team'] + "")

midwest_quarterfinals1 = calcute_win_probability(midwest_winner1, midwest_winner2)
print("From the Midwest quarterfinals 1, the winner is: " + midwest_quarterfinals1['Team'] + "")

midwest_quarterfinals2 = calcute_win_probability(midwest_winner3, midwest_winner4)
print("From the Midwest quarterfinals 2, the winner is: " + midwest_quarterfinals2['Team'] + "")

midwest_quarterfinals3 = calcute_win_probability(midwest_winner5, midwest_winner6)
print("From the Midwest quarterfinals 3, the winner is: " + midwest_quarterfinals3['Team'] + "")

midwest_quarterfinals4 = calcute_win_probability(midwest_winner7, midwest_winner8)
print("From the Midwest quarterfinals 4, the winner is: " + midwest_quarterfinals4['Team'] + "")

midwest_semifinal1 = calcute_win_probability(midwest_quarterfinals1, midwest_quarterfinals2)
print("From the Midwest semifinals 1, the winner is: " + midwest_semifinal1['Team'] + "")

midwest_semifinal2 = calcute_win_probability(midwest_quarterfinals3, midwest_quarterfinals4)
print("From the Midwest semifinals 2, the winner is: " + midwest_semifinal2['Team'] + "")

midwest_final = calcute_win_probability(midwest_semifinal1, midwest_semifinal2)
print("From the Midwest finals, the winner is: " + midwest_final['Team'] + "")
print(" ------------------------------ ")


# FINAL FOUR
print("-------- FINAL FOUR GAMES! --------")
final_four1 = calcute_win_probability(east_final, south_final)
print("From the Final Four 1, the winner is: " + final_four1['Team'] + "")

final_four2 = calcute_win_probability(midwest_final, west_final)
print("From the Final Four 2, the winner is: " + final_four2['Team'] + "")
print(" ------------------------------ ")

# CHAMPIONSHIP
print("-------- CHAMPIONSHIP GAMES! --------")
championship = calcute_win_probability(final_four1, final_four2)
print("From the Championship, the winner is: " + championship['Team'] + "")
print(" ------------------------------ ")









