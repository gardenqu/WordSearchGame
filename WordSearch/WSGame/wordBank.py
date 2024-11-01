from .trieTree import Trie
import random
import string

'''
This class will be what gets the words and places them into a trieTree,creates the matrix, and validates the correctly selected words

'''
class WordBank:
    def __init__(self):
        self.wordbank=Trie()

    def get_words(self,category, list_size, max_length):



        food_list = [
        "Pizza",
        "Burger",
        "Sushi",
        "Pasta",
        "Salad",
        "Sandwich",
        "Steak",
        "Tacos",
        "Pancakes",
        "Dumplings",
        "Curry",
        "Noodles",
        "Paella",
        "Burrito",
        "Ramen"]

        sports_list = [
            "Soccer",
            "Tennis",
            "Basketball",
            "Baseball",
            "Golf",
            "Cricket",
            "Rugby",
            "Swimming",
            "Volleyball",
            "Badminton",
            "Hockey",
            "Table Tennis",
            "Cycling",
            "Running",
            "Boxing"]
            
        bank={'Sports':sports_list, 'Food':food_list}

        if category in bank:

            # Filter words based on the length constraint
            filtered_words = [word for word in bank[category] if len(word) < max_length]

            # Randomly sample up to 5 words from the filtered list
            for word in random.sample(filtered_words,list_size):
                self.wordbank.insert(word.upper())

        else:
            return None  

        
    def insert_words_into_Tree(self,wordsList):
        
        pass



    def fill_empty_spaces(self,grid):
        size = len(grid)
        for i in range(size):
            for j in range(size):
                if grid[i][j] == ' ':
                    grid[i][j] = random.choice(string.ascii_uppercase)
                        
    


  
            
    def create_word_matrix(self,size):

        # Create a size X size gride with random letters
        grid=[[random.choice(' ') for letter in range(size)] for letter in range(size)]
        print(self.wordbank.print_words())

        for word in self.wordbank.print_words():
            word_length = len(word)
            prev=0
            print(word)

             # Randomly choose direction: 0 = horizontal, 1 = vertical
            direction = random.choice([0, 1])
            placed = False
            
            while not placed:  # Loop until the word is successfully placed

                if direction == 0:  # Horizontal
                    row = random.randint(0, size - 1)
                    col = random.randint(0, size - word_length)
                    can_place = True  # Flag to check if we can place the word

                    for i in range(word_length):
                        current_char = grid[row][col + i]
                        

                        if current_char != ' ' and current_char != word[i]:
                            can_place = False  # Can't place the word here
                            break  # Exit the loop as we found a conflict

                    if can_place:  # If we can place the word, place it
                        for i in range(word_length):
                            grid[row][col + i] = word[i]
                        placed = True  # Set flag to true since word is placed

                else:  # Vertical
                    row = random.randint(0, size - word_length)
                    col = random.randint(0, size - 1)
                    can_place = True  # Flag to check if we can place the word

                    for i in range(word_length):
                        current_char = grid[row + i][col]
    

                        if current_char != ' ' and current_char != word[i]:
                            can_place = False  
                            break  

                    if can_place:  
                        for i in range(word_length):
                            grid[row + i][col] = word[i]
                        placed = True 

        self.fill_empty_spaces(grid)

                
        return grid



     
     
     