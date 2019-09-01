'''
3-8. Seeing the World: Think of at least five places in the world you’d like to
visit .

3-9. Dinner Guests: Working with one of the programs from Exercises 3-4 
through 3-7 (page 46), use len() to print a message indicating the number
of people you are inviting to dinner .

3-10. Think of something you could store in a list. For example, you could make a list of mountains,
rivers, countries, cities, languages, or anything else you'd like. Write a program that creates a list
of containing these items and then uses each function in this chapter at least once.
.

'''

# 3-8
places_to_visit = ['Japan', 'Norcal', 'Canada', 'Las Vegas', 'Texas']
print(places_to_visit)
print(sorted(places_to_visit))
print(places_to_visit)
sorted(places_to_visit,reverse=True)
print(places_to_visit)
places_to_visit.reverse()
print(places_to_visit)
places_to_visit.reverse()
print(places_to_visit)
places_to_visit.sort()
print(places_to_visit)
places_to_visit.sort(reverse=True)
print(places_to_visit)

# 3-9
guest_list = ['bob', 'alice', 'simon']
print('I have ' + str(len(guest_list)) + ' guests.')

# 3-10
list_of_oceans = ['Pacific', 'Atlantic', 'Indian', 'Southern', 'Arctic']
print(list_of_oceans)
list_of_oceans.sort()
print(list_of_oceans)
list_of_oceans.sort(reverse=True)
print(list_of_oceans)
print(sorted(list_of_oceans)) # does not change the original list
print(sorted(list_of_oceans,reverse=True)) # does not change the original list
list_of_oceans.reverse()
print(list_of_oceans)
print(len(list_of_oceans))
