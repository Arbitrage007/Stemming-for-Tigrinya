# Stemming-Tigrigna-Document
* **This is simple algorithm for _Stemming Tigrigna Document_.**
> NOTE! This algorithm is not advanced algorithm.

* `Stemming` is the process of reducing inflected (or sometimes derived) words to their word stem, base or root form generally a written word form.

# Installing NLTK in Windows
* This is with the assumption that, you have python installed. If you don't have. So, first step is to install python from [https://www.python.org/downloads/](https://www.python.org/downloads/) and follow the steps.

* Open terminal and the enter below command (Python 3).
~~~
pip install nltk
~~~

* Installation should be done successfully.
* You can verify whether the installation is accurate supplying the below command.
~~~
import nltk
~~~

* If you see `no error`, Installation is complete.

# Installing NLTK through Anaconda
* If you don't have anaconda install it (which can also be used to install different packages) by visiting [https://www.anaconda.com/download/](https://www.anaconda.com/distribution/) and select which version of python you need to install for anaconda.
* **_Note:_** you can refer to this tutorial for detailed steps to [install anaconda](https://www.guru99.com/download-install-r-rstudio.html).

* Open Anaconda Prompt and enter the below command.
~~~
conda install nltk
~~~
* Review the package upgrade, downgrade, install information and enter yes.
* NLTK is downloaded and installed.

# NLTK Dataset
NLTK module has many datasets available that you need to download to use. More technically it is called **corpus**.

# How to Download all packages of NLTK
* Run the Python interpreter in Windows and enter the below commands.
~~~
import nltk
nltk.download ()
~~~

* NLTK Downloaded Window Opens. Click the Download Button to download the dataset. This process will take time, based on your internet connection.
* **_NOTE:_** You can change the download location by Clicking File> Change Download Directory.
* To test the installed data use the following code.
~~~
from nltk.corpus import brown
brown.words()
~~~

* Then if you get the following output it is installed successfully.
~~~
['The', 'Fulton', 'County', 'Grand', 'Jury', 'said', ...]
~~~

* In any case when you are dealing with non-english words in read files and other cases it is good to use below code to `decode-encode` all your inputs-outputs to avoid problems:
~~~
#document openner
import codecs
#open it with utf-8 encoding 
f1 = codecs.open("filename.txt", "r", "utf-8-sig")
text1 = f1.read()
~~~

# Description About The files
* **_This repostary contains the following:_**
1. [**_Stemming of  Tigrigna Document.ipynb_**](https://github.com/Luel-Hagos/Stemming-Tigrigna-Document/blob/master/Stemming%20of%20%20Tigrigna%20Document.ipynb) : which contains the algorithm.
2. [**_postfix.txt_**](https://github.com/Luel-Hagos/Stemming-Tigrigna-Document/blob/master/postfix.txt) : which contains some postfixes used in tigrigna.
3. [**_prefix.txt_**](https://github.com/Luel-Hagos/Stemming-Tigrigna-Document/blob/master/prefix.txt) : which contains some prefixes used in tigrigna.
4. [**_steme.txt_**](https://github.com/Luel-Hagos/Stemming-Tigrigna-Document/blob/master/steme.txt) : which contains some stemm words used in tigrigna.
5. [**_word.txt_**](https://github.com/Luel-Hagos/Stemming-Tigrigna-Document/blob/master/word.txt) : which contains the document to be stemmed.
6. [**_output.txt_** ](https://github.com/Luel-Hagos/Stemming-Tigrigna-Document/blob/master/output.txt) : which contains the final output.
~~~
When you run the program make sure that you are in the same diroctary with ETL_SAMPLE_DICT.zip , unless you specified the path of it.
~~~
