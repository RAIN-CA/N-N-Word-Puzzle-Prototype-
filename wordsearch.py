"""
Introduction to Programming: Coursework 1
Please write your name
@author: Yuhui Mao

"""

# Reminder: You are not allowed to import any modules.


def wordsearch(puzzle: list, wordlist: list) -> None:
    if valid_puzzle(puzzle) and valid_wordlist(wordlist):
        flist = []
        for word in wordlist:
            wpos = get_positions(puzzle, word)
            if wpos is not None:
                flist.append(wpos)
        coloured_display(puzzle, flist)
    else:
        print("ValueError, invalid puzzle or wordlist.")


def valid_puzzle(puzzle: list) -> bool:
    length = 0;
    for string in puzzle:
        if isinstance(string, str):
            if length == 0:
                length = len(string)
            if length != len(string):
                return False
        else:
            return False
    return True
            


def valid_wordlist(wordlist: list) -> bool:
    for element in wordlist:
        if type(element) != type(""):
            return False
    return True
            
            


def get_positions(puzzle: list, word: str) -> list:
    row = 0
    rowc = 0
    column = 0
    columnc = 0
    count = 0
    letter_list = []
    word_list = []
    position = []
    position_list = []
    key_word = list(word.upper())
    """straight right"""
    """print(key_word)
    print(len(key_word))"""
    while row < len(puzzle):
        rowc = row
        columnc = column
        while count < len(key_word) and columnc < len(puzzle[0]):
            letter_list.append(puzzle[rowc][columnc])
            position.append((rowc,columnc))
            columnc += 1
            count += 1
        word_list.append(letter_list)
        position_list.append(position)
        letter_list = []
        position = []
        count = 0
        column += 1
        if column > (len(puzzle[0])-len(key_word)):
            row += 1
            column = 0
    row = 0
    column = 0
    while column < len(puzzle[0]):
        rowc = row
        columnc = column
        while count < len(key_word) and rowc < len(puzzle):
            letter_list.append(puzzle[rowc][columnc])
            position.append((rowc,columnc))
            rowc += 1
            count += 1
        word_list.append(letter_list)
        position_list.append(position)
        letter_list = []
        position = []
        count = 0
        row += 1
        if row > (len(puzzle)-len(key_word)):
            column += 1
            row = 0
    
    row = 0
    column = 0
    while row < len(puzzle):
        rowc = row
        columnc = column
        while count < len(key_word) and rowc < len(puzzle) and columnc < len(puzzle[0]):
            letter_list.append(puzzle[rowc][columnc])
            position.append((rowc,columnc))
            rowc += 1
            columnc += 1
            count += 1
        word_list.append(letter_list)
        position_list.append(position)
        letter_list = []
        position = []
        count = 0
        column += 1
        if column > (len(puzzle[0])-len(key_word)) or row > (len(puzzle)-len(key_word)):
            row += 1
            column = 0
    
    row = 0
    column = 0
    while row < 11:
        rowc = row
        columnc = column
        while count < len(key_word) and rowc < len(puzzle) and columnc < len(puzzle[0]):
            if rowc < 0 or columnc < 0:
                break;
            letter_list.append(puzzle[rowc][columnc])
            position.append((rowc,columnc))
            rowc -= 1
            columnc += 1
            count += 1
        word_list.append(letter_list)
        position_list.append(position)
        letter_list = []
        position = []
        count = 0
        column += 1
        if column > (len(puzzle[0])-len(key_word)):
            row += 1
            column = 0
    
    """print(word_list)
    print(position_list)"""
    
    keys = []
    k = 0
    rev = 0
    revs = {}
    for word2 in word_list:
        if word2 == key_word:
            keys.append(k)
            rev = 0
            revs[k]=rev
        k += 1
    k = 0
    for word2 in word_list:
        if word2 == key_word[::-1]:
            keys.append(k)
            rev = 1
            revs[k]=rev
        k += 1
    """print(keys)
    print(revs)"""
    re_list = []
    if keys == []:
        print(f"'{word}' not found.")
    for key in keys:
        if revs[key] == 1:
            position_list[key].reverse()
            re_list.append(position_list[key])
            return re_list
        else:
            re_list.append(position_list[key])
            return re_list


def basic_display(grid: list) -> None:
    for row in grid:
        string = ""
        for word in row:
            string += " "
            string += word.upper()
            string += " "
        print(string)


def coloured_display(grid: list, positions: list) -> None:
    rowk = []
    columnk = []
    for single_position in positions:
        for position in single_position:
            for pos in position:
                rowk.append(pos[0])
                columnk.append(pos[1])
    rcount = 0
    while rcount < len(grid):
        ccount = 0
        while ccount < len(grid[0]):
            key = 0
            for n in range(0,len(rowk)):
                if rcount == rowk[n] and ccount == columnk[n]:
                    key = 1
            if key == 1:
                print(f'\033[42m {grid[rcount][ccount]} \033[0m', end='')
            else:
                print(f' {grid[rcount][ccount]} ', end='')
            ccount += 1
        print('\n', end='')
        rcount += 1
            


# =============================================================================
# Do not remove the followings. To test your functions
# =============================================================================


def test_valid_wordlist():
    """
    Test function valid_wordlist()
    """
    good_wordlist = ["scalar", "tray", "blew", "sevruc", "testing"]
    good_wordlist2 = ["scalar", "tray", "blew", "sevruc"]
    bad_wordlist2 = ["scalar", "tray", "blew", "sevruc", 59]

    print("wordlist is", valid_wordlist(good_wordlist))
    print("wordlist is", valid_wordlist(good_wordlist2))
    print("wordlist is", valid_wordlist(bad_wordlist2))


def test_valid_puzzle():
    good_puzzle = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
                   'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
                   'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']

    bad_puzzle1 = ['RUNAROUNDDL', 'EDCITOAHC', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
                   'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
                   'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']

    bad_puzzle2 = ['RUNAROUNDDL', ['EDCITOAHCYV'], ('ZYUWSWEDZYA'),
                   'AKOTCONVOYV', 'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL',
                   'ISTREWZLCGY', 'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']

    print("puzzle is", valid_puzzle(good_puzzle))
    print("puzzle is", valid_puzzle(bad_puzzle1))
    print("puzzle is", valid_puzzle(bad_puzzle2))


def test_basic_display():
    puzzle1 = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
               'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
               'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']
    basic_display(puzzle1)
    basic_display([['a', 'b', 'c', 'd', 'e'], ['h', 'l', 'j', 'k', 'l']])


def test_get_positions():
    puzzle1 = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
               'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
               'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']
    get_positions(puzzle1, "TESTING")
    print(get_positions(puzzle1, "TRAY"))


def test_coloured_display():
    puzzle1 = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
               'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
               'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']
    good_wordlist2 = ["scalar", "tray", "blew", "sevruc"]
    final_list = []
    for word in good_wordlist2:
        temp = get_positions(puzzle1, word)
        if temp is not None:
            final_list.append(temp)
    coloured_display(puzzle1, final_list)


def test_wordsearch():
    puzzle1 = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
               'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
               'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']
    good_wordlist2 = ["scalar", "tray", "blew", "sevruc"]
    wordsearch(puzzle1, good_wordlist2)


if __name__ == "__main__":
    # uncomment the test function individually
    # basic solution
    # test_valid_puzzle()
    # test_valid_wordlist()
    # test_basic_display()

    # full solution
    # test_coloured_display()
    # test_get_positions()
    test_wordsearch()
