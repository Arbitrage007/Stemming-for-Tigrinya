# Open the document to be stemmed
import codecs
f1 = codecs.open("word.txt", "r", "utf-8-sig")
text1 = f1.read()

# Open the stem file
f2= codecs.open("steme.txt", "r", "utf-8-sig")
stemw= f2.read()
words1 = stemw.split()
lstemw = list()
for word in words1:
    lstemw.append((word))

#prefix file openner
f3= codecs.open("prefix.txt", "r", "utf-8-sig")
prefixw= f3.read()
words2 = prefixw.split()
lprefixw = list()
for word in words2:
    lprefixw.append((word)) 
lprefix=tuple(lprefixw)

#postfix file openner
f4= codecs.open("postfix.txt", "r", "utf-8-sig")
postfixw= f4.read()
words3 = postfixw.split()
lpostfixw = list()
for word in words3:
    lpostfixw.append((word))  
lpostfix=tuple(lpostfixw)

#tokenizer for the document
from nltk.tokenize import  word_tokenize
tokenword=list()
tokenword=word_tokenize(text1)

# Stemming the document
finalword=list()
for i in range(len(tokenword)):
    if tokenword[i] in lstemw:
        finalword.append(tokenword[i])
    elif tokenword[i].endswith(lpostfix):
        for j in lpostfix:
            if tokenword[i].endswith(j):
                finalword.append(tokenword[i].replace(j,''))
    elif tokenword[i].startswith(lprefix):  
        for k in lprefix:
            if tokenword[i].startswith(k):
                finalword.append(tokenword[i].replace(k,'')) 
    else:
        finalword.append(tokenword[i])

# Save the result
output=""
for i in finalword:
    output+=i+" "
with open("output.txt", "w",encoding='utf-8') as f:
    f.write(output)
f.close()