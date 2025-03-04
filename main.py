# from restaurantTables import restaurant_tables2 

# Level One:

# The Goal of this level is to list all free tables in a chosen timeslot. A free space will be recognized as 'o' and occupied space as '
# After recognizing each of these free tables in a specific timeslot, the code must output a list of table IDs representing free tables.
# These table IDs are represented by the table number.


# To store the tables availablity and timeslots in one piece of data, I will be using a 2D array as it lets me define the rows as timeslots and columns as tables.

# I will be taking inspiration from the restaurantTables.py's array given to us (Link here: https://github.com/CedriHerna/Elite-101-Coding-Assessment-2025).
# I think that the use a 2D array with proper lables at the top array was a splended idea because it both saves extra explaining and helps readablity of the code.

availability_of_tables = [['0', 'Table One', 'Table Two', 'Table Three', 'Table Four', 'Table Five'], #The top row is just for labels of the data below. The 0 for the first row represents it not being a row for timeslots
                          ['1', 'x','o','o','o','o'],   #'o' is an available space | 'x' is an unavailable space
                          ['2', 'x','o','o','o','o'],
                          ['3', 'x','o','o','o','o']]

# For this array, I want Table One to always be occupied so that I can test Level One's goal

# Now that I have my data, I want ot create a function that looks inside of my 2D array and then returns the tables that are open at a certain time slot.

def available_tables(timeslot): #Here I want to ask for the timeslot as an input so that I can specifically scan one timeslot's tables for availablity
    
    current_table = 1   #To ensure that I don't start looking for tables on the column that tells us which timeslot we are on, I am starting the search on column 1.
    free_tables = ''    #This is the string I will be returning which will hold the table ID of each available table.
    while(len(availability_of_tables[timeslot]) > current_table): #This states that it will repeat the loop until the end of the array.
        
        if(availability_of_tables[timeslot][current_table] == 'o'):  #This checks if the certain table on the timeslot we are checking is available.
            free_tables += str(current_table) + ' '                  # if it is available, add the Table ID to the free_tables string.

        current_table += 1                                           #This continues the iteration and ensures the while loop doesn't loop forever.

    if(free_tables == ''):                                           #This is an excpetion checker that checks if there is no available tables.
        return print(f'No Available tables at timeslot {timeslot}')
    else:                                                            #Since we checked the case that there are available tables, now we can print the table IDs to the user.
        return print(f'Available Tables: ' + free_tables)


print("Level 1")
available_tables(1)                                                #This is my test case. It should return that tables 2,3,4, and 5 are available (which it does!)

# =======================================================
# Level Two:

# Goal: Given a certain number of guests, a function needs to return an available table that has the capasity to seat that number of guests.
# Output: After finding a table that is available, return that single table to the user. 

# Because we need the tables to have their number of seats labled, I am going to recreate the previous 2D array to display the number of seats available_tables

availability_of_tables_and_seats = [['0', 'T1(2)', 'T2(4)', 'T3(6)', 'T4(4)', 'T5(2)'],   #Once again, I am going to be borrowing the naming scheme that the example used because I think that it is a great way to display the table number and how many seats it holds.
                                    ['1', 'x','o','o','o','o'], 
                                    ['2', 'x','o','o','o','o'],
                                    ['3', 'x','o','o','o','o']]

# Now that I have my updated array holding the number of seats within parentheses, I can start creating the function.

