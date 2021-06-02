import math

''' PART 1.a)'''
def cosine_similarity(vec1, vec2):
    numerator = 0
    mag_vec1 = 0
    mag_vec2 = 0
    for key,value in vec1.items():
        if key in vec2.keys():
            numerator += (vec1.get(key)*vec2.get(key))
    for values in vec1.values():
        mag_vec1 += (values**2)
    for values in vec2.values():
        mag_vec2 += (values**2)
    denominator = ((math.sqrt(mag_vec1))*(math.sqrt(mag_vec2)))
    if numerator != 0:
        return (numerator/denominator)
    else:
        return 0

''' PART 1.b)'''
def find_index(list,word):
    for i in range(len(list)):
        if word == list[i]:
            return i

# def check_word(word,sentence, index):
#     for i in range(index):
#         if word
#

def build_semantic_descriptors(sentences):
    words = [],[]
    for i in sentences:
        for j in i:
            if j not in words[0]:
                words[0].append(j)
                words[1].append(0)
    descriptors = {}
    for i in words[0]:
        for j in sentences:
            if i in j:
                for n in range(len(j)):
                    if j[n] != i and j[n] not in j[0:n]:
                        d = find_index(words[0],j[n])
                        words[1][d] += 1
        descriptor = {}
        for j in range(len(words[0])):
            if words[1][j] != 0:
                descriptor[words[0][j]] = words[1][j]
        descriptors[i] = descriptor
        for i in range(len(words[1])):
            words[1][i] = 0
    return descriptors

'''d = [["i", "am", "a", "sick", "man"]]
["i", "am", "a", "spiteful", "man"],
["i", "am", "an", "unattractive", "man"],
["i", "believe", "my", "liver", "is", "diseased"],
["however", "i", "know", "nothing", "at", "all", "about", "my",
"disease", "and", "do", "not", "know", "for", "certain", "what", "ails", "me"]]'''



'''PART 1.c) '''
def build_semantic_descriptors_from_files(filenames):
    global mega
    curated = []
    mega = ''
    for i in range(len(filenames)): # append all files into one megafile
        f = open(filenames[i], "r", encoding="latin1")
        f = (f.read())

        if i == 0:
            mega = f
        else:
            mega +='.'+f
        # for i in range(len(f)):
        #     if isinstance(f[i],int):
        #         print(f[i])
 # trying to replace all integers to empty spaces
    mega = mega.replace('!','.')
    mega = mega.replace('?','.')
    for i in [",", "-", "--", ":", ";"]:
        mega = mega.replace(i, " ")
    mega = mega.split('.')
    i = 0
    while '' in mega:
        if mega[i] == '':
            del mega[i]
            i = 0
        i += 1
    for i in range(len(mega)):
        curated.append(mega[i].split())
    for i in range(len(curated)):
        for j in range(len(curated[i])):
            curated[i][j] = curated[i][j].lower()
    return build_semantic_descriptors(curated)


dict = build_semantic_descriptors_from_files(['swann.txt'])

'''PART 1.d)'''
def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    descript_word = semantic_descriptors.get(word)
    best = ''
    value = -1.0
    for i in choices:
        descript = semantic_descriptors.get(i,0)
        if descript != 0:
            if similarity_fn(descript_word,descript) > value:
                best = i
                value = similarity_fn(descript_word,descript)
    if value == -1.0 and best == '':
        return choices[0]
    return best

#print(most_similar_word('hi',['true'],dict, cosine_similarity))

'''PART 1.e)'''
def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    f = open(filename,"r", encoding='latin1')
    s = f.readlines()
    for i in range(len(s)):
        s[i] = s[i].replace('\n','')
        s[i] = s[i].split(' ')
    num_questions = 0
    num_correct = 0
    for i in range(len(s)):
        ans = ''
        ans = str(most_similar_word(s[i][0], s[i][2:len(s[i])], semantic_descriptors, similarity_fn))
        print(ans,s[i][1])
        num_questions += 1
        if ans == s[i][1]:
            num_correct += 1
    return num_correct/num_questions*100

print(run_similarity_test('sample_test.txt', dict, cosine_similarity))














