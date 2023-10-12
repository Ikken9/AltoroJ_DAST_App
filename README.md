# AltoroJ_DAST_App

## Requirements

Python 3.11 <br>
Python's requests module (should be installed by default, if not you can install 
it from [here](https://pypi.org/project/requests/)) <br>
Python's json module (should be installed by default)


## Usage

`python ./main.py <args...>`

It has 3 operating modes, the first is **UI SQL Injection Test**, which is used to test the App against SQL Injection 
attacks to one of the login endpoints that is used in the frontend, the second is **API SQL Injection Test**, and it's
focused on test the same vulnerability but on the other login related endpoint, and the last is **XSS Test**, used to
test for Cross Site Scripting vulnerability on the Search bar.

### Arguments

Run it as a normal python script: ./main.py <args...> <br>
Parameters:
    
    -m, --mode <[1, 2, 3]> (required)
            [1] UI SQL Injection Test
            [2] API SQL Injection Test
            [2] XSS Test
    -p, --payload <path_to_payload_file> (required)

### Examples

    python ./main.py -m 1 -p payloads/sql_payloads.txt

    python ./main.py -m 2 -p payloads/xss_payloads.txt

### Note: 
AltoroJ must be running on TCP port 8080 (if not, you can change the code to match the port you want to use). 

## Explanation

