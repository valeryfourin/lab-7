
book1={'circulation':45000, 'author':'J.K.Rowling ', 'name':'"Harry Potter" ', 'genre':'fantasy'}
book2={'circulation':9000, 'author':'Ulf Stark ', 'name':'"Sixten" ', 'genre':'adventure'}
book3={'circulation':7600, 'author':'Charles Dickens ', 'name':'"Oliver Twist" ', 'genre':'Novel'}
books=list((book1,book2,book3))

for i in books:
    if i['circulation']<10000:
        print(f'{dict.items(i)}')
    else: continue
