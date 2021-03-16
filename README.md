# Master Thesis

This is my app for downloading metadata of selected videos and comments

To install pytube3
    
    Go to the pytube/extract.py (in pytube library - ../site-packages/pytube/extract.py)
    Open the extract.py file and search for the line: parse_qs(formats[i]["cipher"]) for i, data in enumerate(formats)
    Replace 'cipher' with 'signatureCipher' and save it.
    
    then type 'python -m pip install git+https://github.com/nficano/pytube' to cmd

To run app:

    python3 main.py


Folders:

- archive -> contains archived scripts
- documents -> contains example outputs
- movies -> contains downloaded movies  
- output -> contains output csv files
    - movies csv "{%y%m%d_%H%M%S}\_\_movies_{length of video}\_{type of order}\_{topic}\_{type of license}\_{country}.csv"
    - comments csv "{%y%m%d_%H%M%S}\_\_comments.csv"