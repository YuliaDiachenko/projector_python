def number_of_hats(cats: list) -> int:
    cats = dict(cats)
    hats = list(cats.values())
    return hats.count(True)

size = 100
storage = [[i, False] for i in range(size)]

for circle in range(size):
    for st in storage[circle::circle+1]:    
        num_cat, hat = st
        st[1] =True if not hat else False

cats_with_hats = {"No "+str(cat+1) : hat for cat, hat in storage if hat == True} 

print("\nCats with hats are :" , list(cats_with_hats.keys()))
print("Number of cats\' hats: ", number_of_hats(storage))
    
