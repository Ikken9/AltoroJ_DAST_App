from argument_parser import TEST_UI_SQL_INJECTION, TEST_SQL_API_INJECTION, TEST_XSS, payload_files
import sql_injection_tester
import xss_tester


def main():
    print("AltoroJ Simple DAST Application")

    host = "http://localhost:8080"

    sql_api_injection_target_url = host + "/AltoroJ/api/login"
    sql_ui_injection_target_url = host + "/AltoroJ/doLogin"
    xss_target_url = host + "/AltoroJ/search.jsp"

    if TEST_UI_SQL_INJECTION:
        print("[*] Starting SQL UI Injection Test...\n")
        result = sql_injection_tester.test_ui(sql_ui_injection_target_url, payload=parse_payload())
        print(f"[*] Test finished, exit code {result}")
        if result == 0:
            print("[*] SQL UI Injection Vulnerability is not present")
        elif result == 1:
            print("[*] SQL UI Injection Vulnerability is present")

    elif TEST_XSS:
        print("[*] Starting XSS Test...\n")
        result = xss_tester.test(xss_target_url, payload=parse_payload())
        print(f"[*] Test finished, exit code {result}")
        if result == 0:
            print("[*] XSS Vulnerability is not present")
        elif result == 1:
            print("[*] XSS Vulnerability is present")

    elif TEST_SQL_API_INJECTION:
        print("[*] Starting SQL API Injection Test...\n")
        result = sql_injection_tester.test_api(sql_api_injection_target_url, payload=parse_payload())
        print(f"[*] Test finished, exit code {result}")
        if result == 0:
            print("[*] SQL API Injection Vulnerability is not present")
        elif result == 1:
            print("[*] SQL API Injection Vulnerability is present")


def parse_payload():
    payload_list = []
    for file in payload_files:
        with open(file) as payload:
            for line in payload:
                payload_list.append(line)

    return payload_list


if __name__ == '__main__':
    main()