def party_size_one_available_table(timeslot, party_size):  #Here I now ask for the party size as well because I need to look if a table has enough seats for them.

    #First I want to find that tables that will be able to fit the party size. Then I want to look at which of those tables has the capasity to hold them.

    current_table = 1 #Again, this is to start looking at the column where the table's availbity is stored.
    while(current_table < len(availability_of_tables_and_seats[timeslot])):
        
        # Since the way I named my tables will always be the same, I know that my number of seats value will be inbetween the two parentheses
        # I will use this information to create an integer which will then be compared the the number of party members.
        # If that comparison tells me the amount of people fit and the table is available, then I will return the table ID to the user.

        current_availablity = availability_of_tables_and_seats[timeslot][current_table]     #This variable tells the code whether or not the table is available or occupied with the symbol 'o' and 'x' respectively

        open_parantheses = availability_of_tables_and_seats[0][current_table].find('(') + 1  #This variable holds the index in the string that is just after the parantheses so that I can get the numbers that holdthe number of seats
        closed_parantheses = availability_of_tables_and_seats[0][current_table].find(')')    # This variable is the end bound that is non inclusive and allows the future variable to only hold the number of seats at a table rather than the closed parantheses sign.

        current_available_seats = availability_of_tables_and_seats[0][current_table]   #This finds the table's details which are at the row 0.
        current_available_seats = current_available_seats[open_parantheses:closed_parantheses] #This specifically pulls out the numbers inbetween the parantheses of the table details.

        if(current_availablity == 'o' and int(current_available_seats) >= party_size):  #This compares to see if both the table is available and has enough seats for the whole group coming to sit at the table.
            return print(f'Table {current_table} is available.')  
        else:
            current_table += 1   #This allows the while loop to continue itterating
        
    return print('No available tables at this timeslot')   # In case the group is too large, the excpetion here helps report that to the user.


print("\nLevel 2")
party_size_one_available_table(1, 2)                                                 #This tests if a table for at least 2 people is available, which should be table 2 since table 1 is occupied.


# =======================================================
# Level Three:

# Goal: Given a certain party size, a function needs to return all the available tables that can seat them.
# Output: After finding all the available tables, the function needs to return all the available tables at no matter what timeslot they are in

availability_of_tables_and_seats = [['0', 'T1(2)', 'T2(4)', 'T3(6)', 'T4(4)', 'T5(2)'],   #For simplicity, I am using the same array as on Level Two
                                    ['1', 'x','o','o','o','o'], 
                                    ['2', 'x','o','o','o','o'],
                                    ['3', 'x','o','o','o','o']]

def party_size_available_tables(party_size):

    all_available_tables = 'All the available tables include: \n'                                          #This string will hold all the available tables.
    current_timeslot = 1                                                                                   #Since I am using a while loop, I must define the initial bound timeslot outside of the while loop it is currently itterating through.
    while(current_timeslot < len(availability_of_tables_and_seats)):                                       #Since the length of an array is just the total amount of things within it, the current timeslot is being compared to the total amount of items within the array, which for this array is the total amount of timeslots.
        
        current_table = 1                                                                                  #To ensure that we restart at the first table everytime this itterates, current table is reset right outside its while loop in the timeslot while loop.

        while(current_table < len(availability_of_tables_and_seats[current_timeslot])):                    #This while loops wants to continue itterating until the current_table value reaches the total amount of tables at a certain time slot.
            
            current_availablity = availability_of_tables_and_seats[current_timeslot][current_table]        #This variable tells the code whether or not the table is available or occupied with the symbol 'o' and 'x' respectively

            open_parantheses = availability_of_tables_and_seats[0][current_table].find('(') + 1    #This variable holds the index in the string that is just after the parantheses so that I can get the numbers that holdthe number of seats
            closed_parantheses = availability_of_tables_and_seats[0][current_table].find(')')      #This variable is the end bound that is non inclusive and allows the future variable to only hold the number of seats at a table rather than the closed parantheses sign.

            current_available_seats = availability_of_tables_and_seats[0][current_table]           #This finds the table's details which are at the row 0.
            current_available_seats = current_available_seats[open_parantheses:closed_parantheses] #This specifically pulls out the numbers inbetween the parantheses of the table details.
            
            if(current_availablity == 'o' and int(current_available_seats) >= party_size):
                all_available_tables += (f'Table {current_table} at timeslot {current_timeslot}\n')#unlike Level 2, this if statement now allows us to add onto the all_available_tables string which will hold all the table IDs
                current_table += 1                                                                 #Also this needs to continue itterating even past the first table
                
            else:
                current_table += 1                                                                 #Continue itterating the tables.

        current_timeslot += 1                                                                      #Continue itterating to the next timeslot.

    if(all_available_tables == 'All the available tables include: \n'):
        return print('No available tables.')
    else:
        return print(f'{all_available_tables}')

print('\nLevel 3')
party_size_available_tables(6)                                                                     #This tests my function to find all the tables that can hold 6 people

# =======================================================
# Level Four:

# Goal: If a single table isn't large enough, the function needs to find an adjacent table to combine with and have enough capasity.
# Output: This function returns a list of both single or adjacent pairs.

