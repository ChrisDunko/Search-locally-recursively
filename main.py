print( "search for file with name parts of your choosing" )

running = True
while running:
    search_term = input( "Search term: " )
    if search_term == ":q":
        running = False
    else:
        print( search_term )
