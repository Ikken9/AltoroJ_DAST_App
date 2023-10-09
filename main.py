from argument_parser import TEST_SQL_INJECTION, TEST_XSS, payload_files
import sql_injection_tester
import xss_tester


def main():
    print("AltoroJ Simple DAST Application")

    host = "localhost:8080"

    sql_injection_target_url = host + "/AltoroJ/login"  # replace with valid url
    xss_target_url = host + ""  # replace too

    if TEST_SQL_INJECTION:
        print("[*] Starting SQL Injection Test...\n")
        result = sql_injection_tester.test(sql_injection_target_url, payload=parse_sql_injection_payload()) # MEPA TA INVIERTIDO
        print(f"[*] Test finished, exit code {result}")
        if result == 0:
            print("[*] SQL Injection Vulnerability is not present")
        elif result == 1:
            print("[*] SQL Injection Vulnerability is present")

    elif TEST_XSS:
        print("[*] Starting XSS Test...\n")
        result = xss_tester.test(xss_target_url, payload=parse_xss_payload())
        print(f"[*] Test finished, exit code {result}")
        if result == 0:
            print("[*] XSS Vulnerability is not present")
        elif result == 1:
            print("[*] XSS Vulnerability is present")


def parse_sql_injection_payload():
    payload_list = []
    for file in payload_files:
        with open(file) as sql_payload:
            for line in sql_payload:
                payload_list.append(line)

    return payload_list


def parse_xss_payload():
    return 0  # to be done


if __name__ == '__main__':
    main()
