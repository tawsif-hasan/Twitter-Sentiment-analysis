punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
#Removing punctuations
def strip_punctuation(string1):
    punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
    for char in string1:
        if char in punctuation_chars:
            string1=string1.replace(char,"")
    return string1

# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
#function to return the count of positive words from a text
def get_pos(string2,count_pos=0):
    string2=strip_punctuation(string2)
    string2=string2.lower()
    wrds=string2.split()
    for wrd in wrds:
        if wrd in positive_words:
            count_pos=count_pos+1
    return count_pos

#negative words to use
negative_words = []
with open("negative_words.txt") as pos_f:
    #print(pos_f.read())
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

#function to return the count of negative negative_words
def get_neg(string2,count_neg=0):
    string2=strip_punctuation(string2)
    string2=string2.lower()
    wrds=string2.split()
    for wrd in wrds:
        if wrd in negative_words:
            count_neg=count_neg+1
    return count_neg


twitter_data=open("project_twitter_data.csv","r")
#print(twitter_data.read())
lines=twitter_data.readlines()
header=lines[0]
field_names = header.strip().split(',')
lst=[]
#iterating through the lines to find the required counts
for row in lines[1:]:
    t_r_r = row.strip().split(',')
    tweet=t_r_r[0]
    retweet_count=int(t_r_r[1])
    reply_count=int(t_r_r[2])
    tweet=strip_punctuation(tweet)
    pos_count=get_pos(tweet)
    neg_count=get_neg(tweet)
    net_score=pos_count-neg_count
    tupple= (retweet_count,reply_count,pos_count,neg_count,net_score)
    lst=lst+[tupple]
#print(lst)
#print(tupple)
#print(net_score)
print(tweet)
print(pos_count)
print(neg_count)
print(retweet_count)
print(t_r_r)
resulting_data=open("resulting_data.csv","w")
resulting_data.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
resulting_data.write("\n")
for tupples in lst:
    row_string="{},{},{},{},{}".format(tupples[0],tupples[1],tupples[2],tupples[3],tupples[4])
    resulting_data.write(row_string)
    resulting_data.write("\n")
resulting_data.close()
