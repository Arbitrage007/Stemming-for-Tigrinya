import codecs
# prefix
pre=codecs.open("pre1.txt","r","utf-8-sig")
prefix=pre.read()
prefix_words=tuple(sorted(prefix.split(),key=len,reverse=True)) # in order for long match
#print(prefix_words)

# postfix
post=codecs.open("post1.txt","r","utf-8-sig")
postfix=post.read()
postfix_words=tuple(sorted(postfix.split(),key=len,reverse=True)) # long match
#print(postfix_words)

# stopwords
stopW= codecs.open("stopword.txt", "r", "utf-8-sig")
stopword= stopW.read()
stop_words = tuple(stopword.split())
#print(stop_words)

# exceptions
exceptionW= codecs.open("exception.txt", "r", "utf-8-sig")
exception=exceptionW.read()
exception_words=tuple(exception.split())
#print(exception_words)

# length rule
def str_len(word):
    return len(word)<=2

# remove the postfix
def postfix_remove(word):
    for pfix in postfix_words:
            if word.endswith(pfix):
                new_word=word.replace(pfix,'')
                return new_word

# remove the postfix
def prefix_remove(word):
    for prefx in prefix_words:
            if word.startswith(prefx):
                new_word=word.replace(prefx,'')
                return new_word

# check if the word is stopword
def isStopword(word):
    return word in stop_words

# check if the word is exception word
def isException(word):
    return word in exception_words

 
# removes duplicate 
def remove_duplicate(word):
    val={"ሃሀ":"ሀ","ላለ":"ለ","ላል":"ለ","ሓሐ":"ሐ","ማመ":"መ","ራረ":"ረ","ሳሰ":"ሰ","ሻሸ":"ሸ","ቃቀ":"ቀ","ቓቐ":"ቐ",
         "ባበ":"በ","ቫቨ":"ቨ","ታተ":"ተ","ቻቸ":"ቸ","ናነ":"ነ","ኛኘ":"ኘ","ኣአ":"አ","ካከ":"ከ","ኻኸ":"ኸ",
         "ዋወ":"ወ","ዓዐ":"ዐ","ዛዘ":"ዘ","ዣዠ":"ዠ","ያየ":"የ","ዳደ":"ደ","ጣጠ":"ጠ","ጫጨ":"ጨ","ፃፀ":"ፀ","ፋፈ":"ፈ","ፓፐ":"ፐ",
        "ከድ":"ከደ","ላዕ":"ልዐ","መፃ":"መፀ","መፅ":"መፀ"}
    
    new_word=word
    for w in val.keys():
        if w in word:
            new_word=word.replace(w,val[w])
            return new_word
    return new_word

# stemming process
def Stem_It(input_snt):
	stem_result = ''          # a variable that holds the stemmed result
	space = ' '
	for word_index in range(len(input_snt)):
	    Tword=input_snt[word_index]
	    if isStopword(Tword):
	        continue
	    elif isException(Tword) or str_len(Tword):
	        stem_result += space + Tword
	    elif Tword.endswith(postfix_words):
	        step1=postfix_remove(Tword)
	        if str_len(Tword):
	            stem_result += space + step1
	        elif step1.startswith(prefix_words):
	            step2 = prefix_remove(step1)
	            stem_result += space + step2
	        else:
	            stem_result += space + step1
	    elif Tword.startswith(prefix_words):
	        step3 = prefix_remove(Tword)
	        stem_result += space + step3
	    else:
	        stem_result += space + Tword
	return stem_result

# accept input to be stemmed
input_snt = input().split() 
last_val=remove_duplicate(Stem_It(input_snt))
print(last_val)

# print the output
result = Stem_It(input_snt)
print(result)

# save the result in file [optional]
#with open("output.txt", "w",encoding='utf-8') as f:
    #f.write(result)
#f.close()
