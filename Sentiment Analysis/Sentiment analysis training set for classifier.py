files = glob.glob('/Users/michielv.nederpelt/Downloads/en/mpqa/tab_feature_files/*.csv')
empty_list = []
final_list = []
for file in files:
    #print(file)
    frame= pd.read_csv(file,sep="\t", header=None, names=header_names)
    list_of_tokens = []
    list_of_tokens.append(frame['token'].tolist())
    

    for a in list_of_tokens:
        #string_tokens = str(list_of_tokens)
        string_per_file = " ".join(a)
        #print(string_per_file)
        break
        

    list_of_sentiment = []
    list_of_sentiment.append(frame['sentiment'].tolist())
    #print(list_of_sentiment)

    score = 0
    for a in list_of_sentiment:
        for b in a:
            if b == "B-negative":
                score += -1
            if b == "B-positive":
                score += 1
    #print(score)
    sentiment = ""
    if score > 0:
        sentiment = "positive"
    elif score == 0:
        sentiment = "neutral"
    else:
        sentiment = "negative"
    #print(sentiment)
    sentiment_dict = dict()
    sentiment_dict[string_per_file] = sentiment
    empty_list.append(string_per_file)
    
    #print(sentiment_dict)
    final_list.append(sentiment_dict)
    
print(final_list)
