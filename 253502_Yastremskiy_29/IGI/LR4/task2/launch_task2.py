from task2.text_processing import TextHandler

def start_task2() -> None:
    test = TextHandler("task2_text.txt")
    test.print_all_info_console()
    test.print_info_file()
    print('\n')
    test.print_info_about_archive()
    print('\n')
    print("Enter example of IP for checking:")
    ip = input()
    if TextHandler.check_correct_ip_address(ip):
        print(f"IP-address entered correctly: {ip}")
    else: print(f"IP-address is invalid: {ip}")
