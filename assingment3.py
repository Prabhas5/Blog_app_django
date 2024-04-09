'''Assignment 3: File Handling and Text Processing

Problem Statement: You are given a text file words.txt containing a list of words, 
one word per line. Write a Python script to read the file, find all the anagrams present in the list, 
and group them together. An anagram is a word or phrase formed by rearranging the letters of another word or phrase, 
using all the original letters exactly once. Write the grouped anagrams to an output file anagrams.txt.

Input: A text file words.txt containing a list of words, one word per line.

Output: An output file anagrams.txt containing grouped anagrams, one group per line.'''
#Solutions
def get_signature(word:str):
    #converting word to lower and reearrangin in alphabetical order
    return "".join(sorted(word.lower().strip()))

def group_anagrams(words:list):
    anagram_group={}
    for word in words:
        signature=get_signature(word)
        if signature not in anagram_group:
            anagram_group[signature]=[]
        anagram_group[signature].append(word)
    return anagram_group

def write_to_file(analgam_group:dict,output_file:str):
    with open(output_file,"w") as file:
        for group in analgam_group.values():
            file.write((', '.join(group) + '\n'))

def main(input_file:str,output_file:str):
    #reading file from input
    with open(input_file,"r") as file_handle:
        words=[line.strip() for line in file_handle]
    anagram_groups = group_anagrams(words)
    write_to_file(anagram_groups,output_file)

input_file="words.txt"
output_file="anagrams.txt"
if __name__=="__main__":
    main(input_file,output_file)