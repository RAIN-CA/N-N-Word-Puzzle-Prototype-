# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 18:47:47 2022

@author: Mao_Yuhui
"""
# import wordsearch
import random

def get_wordList(word_length: int, amount: int) -> list:
    acount = 0
    word_list = []
    while acount < amount:
        lcount = 0
        word = ''
        """set the minimum number of letters as 3"""
        while lcount < random.randint(3, word_length):
            get_ascii = 0
            """upper: 65~90; lower: 97~122"""
            get_ascii = random.randint(97, 122)
            word += chr(get_ascii)
            lcount += 1
        word_list.append(word)
        acount += 1
    return word_list


def max_word_length(word_list: list) -> int:
    length = 0
    for word in word_list:
        if length < len(word):
            length = len(word)
    return length

def get_puzzle(row: int, column: int) -> list:
    puzzle = []
    rcount = 0
    while rcount < row:
        ccount = 0
        puzzle_row = ''
        while ccount < column:
            get_ascii = 0
            """upper: 65~90; lower: 97~122"""
            get_ascii = random.randint(65, 90)
            puzzle_row += chr(get_ascii)
            ccount += 1
        puzzle.append(puzzle_row)
        rcount += 1
    return puzzle

def get_position(puzzle: list, word: chr) -> list:
    row = len(puzzle)
    column = len(puzzle[0])
    word_length = len(word)
    poslist = []
    repos = []
    
    #horizontal#
    rcount = 0
    while rcount < row:
        ccount = 0
        while ccount < (column - word_length + 1):
            spos = []
            repos =[]
            for n in range(0, word_length):
                spos.append((rcount,ccount+n))
                repos.insert(0, (rcount,ccount+n))
            ccount += 1
            poslist.append(spos)
            poslist.append(repos)
        rcount += 1
    
    #vertical#
    ccount = 0
    while ccount < column:
        rcount = 0
        while rcount < (row - word_length + 1):
            spos = []
            repos =[]
            for n in range(0, word_length):
                spos.append((rcount+n, ccount))
                repos.insert(0, (rcount+n, ccount))
            rcount += 1
            poslist.append(spos)
            poslist.append(repos)
        ccount += 1
    
    #top left to bottom right#
    rcount = 0
    while rcount < (row - word_length + 1):
        ccount = 0
        while ccount < (column - word_length + 1):
            spos = []
            repos =[]
            for n in range(0, word_length):
                spos.append((rcount+n, ccount+n))
                repos.insert(0, (rcount+n, ccount+n))
            poslist.append(spos)
            poslist.append(repos)
            ccount +=1
        rcount += 1
    
    #bottom left to top right#
    rcount = 0
    while rcount < (row - word_length + 1):
        ccount = 0
        while ccount < (column - word_length + 1):
            spos = []
            repos =[]
            for n in range(0, word_length):
                spos.append((rcount-n+word_length-1, ccount+n))
                repos.insert(0, (rcount-n+word_length-1, ccount+n))
            poslist.append(spos)
            poslist.append(repos)
            ccount +=1
        rcount += 1
    
    return poslist

def replace_word(puzzle: list, word: chr, insert_row: int, 
                 insert_column: int) -> list:
    # dismantle the puzzle #
    row= len(puzzle[0])
    column = len(puzzle)
    dpuzzle = []
    rcount = 0
    while rcount < row:
        ccount = 0
        dpuzzle_row = []
        while ccount < column:
            dpuzzle_row.append(puzzle[rcount][ccount])
            ccount += 1
        rcount += 1
        dpuzzle.append(dpuzzle_row)
    # replace the word #
    dpuzzle[insert_row].pop(insert_column)
    dpuzzle[insert_row].insert(insert_column, word.upper())
    # reassemble the puzzle #
    rapuzzle = []
    rcount = 0
    while rcount < row:
        ccount = 0
        rapuzzle_row = ''
        while ccount < column:
            rapuzzle_row += dpuzzle[rcount][ccount]
            ccount += 1
        rcount += 1
        rapuzzle.append(rapuzzle_row)
    return rapuzzle

def conflict_check(used_positions: list,used_words:chr,
                   word: chr, position: list) -> bool:
    for count in range(0, len(word)):
        for n in range(0, len(used_positions)):
            if used_positions[n] == position[count]:
                if used_words[n] != word[count]:
                    return False
    return True

def display_puzzle(puzzle: list) -> None:
    row= len(puzzle[0])
    column = len(puzzle)
    rcount = 0
    while rcount < row:
        ccount = 0
        while ccount < column:
            print(f' {puzzle[rcount][ccount]} ', end='')
            ccount += 1
        rcount += 1
        print('\n', end='')

###############################################################################
# main body #
###############################################################################
word_length = 7
amount = 5
word_list = get_wordList(word_length, amount)
puzzle_auto = get_puzzle(10, 10)
used_positions = []
used_words = []
n = 0
while n < len(word_list):
    position = get_position(puzzle_auto, word_list[n])
    key = random.randint(0, len(position))
    if conflict_check(used_positions, used_words, word_list[n], position[key]):
        for i in range(0, len(word_list[n])):
            puzzle_auto = replace_word(puzzle_auto, word_list[n][i],
                         position[key][i][0], position[key][i][1])
            used_positions.append(position[key][i])
            used_words.append(word_list[n][i])
        n += 1

#print(used_words)
#print(word_list)
#print(used_positions)
# output #
display_puzzle(puzzle_auto)
for word in word_list:
    print(word)
# wordsearch.wordsearch(puzzle_auto, word_list)