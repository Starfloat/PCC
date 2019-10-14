def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())
        
def make_great(magicians, great_magicians):
    while magicians:
        current_magician = 'the Great ' + magicians.pop()
        great_magicians.append(current_magician)
    for magician in great_magicians:
        print(magician)
    
magicians_list = ['bob','billy','alice']
great_magicians = []
make_great(magicians_list, great_magicians)
show_magicians(magicians_list)

