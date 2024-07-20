def number_of_words(text):
    return len(text.split())

def number_of_characters(text):
    char_count = {}
    
    for char in text.lower():
        
        if not char.isalpha():
            continue
        
        if not char in char_count:
            char_count[char] = 0
        
        char_count[char] += 1
        
    return char_count

def most_found(dict):
    max_num = float("-inf")
    max_char = ""
    
    for i in dict:
        if dict[i] > max_num:
            max_num = dict[i]
            max_char = i
            
    return max_char, max_num

def generate_report(text):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"\n{number_of_words(text)} words found in the document\n")
    
    chars = number_of_characters(text)
    max_char, max_num = most_found(chars)
    
    sorted_chars = sorted(chars)    
    
    for char in sorted_chars:
        print(f"The '{char}' character was found {chars[char]} times!")
    
    print(f"\nyour most found character was '{max_char}' with {max_num} ocurrences!")
        
    print("\n--- End report ---")
        
        
def main():
    with open("books/frankenstein.txt") as f:
        file_content = f.read()
        
    generate_report(file_content)
  
        
main()