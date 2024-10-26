def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)

        words = file_contents.split()
        count = len(words)

        print("\n--- Begin report on books/frankenstein.txt ---")
        print(f"{count} words found in the document\n")

        lower_contents = file_contents.lower()
        character_count = {}

        for char in lower_contents:             # look through lower case contents character-by-character
            if char in character_count:         # if it has already been counted
                character_count[char] += 1
            else:                               # if it hasn't been counted yet
                character_count[char] = 1

        count_alpha = []

        for char in character_count:
            if char.isalpha():                                                          # if it is an alphabet character
                count_alpha.append({"character": char, "count": character_count[char]})    # add the dictionary to the list

        count_alpha.sort(reverse=True, key=sort_on)     # sorts count_alpha decending by count

        for i in count_alpha:
            print(f"The '{i['character']}' character was found {i['count']} times")
        
        print("--- End of report ---")

def sort_on(dict):
    return dict["count"]

main()