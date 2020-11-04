# Master_Thesis

To install pytube3
    
    Go to the pytube/extract.py (in pytube library - ../site-packages/pytube/extract.py)
    Open the extract.py file and search for the line: parse_qs(formats[i]["cipher"]) for i, data in enumerate(formats)
    Replace 'cipher' with 'signatureCipher' and save it.