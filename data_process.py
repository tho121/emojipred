import emoji

#Replace usernames and links, remove newlines, and write to the given file handle
def continuous_tweet_processing(tweets, filehandle):

    for tweet in tweets.data:
        #print(tweet)
        if tweet.lang == 'en':
            text = tweet.text.replace("\n", " ")

            #replace users (@someusername) with [USR]
            text = " ".join([ch.split('@')[0] + "[USR]" if "@" in ch else ch for ch in text.split()])

            #replace links (https://somelink) with [LNK]
            text = " ".join([ch.split("https:")[0] + "[LNK]" if "https:" in ch else ch for ch in text.split()])
            
            filehandle.write(text + "\n")

#identify all emojis, split the text accordingly, extract text segments that direction proceed of the emojis in the list
#format for a csv file
def tweet2csv(line, emoji_list_icons):
    emjs = [e for e in emoji_list_icons if e in line]

    processed_lines = []
    emj_label = []
    text = ""

    #print(line)
    for emj in emjs:
        line_split = line.split(emj, 1)
        text = line_split[0]   #get string that preceeds this emoji

        if text == "":  
            continue

        #check if preceeding string has emojis and remove if so
        #this purposely ignores cases where emojis are used as part of the vocabulary
        if emoji.emoji_count(text) > 0:  
            continue

        processed_lines.append(text)
        emj_label.append(emj)

        line = line_split[1]

    formatted_text_all = []

    for i in range(len(processed_lines)):
                    formatted_text = emj_label[i] + "," + processed_lines[i] + "\n"
                    formatted_text_all.append(formatted_text)

    return formatted_text_all