This code is used to run Google speech to text, an API that takes audio files and generates from them words and  their timestamps. 
To use said code, a credential file is used because Google charges for the use of this API. It is simple to generate a credential file via their interface "Google Console".
Another thing to note is that to run large audio files, they need to be uploaded on Google cloud storage, also acessible via "Google Console". The audiolist file found in this folder is to indicate all the files that the tool needs to used on. 
That list is  a mirror of what can be found on Google cloud storage.
A Youtube video explaining these steps can be found here: https://youtu.be/lKra6E_tp5U?list=PLSYwIIgrivO2L_sIWtrxO5PlhwypMhF6u

There is a slight modification at the end of the code. The goal is to save the output of speech to text as Json files, to not have to run the tool every time and only have to load the json files. That code was not run yet but could be usefull afterwards. 
