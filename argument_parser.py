import argparse

TEST_SQL_INJECTION = False
TEST_XSS = False
payload_files = None


def argument_parser():
    global TEST_SQL_INJECTION
    global TEST_XSS
    global payload_files

    parser = argparse.ArgumentParser()

    parser.add_argument("-m", "--mode",
                        help="Operating Test Mode\n" +
                             "[1] SQL Injection Test\n" +
                             "[2] XSS Test",
                        choices=[1, 2],
                        required=True)

    parser.add_argument("-p", "--payload",
                        help="Payload, needs to be a TXT file",
                        type=str,
                        default="",
                        nargs='+',
                        required=False)

    return parser.parse_args()


args = argument_parser()
if args.mode == 1:
    TEST_SQL_INJECTION = True
elif args.mode == 2:
    TEST_XSS = True

payload_files = args.payload
