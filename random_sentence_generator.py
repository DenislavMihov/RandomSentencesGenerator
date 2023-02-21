import random

names = ["Peter", "Michell", "Jane", "Steve", "Gosho",\
         "Asen", "Mitko", "Miroslav", "Denislav", "Stracimir",\
         "Cordoba", "Jelio", "Ivan", "Franck", "Eva" ]

places = ["Golqmo Kunare", "Sofia", "Pernik", "Radomir", "Pravec", "Targovishte"]
verbs = ["eats", "holds", "sees", "plays with", "brings",\
         "running", "scrach his", "rides", "climbing"]

nouns = ["stones", "cake", "apple", "laptop", "bikes",\
         "beer", "mountain", "table", "stairs"]

adverbs = ["slowly", "diligently", "warmly", "sadly", "rapidly",\
           "heavily", "curiously", "daily", "lovingly", "rarely"]

details = ["near the river", "at home", "in the park", "at the stadium", "in musеum"]

def random_word_generator(words):
    return random.choice(words)

print("Hello, this is your first random sentence:")


while True:
    random_name = random_word_generator(names)
    random_place = random_word_generator(places)
    random_verb = random_word_generator(verbs)
    random_noun = random_word_generator(nouns)
    random_adverb = random_word_generator(adverbs)
    random_detail = random_word_generator(details)

    print(f"{random_name} from {random_place} {random_adverb} {random_verb} {random_noun}")
    print("Click [Enter] to generate a new one.")

