# hail mighty travelers, you have reached a quest board. However the board is written in
# the archaic language, something you reckon is called python3.
# the quests have a dictionary, with boss names and how much loot they give you.
# you must find the best boss to kill because you are the best!
#
# hint dictionaries have "keys" that map to "values". If i have a dictionary d, i can access its keys with 
# d.keys(). I can get its values with d.values(). If i do d['key in dictionary'], i will get the value 
# corresponding to 'key in dictionary'. keys need not be strings. You could just as easily have d[1] as a valid key.
# to get a list containing [(key1, value1), (key2, value2), ... ] do dict.items().
# you can iterate this list by doing 
# for key, value in d.items():
#   print(key, value)
# 

from random import randint 

def find_optimal_quest(d):
    
    # write your code here
    # it should return the boss with the best loot! Feel free to ask us questions :)
    pass 
    


# scroll past this
s = '''Gaston Goshorn  
Sandi Stever  
Soila Stalling  
Rocky Reiling  
Renna Rapozo  
Laverne Lague  
Johnnie Junior  
Sherrie Schwenk  
Aracely Aberle  
Tressie Torrey  
Marin Martino  
Valda Vallone  
Trevor Thome  
Reynaldo Raymer  
Genoveva Gridley  
Tama Tirrell  
Janet Jelinek  
Jeannetta Jose  
Felicitas Fertig  
Tambra Toribio  
Britt Boose  
Orville Oommen  
Annmarie Aiello  
Margaret Moreman  
Nicholle Nedd  
Usha Utzinger  
Santina Steptoe  
Cinderella Chamblee  
Tamika Tomer  
Thad Tiano  
Laurette Lindell  
Marcellus Meaney  
Sarita Shams  
Carlena Countryman  
Estell Engleman  
Malika Melson  
Kieth Knupp  
Sebastian Starling  
Suzie Schoenfeld  
Santos Silverio  
Madelaine Minnix  
Sixta Scates  
Dorris Deforest  
An Arruda  
Susannah Scanlon  
Jada Jessen  
Numbers Noonkester  
Josephine Jaramillo  
Magaly Mcgaugh  
Marshall Meany'''

def generate_quest_board():
    d = dict()
    for name in s.split('\n'):
        d[name.strip()] = randint(-1000, 1000)
    return d 
        
def validate_answer(d):
    return max(list((v, k) for (k, v) in d.items()))[1]
   
quests = generate_quest_board()
assert validate_answer(quests) == find_optimal_quest(quests)
