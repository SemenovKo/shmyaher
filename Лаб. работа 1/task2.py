# TODO Найдите количество книг, которое можно разместить на дискете
space = 1.44 * 1024 * 1024
books =  4*25*50*100
books_in_space = round(space/books)

print("Количество книг, помещающихся на дискету:", books_in_space)
