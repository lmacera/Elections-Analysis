Counties = ["Arapahoe", "Denver", "Jefferson"]
if Counties [1] == 'Denver' :
    print(Counties[1])
if "El Paso"  in Counties :
    print("El Paso is in the list of counties")
else:
    print(" El Paso is not in the list of counties")
if "Arapahoe" in Counties or "El Paso" in Counties:
    print(" Arapahoe and El Paso are in the list of counties")
else:
    print( "Arapahoe or El Paso is not in the list of counties")
for county in Counties:
    print(county)
for num in range(7):
    print(num)
counties_disct = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for x in counties_disct:
    print(counties_disct[x])
for X, Y in counties_disct.items():
    print( X, "county has", Y, "voters registered") 
    voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
for X in voting_data:
    for Y in X.values():
            print(Y)
for X in voting_data:
    print(X["registered_voters"])
candidate_votes = int(input(" how many votes did the canadate get?"))
total_votes = int(input(" How many total votes were recieved?"))
candidate_message = (
    f" You recieved {candidate_votes:,} number of votes"
    f" The total number of votes were {total_votes:,}."
    f" You recieved {candidate_votes/total_votes * 100:.2f}% of the total votes.")
print(candidate_message)

