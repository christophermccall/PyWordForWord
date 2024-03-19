import os
print(">>>start")

# content = file.read()
# print(type(content))
# print(content)
# file.close()

def read_file(filename):
    file = open(filename, 'r')
    content = file.read()
    file.close()
    return content

def wc(inpustring):
    wds_list = inpustring.split()
    chs =len(inpustring)#words
    wds = len(wds_list)
    lns = 0

    for ch in inpustring:
        if ch == '\n':
          lns += 1


    return lns, wds, chs



def word_frequency(inputstring):
    d= {}
    wds_list = inputstring.split()
    for word in wds_list:
        if word in d:
            d[word]+=1
        else:
            d[word] = 1

    return d



def char_frequency(inputstring):
    chlist = 'abcdefghijklmopqrstuvwxyz'
    d= {}
    wds_list = inputstring.split()
    for word in wds_list:
        chword = list(word)
        for ch in chword:
            if ch in chlist:
                if ch in d:
                    d[ch] += 1
                else:
                    d[ch] = 1

    return d


def char_distribution(inputstring):
    chlist = 'abcdefghijklmopqrstuvwxyz'
    d= {}
    wds_list = inputstring.split()
    wdlistlen = len(wds_list)
    for word in wds_list:
        chword = list(word)
        for ch in chword:
            if ch in chlist:
                if ch in d:
                    d[ch] += 1
                else:
                    d[ch] = 1
    percents = {k: '{:.0f}'.format(v/wdlistlen * 100) + '%' for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}

    return percents

#
#
# value = {"Company": "GeeksforGeeks",
#          "Department": "Computer Science"}
#
# # Using f-strings
# print(f"{value['Company']} is a {value['Department']} Portal.")
#

def word_distribution(input_string):
    d = {}
    wds_list = input_string.split()
    wdlistlen = len(wds_list)
    for word in wds_list:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1

    percents = {k: '{:.4f}'.format(v/wdlistlen * 100) + '%' for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}

    return percents

# def print_file(file_name):
#     print("start")
#     file = open(file_name)
#     while True:
#         content = file.readline()
#         print(content)
#         if not content:
#             break
#     print("End of file?", end='')
#     file.close()
#
#
# print_file("testdata/testdata3.txt")
#

txt = read_file("testdata/testdata7.txt")
test = wc(txt)
srtdct = word_distribution(txt)

print(srtdct)
