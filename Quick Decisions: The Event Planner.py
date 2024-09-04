
attendees = int(input("Enter number of attendees: "))
venue = "large hall" or "conference room"
if (attendees >= 200 and attendees <= 300) and venue == "large hall":
    print("Time for a great feast!")
elif attendees <= 100 and venue == "conference room": 
    print("Eat up join the banquet!")
elif attendees > 10 and attendees > 300:
    print("After a successful dinner, enjoyed listening and dancing to music")
else:
    print("Enjoying the Gourmet Meals Catering!")



# attendees = int(input("Enter number of attendees: "))
# venue = "large hall" or "conference room"
# if attendees > 100 and venue == "large hall":
#     print(venue)
# elif attendees < 100 and venue != "large hall":
#     print(venue)







attendees = int(input("Enter number of attendees: "))
venue = "large hall" or "conference room"
if (attendees >= 200 and attendees <= 300) and venue == "large hall":
    print("Time for a great feast!")
    if attendees <= 100 and venue == "conference room": 
        print("Eat up join the banquet!")
    elif attendees > 10 and attendees > 300:
        print("After a successful dinner, enjoyed listening and dancing to music")
else:
    print("Enjoying the Gourmet Meals Catering!")