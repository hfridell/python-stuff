# rest_call.py
## Setup
rest_call.py imports from requests and hashlib they are included in `requirements.txt`

## Function
* Makes a GET request to the raw link for [github gist](https://gist.github.com/hfridell/4d72354ba031f76c27d2f579c1b3751a) containing 3 lines of text separated by blank lines. The SHA256 is `FA3CA8CF4AE9D4EF4D5FC6DDAAE9357C23D52E15FBBD84AF1FD38AA43F9DF809`. These are put in output files. Information about the request is also printed.

File content:
```
Test File

12345

\n
```

## Result
* Creates the output file `target_file.txt` 
* checksum of output file is stored in `target_file.txt.sha256`
* prints details about the request, file name, and checksum

## Next steps
* add command line arguments to allow passing in parameters for the url and output files