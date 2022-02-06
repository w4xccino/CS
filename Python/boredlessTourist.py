
destinations = ["Paris, France","Shanghai, China", "Los Angeles, USA","São Paulo, Brazil","Cairo, Egypt"]
attractions = [[] for item in destinations]
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

def get_destination_index(destination):
  destination_index = 0
  for i in destinations:
    if i == destination:
      return destination_index
    destination_index += 1

# print(get_destination_index('Shanghai, China'))

def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

test_destination_index = (get_traveler_location(test_traveler))
# print(test_destination_index)

# print(attractions)

#attraction = ['asd',['abd','bca']]
def add_attraction(destination, attraction):
  destination_index = get_destination_index(destination)
  attractions_for_destination = attractions[destination_index] 
  attractions_for_destination.append(attraction)
  return attractions

add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

def find_attractions(destination, interests):
    destination_index = get_destination_index(destination)
    attractions_in_city = attractions[destination_index]
    attractions_with_interest = []
    
    for possible_attraction in attractions_in_city:
        attraction_tags =  possible_attraction[1]
        for interest in interests:
            if interest in attraction_tags:
                attractions_with_interest.append(possible_attraction[0])
    return attractions_with_interest

# print(find_attractions("Los Angeles, USA",["art"]))

def get_attractions_for_traveler(traveler):
   traveler_destination = traveler[1] 
   traveler_interests = traveler[2]
   traveler_attractions = find_attractions(traveler_destination,traveler_interests)
   interest_string = "Hi "
   interest_string += traveler[0]
   interest_string += ", we think you'll like these places around "
   interest_string += traveler_destination 

   string = ": "
   for i in traveler_attractions:
        if traveler_attractions.index(i) < len(traveler_attractions) - 1:
            string += i + ", "
        else:
            string += i + "."
   interest_string += string 
   return interest_string
print(get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']]))