availability_of_tables_and_seats = [['0', 'T1(2)', 'T2(4)', 'T3(6)', 'T4(4)', 'T5(2)'],   #For simplicity, I am using the same array as on Level Two
                                    ['1', 'x','o','o','o','o'], 
                                    ['2', 'x','o','o','o','o'],
                                    ['3', 'x','o','o','o','o']]


def combined_and_single_tables(party_size):

    single_tables = 'All the single tables include: \n'
    combined_tables = 'All combined tables include \n'                                                     #This string will hold all the available tables.

    tables_sizes = [] 

    current_table = 1
    while(current_table < len(availability_of_tables_and_seats[0])):                            #This while loop helps me find the number of chairs at each table.

        open_parantheses = availability_of_tables_and_seats[0][current_table].find('(') + 1    #This variable holds the index in the string that is just after the parantheses so that I can get the numbers that holdthe number of seats
        closed_parantheses = availability_of_tables_and_seats[0][current_table].find(')')      #This variable is the end bound that is non inclusive and allows the future variable to only hold the number of seats at a table rather than the closed parantheses sign.

        current_available_seats = availability_of_tables_and_seats[0][current_table]           #This finds the table's details which are at the row 0.
        current_available_seats = current_available_seats[open_parantheses:closed_parantheses] #This specifically pulls out the numbers inbetween the parantheses of the table details.
         
        tables_sizes.append(int(current_available_seats))                                      #This stores the sizes within an array.
        current_table += 1                                                                     #This helps the while loop move to the next itteration. 
                                                  #
    current_timeslot = 1
                                                                                                           #Since I am using a while loop, I must define the initial bound timeslot outside of the while loop it is currently itterating through.
    while(current_timeslot < len(availability_of_tables_and_seats)):                                       #Since the length of an array is just the total amount of things within it, the current timeslot is being compared to the total amount of items within the array, which for this array is the total amount of timeslots.
        
        current_table = 1                                                                                  #To ensure that we restart at the first table everytime this itterates, current table is reset right outside its while loop in the timeslot while loop.
        availablity_temp = 'x'                                                                             #This is a temperary value that will store the PREVIOUS availablity.

        while(current_table < len(availability_of_tables_and_seats[current_timeslot])):                    #This while loops wants to continue itterating until the current_table value reaches the total amount of tables at a certain time slot.
            
            
            
            current_availablity = availability_of_tables_and_seats[current_timeslot][current_table]        #This variable tells the code whether or not the table is available or occupied with the symbol 'o' and 'x' respectively
            

            if(current_availablity == 'o'  and availablity_temp == 'o' and (tables_sizes[current_table - 1] + tables_sizes[current_table - 2]) >= party_size):  #Checks if the table is available, if the table before can conbine with it to create a table large enough for the party  
                
                combined_tables += (f'Tables {current_table} and {current_table - 1} at timeslot {current_timeslot}\n')                                         #The combined tables string gets updated to hold the new combination of tables.
                
            
            if(current_availablity == 'o' and tables_sizes[current_table - 1] >= party_size):

                single_tables += (f'Table {current_table} at timeslot {current_timeslot}\n')     #The single tables string gets updated to hold the single table that can hold the party.          
                      
            availablity_temp = current_availablity                                                #Update the temperary so that it now holds the "previous availablity" for the next itteration.
            current_table += 1                                                                    #Continue itterating to the next table
                                                                          

        current_timeslot += 1                                                                      #Continue itterating to the next timeslot.

    if(single_tables == 'All the single tables include: \n'):                                      #If single tables has the base case, then check if the combnied tables does too. Depending on if it does or not, print combined tables or not.
    
        if(combined_tables == 'All combined tables include \n'):
            
            return print('No available tables.')

        elif(combined_tables != 'All combined tables include \n'):

            return print(combined_tables)
    else:                                                                                          #Since we have single_tables, check whether or not we have combined tables. If we do, print it out with single_tables.

        if(combined_tables == 'All combined tables include \n'):
            
            return print(single_tables)

        elif(combined_tables != 'All combined tables include \n'):

            return print(f'{single_tables}\n{combined_tables}')
    
    
print('\nLevel 4')
combined_and_single_tables(5)

