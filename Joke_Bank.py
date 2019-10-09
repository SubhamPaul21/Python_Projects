# This is a Joke Scraper which uses an API to provide you jokes based on your requirement or choice... Enjoy and Have a laugh :D :D 

#import required modules
import requests
import pyfiglet
import termcolor

# make the header styling
header = pyfiglet.figlet_format('WELCOME TO DAD JOKES!!!')
header = termcolor.colored(header, color='cyan')

print(header)
print('Hello, There!!!')
print()

# define a function to get more jokes if you want
def get_more():
    print()
    decision = input('Want more jokes?(Yes/No) ').lower()
    if decision[0] == 'y':
        print()
        get_joke()
    exit()

# define function to get the joke as required
def get_joke():

    base_url = 'https://icanhazdadjoke.com/'
    print('Choose 1 for Random Joke or 2 for Specified Joke?')
    choice = int(input('> '))
    if choice == 1:
        print()
        print("Here's a Random Joke :")
        response = requests.get(base_url,headers={'Accept':'application/json'}).json()
        print()
        print(response['joke'])
        get_more()
    elif choice == 2:
        print()
        user_input = input("What joke would you like to search for? : ")
        user_input = user_input.lower()
        
        # stop if you input these keywords
        if user_input == ('stop' or 'exit' or 'end'):
            exit()
            print()
        
        # get the response object and make json syntax out of it.
        response = requests.get(base_url + 'search',headers={'Accept':'application/json'},params={'term':user_input}).json()
    
        num_jokes = response['total_jokes']
        
        if num_jokes > 1:
            print()
            print('There are',num_jokes, 'jokes')
            how_many = int(input('How many would you like to see? > '))
            print()
            
            # if you enter more than available joke for a particular term, warn it and start again.
            if num_jokes < how_many:
                print('Enter the value within', num_jokes)
                print()
                get_joke()
            else:
                for i in enumerate(response['results']):
                    id = i[0]
                    if id < how_many:
                        print(i[0] + 1,'.',i[1]['joke'])
                        print()
                        id = id + 1
                get_more()
        elif num_jokes == 1:
            print('There is one joke')
            print()
            print(response['results'][0]['joke'])
            get_more()
        else:
            print('There are no jokes with the search term',user_input, 'try something else')
            get_more()

    else:
        print('Choose 1 or 2')
        get_joke()
        
get_joke()
