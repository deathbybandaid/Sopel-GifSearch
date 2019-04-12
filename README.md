# Sopel Gif Search

Sopel Gif Search builds a convenient framework for searching for Gifs

# This code is bad, and the author doesn't feel bad
Use at your own risk. Problems are not my fault™.

# Installation
````
git clone https://github.com/deathbybandaid/Sopel-GifSearch.git
cd Sopel-GifSearch
pip3 install .
````

# Usage

````
<~deathbybandaid> .gif test
<Sopel> Gfycat Result (.gif test #44): https://thumbs.gfycat.com/SoupyIllfatedAmericanbobtail-size_restricted.gif
````

Any config filename in the gifapi folder(s) is a command.

Included are:

* tenor
* giphy
* gfycat
* gifme


In order to use a specific api, you will need to add to your sopel config a section and apikey:

````
[tenor]
apikey = asdgfsdfgjsdkfhgklsdfgklshdfgjk
````

# Personal configs

It is possible to add configs other than the included. This can be done by adding the section

````
[Sopel-GifSearch]
extra = /path/to/directory
````

# NSFW results

````
[Sopel-GifSearch]
nsfw = True
````
