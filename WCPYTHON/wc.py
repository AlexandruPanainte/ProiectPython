import os
import sys

custom_options_flag = 0
options = [1 for i in range(5)]
possible_options = ['-l', '-L', '-c', '-w', '-m']
options_in_input = []
check_input = 0

# newline, word, character, byte, max_width
# l, w, m, c, L

def word_count(file):
    if options[0] == 1:
        option_l(file)
    if options[1] == 1:
        option_w(file)
    if options[2] == 1:
        option_m(file)
    if options[3] == 1:
        option_c(file)
    if options[4] == 1:
        option_L(file)


def option_c(file):
    print("Number of bytes: " + str(os.path.getsize(file)))


def option_m(file):
    # exclude spaces exclude newlines
    characters = open(file, 'r').read().replace(" ", "").replace("\n", "")

    print("Number of characters: " + str(len(characters)))


def option_l(file):
    lines = sum(1 for line in open(file))
    print("Number of lines: " + str(lines))


def option_L(file):
    max_width = 0
    for line in open(file):
        # ignore newline
        if len(line) - 1 > max_width:
            max_width = len(line) - 1
    print("Maximum line width: " + str(max_width))


def option_w(file):
    words = open(file).read().split()
    print("Number of words: " + str(len(words)))


if len(sys.argv) == 1:
    print("No argument given")
    exit()

for i in range(1, len(sys.argv)):
    if sys.argv[i] not in possible_options:
        check_input = 1
    if sys.argv[i][0] == '-' and check_input == 1:
        print("Invalid input!")
        exit()
    if sys.argv[i] in possible_options:
        if sys.argv[i] not in options_in_input:
            options_in_input.append(sys.argv[i])
        else:
            print("Invalid input!")
            exit()


for i in range(1, len(sys.argv)):
    if sys.argv[i] == "--help":
        print("Help: https://man7.org/linux/man-pages/man1/wc.1.html")
        exit()

    if sys.argv[i] == "-l":
        if custom_options_flag == 0:
            custom_options_flag = 1
            options = [0 for i in range(5)]
        options[0] = 1

    elif sys.argv[i] == "-w":
        if custom_options_flag == 0:
            custom_options_flag = 1
            options = [0 for i in range(5)]
        options[1] = 1

    elif sys.argv[i] == "-m":
        if custom_options_flag == 0:
            custom_options_flag = 1
            options = [0 for i in range(5)]
        options[2] = 1

    elif sys.argv[i] == "-c":
        if custom_options_flag == 0:
            custom_options_flag = 1
            options = [0 for i in range(5)]
        options[3] = 1

    elif sys.argv[i] == "-L":
        if custom_options_flag == 0:
            custom_options_flag = 1
            options = [0 for i in range(5)]
        options[4] = 1

    elif os.path.isfile(sys.argv[i]):
        print("\nFile path: "+sys.argv[i])
        word_count(sys.argv[i])
    else:
        print("Error at argument " + str(i))
