from pyscript import document

def candidate_checker(e):
    club_members = ["William Sparks", "Melissa Cooper", "Brick Heck", "Squidward Tentacles", "Eugene Krabs", 
                    "Sheldon Plankton", "Georgie Cooper", "Sheldon Cooper", "Tam Nguyen", "Axl Heck", 
                    "Sue Heck", "Spongebob Squarepants"]
    
    first_name = document.getElementById('first_name').value 
    last_name = document.getElementById('last_name').value
    candidate = first_name + ' ' + last_name # concatenates the items
    member_checker = candidate.title() in club_members # 0 and 1, true or false

    messages = (f'Sorry {candidate}. You are not welcome in our club, better luck next time (╥﹏╥)', f'Congrats {candidate}! You have been accepted into our club ദ്ദി◝ ⩊ ◜.ᐟ') # first message if they arent welcome, second if they are

    document.getElementById('result').innerHTML = messages[member_checker] # shows the message itself