# AltoroJ_DAST_App

## Requirements

Python 3.11 <br>
Python's requests module (should be installed by default, if not you can install 
it from [here](https://pypi.org/project/requests/)) <br>
Python's json module (should be installed by default)


## Usage

`python ./main.py <args...>`

### Arguments

Run it as a normal python script: ./main.py <args...> <br>
Parameters:
    
    -m, --mode <[1, 2, 3]> (required)
            [1] UI SQL Injection Test
            [2] XSS Test
            [2] XSS Test
    -p, --payload <path_to_payload_file> (required)

### Examples

    python ./main.py -m 1 -p payloads/sql_payloads.txt

    python ./main.py -m 2 -p payloads/xss_payloads.txt