#An empty list of people who are attending game night.
gamers = []

#Check that the argument passed to the gamer parameter has both "name" and a "availability" as keys and if so add gamer to gamers_list
def add_gamer(gamer, gamers_list):
    if gamer.get("name") and gamer.get("availability"):
        gamers_list.append(gamer)
    else:
        print("Gamer missing critical information")


#Adding gamers to the list
add_gamer({'name':'Kimberly','availability': ["Monday", "Tuesday", "Friday"]}, gamers)
add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)


#A function that returns a dictionary with the days of the week. We'll be using this to count the availability per night.
def build_daily_frequency_table():
    return {
        "Monday":0,
        "Tuesday":0,
        "Wednesday":0,
        "Thursday":0,
        "Friday":0,
        "Saturday":0,
        "Sunday":0
    }

count_availability = build_daily_frequency_table()


#Function that iterate through each gamer in gamers_list and iterate through each day in the gamer's availability. For each day in the gamer's availability, add one to that date on the frequency table.
def calculate_availability(gamers_list, available_frequency):
    for gamer in gamers_list:
        for available_day in gamer['availability']:
            available_frequency[available_day] += 1


#Calling calculate_availability 
calculate_availability(gamers, count_availability)
print(count_availability)


#A function that returns the key with the highest number.
def find_best_night(availability_table):
    best_availability = 0
    for day, availability in availability_table.items():
        if availability > best_availability:
            best_night = day
            best_availability = availability
    return best_night


#Calling find_best_night to find the best day to host game night.
game_night = find_best_night(count_availability)
print("Best night to host game night: " + game_night)



#A function to return a list of all of the people who are available that night.
def available_on_night(gamers_list, day):
    return [gamer['name'] for gamer in gamers_list if day in gamer['availability']]

attending_game_night = available_on_night(gamers, game_night)
print("People who can attend game night:")
print(attending_game_night)


#Creating a form email to send to each of the participants that we'll fill out with data later.
form_email = """
Dear {name},

The Sorcery Society is happy to host "{game}" night and wishes you will attend. Come by on {day_of_week} and have a blast!

Magically Yours,
the Sorcery Society
"""

#Function to send out email to all the participants
def send_email(gamers_who_can_attend, day, game):
    for gamer in gamers_who_can_attend:
        print(form_email.format(name=gamer, day_of_week=day, game=game))

send_email(attending_game_night, game_night, "Abruptly Goblins!")


#-------------------------------------------------------------------------------------------------------
"""
You feel bad for the folks who weren't able to attend on the decided upon game night,
and try to use your currently written methods to have a second game night of the week.
"""


#A listof everyone in gamers that wasn't able to attend game night.
unable_to_attend_best_night = [gamer for gamer in gamers if game_night not in gamer['availability']]
#Creating a new frequency table
second_night_availability = build_daily_frequency_table()
#Calculating new availability
calculate_availability(unable_to_attend_best_night, second_night_availability)
#Finding best nights for the new participants
second_night = find_best_night(second_night_availability)


#Sending out an email to everyone (whether they can attend the first night or not) whose marked themselves as available on our second game night.
available_second_game_night = available_on_night(gamers, second_night)
send_email(available_second_game_night, second_night, "Abruptly Goblins!")

