# Basic Scrabble project to practice Dictionaries uses

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {}

for key, value in zip(letters, points):
    letter_to_points[key] = value

letter_to_points[" "] = 0 # assign a blank space

def score_word(word):
    point_total = 0
    for letra in word:
        point_total += letter_to_points[letra]

    return point_total

# testing the function score_word

brownie_points = score_word("BROWNIE")
print(brownie_points)

player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}
player_to_points = {}
for player, words in player_to_words.items():
  player_points = 0
  for word in words :
    player_points += score_word(word)
    player_to_points[player] = player_points
      
print(player_to_points)

def play_word(player, word):
  if player in player_to_words:
    player_to_words[player].append(word)
  else:
    print("This player doesn't exist!")
    
play_word("player1", "RACKET")
print(player_to_words)
