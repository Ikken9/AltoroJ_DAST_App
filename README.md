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
            [2] XSS Test
            [3] API SQL Injection Test
    -p, --payload <path_to_payload_file> (required)

### Examples

``` Bash
python ./main.py -m 1 -p payloads/sql_payloads.txt

python ./main.py -m 2 -p payloads/xss_payloads.txt

python ./main.py -m 3 -p payloads/sql_payloads.txt
```

### Note: 
AltoroJ must be running on TCP port 8080 (if not, you can change the code to match the port you want to use). 

## Explanation

To translate the parameters entered by the user when executing the script, the `argument_parser` method is used, which handles the different accepted and required parameters with their respective values, indicating which test to execute and with which **data/payload**.

The `main` method is the one that defines the host to be tested, and at the same time it is the one that executes the test itself. It loads the information of the files that contain the input for the tests (through the `parse_payload` method) and logs the process and result of each one of them, returning the `exit code` corresponding to the result of the executed test.

### SQL injection test

#### Test the API

The `test_api` method is in charge, for each data in the indicated payload file, of sending to the server the corresponding request or requests, indicating all the required data (headers, body, etc) in the requested format, for each one of them. If the server responds with a positive `status code (200)` the method will **return 1**, indicating that it is possible to enter the system. If none of the requests made has such a response code, the method will **return 0**.

#### Test the UI
	
This test works in a very similar way to the **API test**, for each data in the indicated payload file the URL is constructed with the required data and an expected response is defined, `expected_response`, which would indicate that with the indicated data it is not possible to enter the system. 

When the response is obtained from the server (which is an HTML) it is searched if there is any sequence of characters as expected (`expected_response`). If so, it means that the system behaved as it should, therefore it returns the value of 0. If not, it means that the system did not do what it was supposed to do and it returns the value of 1.

### Cross Site Scripting Test 

The XSS test, defined in the `test_xss` method works in such a way that for each piece of data in the corresponding payload file, the corresponding request is generated, and once the response is obtained from the server, it is ensured that the exact script/data sent is not found in the response. If it is found, it means that the server failed to regulate the data, so the test returns the **value of 1**. Otherwise, it returns the **value of 0**.