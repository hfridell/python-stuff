import requests
from hashlib import sha256

# short gist of text
test_url = 'https://gist.githubusercontent.com/hfridell/4d72354ba031f76c27d2f579c1b3751a/raw/d64b3bd41e3f30d227f10444add539473a25a733/test.txt'

def get_web_file(url):
    try:
        request = requests.get(url)
        request.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
        exit(1)

    return request.text

def write_file(content, filename='output.txt'):
    with open(filename,'w') as f:
        f.write(content)

def create_checksum(filename, file_output=True):
    with open(filename, 'rb') as input:
        checksum = sha256(input.read()).hexdigest()

    if file_output:
        output_file = filename + '.sha256'
        with open(output_file,'w') as f:
            f.write(checksum)

    return checksum

if __name__ == '__main__':
    content = get_web_file(test_url)
    output = 'target_file.txt'
    
    write_file(content, output)
    checksum = create_checksum(output)

    print('Requested: ', test_url)
    print('Output File: ', output)
    print('Checksum: ', checksum)