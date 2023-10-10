import address_book, note_book, file_sort


# avoiding next cycle execution and I/O exception after basic exit() with 'is_finished' var
def exit():
    return True


def show_help():
    command_help = {'1': "Address book of your victims",
                '2': "Notebook for special murders",
                '3': "Sort files in some folder",
                'exit': "Exit"}
    
    for key, value in command_help.items():
        print(f"'{key}': {value}")

command_list = {'1': address_book.main,
                '2': note_book.main,
                '3': file_sort.main,
                'exit': exit,
                'help': show_help}


def main():
    is_finished = False
    print("Console Bot 'Jason' is running!")

    while True:
        show_help()
        choice = input("Choose program: ")

        try:
            is_finished = command_list[choice]()
        except:
            print("Use only specified commands!")

        if is_finished:
            break


if __name__ == '__main__':
    main()