# Sukurkite klasę "Movie", kuri gebės sukurti objektus 3 savybėm ir 1 metodu. 
# Naudojant šią klasę sukurkite bent du skirtingus objektus.

# Savybės:
# title: string
# director: string
# budget: number

# Metodas: 
# wasExpensive() - jeigu filmo "budget" yra daugiau nei 100 000 000 mln USD, tada grąžins True, kitu atveju False. 


print('------------------------------------------------------------')
class Movie:
    def __init__(self, title, director, budget):
        self.title = title
        self.director = director
        self.budget = budget
        
    def wasExpensive(self):
            if self.budget > 100000000:
                print(f'The movie "{self.title}" budget is more than 100 000 000 mln USD. The actual budget is {self.budget} mln USD. \nThe statement is equal to', True)
            else:
                print(f'The movie "{self.title}" budget is less than 100 000 000 mln USD. The actual budget is {self.budget} mln USD. \nThe statement is equal to', False)


movieObject1 = Movie('Avatar: The Way of Water','James Cameron', 4600000000 )
movieObject2 = Movie('My Big Fat Greek Wedding','Joel Zwick', 5000000 )

movieObject1.wasExpensive()
movieObject2.wasExpensive()

print('------------------------------------------------------------')
