"""
reads a paragraph of text
and creates a dictionary of words and frequency mapping
"""

#----
#make this part into a function
#input: file name string
#output: list of words contained in the filename
#----
def my_list(str):
    input_file = open("paragraph.txt", "r")
    word_list = []
    for line in input_file:
        temp = line.rstrip('\n')
        print temp
        line_word_list = temp.split(" ")
        print line_word_list
        word_list.extend(line_word_list)
    print word_list
    return;
my_list(open("paragraph.txt", "r"))

 


#----- 
#--------

#-----make this part into a function
#input: list of words
#output: dictionary of words counts

    
def word_counts(word_list):
    word_counts = {}
    for i in word_list:
        if i in word_counts:
            word_counts[i] = word_counts[i] + 1
        else:
            word_counts[i] = 1
    print word_counts
    return ;
   



output_file = open('wordcounts.txt', 'w')
output_file.write(str(word_counts))




