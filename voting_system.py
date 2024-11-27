print('Welcome to e-voting system , kindly cast your vote')
print('Follow the instructions to votes')
print('1. Enter you id code ')
print('2. Choose yes or no for votes')
print('3. Do not choose  two options ')



# Brothers_wins ,sisters_wins,tahiru_wins will print the total vote result for each constestant 
Brothers_wins = 0
Sisters_wins = 0
Tahiru_wins =  0

# it will store the voter_ids to prevent mutiple voting 
voted_ids = []
# only allow the ids in the set to vote
eligible_voters = ['b1', 'b2', 'b3']

#it wiil make the code to continue runing until all registers voters have voteded 
while True:
    user_input = input('Please Enter your ID code: ')
    if user_input not in ('b1','b2','b3') :
        print('not qualified')
        continue


    if user_input in voted_ids:
        print('You have already voted!')
        continue
    # it will send the voters_ids into the empty set to prevent mutiple voting 
    voted_ids.append(user_input)

# The random_code will allow only the partcipant who have be registered to vote from the
#  eligible voters from the number 0-2 depending on the voters registered 
    

    print('Brothers for SRC presidents')
    Brothers = input('VOTE - yes/no: ')
    print('Sisters for SRC presidents')
    Sisters = input('Vote - yes/no: ')
    print('Tahiru for SRC presidents')
    Tahiru = input('Vote - yes/no: ')
    

    # to check if a voter choose two option it should not count until the person choose one option 
    if Brothers == 'yes' and  Sisters == 'no'  and  Tahiru  == 'no':
        Brothers_wins += 1
        
    elif Sisters == 'yes' and Brothers == 'no' and Tahiru == 'no':
        Sisters_wins += 1
        
    elif Tahiru == 'yes' and Brothers == 'no' and Sisters == 'no':
        Tahiru_wins += 1
        
   # elif Tahiru == 'yes' and Sisters == 'no' and Brothers == 'no':
        #Tahiru_wins += 1 
        
    #elif Brothers == 'no' and Sisters == 'yes' and Tahiru == 'no':
        #Sisters_wins += 1
    #elif Sisters == 'no' and Brothers == 'yes' and Tahiru == 'no':
        #Brothers_wins += 1
    #elif Tahiru == 'no' and Brothers == 'yes' and Sisters ==  'no':
        #Brothers_wins += 1
    #elif Tahiru == 'no' and Sisters == 'yes' and Brothers == 'no':
        #Sisters_wins += 1 
    

          

    





# this will prevent voters form selecting two option when voting and it will continue until they select only one option 
    else:
        print(' cannot choose two option.NOT COUNTED! ')
        continue

    

    # Check if all eligible voters have voted
    if len(voted_ids) == len(eligible_voters):
        print('All eligible voters have voted.')
        # print the result and number of voters who has votered 
        print('Total votes cast:', len(voted_ids))
        print('Brothers got', Brothers_wins, 'votes.')
        print('Sisters got', Sisters_wins, 'votes.')
        print('Tahiru got', Tahiru_wins, 'votes.')
        
    # stop the loop if all registered voters have voted 
        break


