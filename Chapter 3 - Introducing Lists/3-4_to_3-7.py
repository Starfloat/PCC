'''
3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
would you invite? Make a list that includes at least three people you’d like to
invite to dinner . Then use your list to print a message to each person, inviting
them to dinner .
'''

'''
3-5. Changing Guest List: You just heard that one of your guests can’t make the
dinner, so you need to send out a new set of invitations . You’ll have to think of
someone else to invite.
'''

'''
3-6. More Guests: You just found a bigger dinner table, so now more space is
available . Think of three more guests to invite to dinner.
'''

'''
3-7.  Shrinking Guest List: You just found out that your new dinner table won’t
arrive in time for the dinner, and you have space for only two guests
'''

guest_list = ['bob', 'alice', 'simon'] # 3-4

for guests in guest_list:
    print("Sending invitation to " +  guests.title() + " for dinner.")

print('...')

print('Simon cannot make it for dinner.') # 3-5
print('...')  
print('Inviting Roger instead.')
guest_list.remove('simon')
guest_list.append('roger')
for guests in guest_list:
    print("Sending invitation to " +  guests.title() + " for dinner.")
print('...')

print("Sending message to guest lists that I have obtained a bigger table, allowing more guests.") # 3-6
print('...')
guest_list.insert(0,'bill')
guest_list.insert(3,'mark')
guest_list.append('melanie')
for guests in guest_list:
    print("Sending invitation to " +  guests.title() + " for dinner.")
    
print("...\n Sorry, my new dinner table won't arrive in time, so I onl'y have space for two people.") # 3-7
while len(guest_list) > 2:
    removed_guest = guest_list.pop()
    print("Sorry "+ removed_guest.title() + ", I cannot invite you to dinner for today.")
for guests in guest_list:
    print(guests.title() + " you are still invited for dinner, please come tonight.")

while len(guest_list) > 0:
    del guest_list[0]
print(guest_list)





