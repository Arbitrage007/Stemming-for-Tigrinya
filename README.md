# Stemming Algorithm for Tigrinya Language
* `Stemming` is the process of reducing inflected (or sometimes derived) words to their word stem, base or root form generally a written word form.


* In any case when you are dealing with non-english words in read files and other cases it is good to use below code to `decode-encode` all your inputs-outputs to avoid problems:
~~~
import codecs
#open it with utf-8 encoding 
f1 = codecs.open("filename.txt", "r", "utf-8-sig")
text1 = f1.read()
~~~
