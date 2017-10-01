def freq(word_list):
    input_file = open('paragraph.txt', 'r')
    word_list = []
    for line in input_file:
        temp = line.rstrip('\n')
        print temp
        line_word_list = temp.split(" ")
        print line_word_list
        word_list.extend(line_word_list)

    print word_list
    return;
