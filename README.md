# Stemming-For-Tigrigna
* **This is a simple algorithm for _Stemming Tigrigna Document_.**
> NOTE! This algorithm is not an advanced algorithm.

* `Stemming` is the process of reducing inflected (or sometimes derived) words to their word stem, base or root form generally a written word form.


* In any case when you are dealing with non-english words in read files and other cases it is good to use below code to `decode-encode` all your inputs-outputs to avoid problems:
~~~
import codecs
#open it with utf-8 encoding 
f1 = codecs.open("filename.txt", "r", "utf-8-sig")
text1 = f1.read()
~~~

# Description About Some of The files
1. [**_Stemming of  Tigrigna Document.ipynb_**](https://github.com/Luel-Hagos/Stemming-Tigrigna-Document/blob/master/Stemming%20of%20%20Tigrigna%20Document.ipynb) : which contains the algorithm.
2. [**_post1.txt_**](https://github.com/Luel-Hagos/Stemming-Tigrigna-Document/blob/master/postfix.txt) : which contains some postfixes used in Tigrinya.
3. [**_pre1.txt_**](https://github.com/Luel-Hagos/Stemming-Tigrigna-Document/blob/master/prefix.txt) : which contains some prefixes used in Tigrinya
When you run the program make sure that you are in the same directory with the files unless you specified the path of it.
~~~
