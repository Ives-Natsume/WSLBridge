import re

def winPath_user_input(user_input):
    loop_flag = True
    while loop_flag == True:
        #print("Paste your taget path here.")

        #winPath = input()


        print("Windows target path set as", user_input)
        print("Confirm? Press enter to continue, or any other key to reset.")


        user_choice = input()

        if user_choice == "":
            loop_flag = False

    return user_input



def linuxPath_handler(windows_path):
    unix_path = windows_path.replace('\\\\', '/')

    # match disk drive number
    drive_match = re.match('^([A-Za-z]):', unix_path)
    

    if drive_match:
        drive_letter_raw = drive_match.group(1)
        drive_letter = drive_match.group(1).lower()
        mount_point = f"/mnt/{drive_letter}"
        unix_path = unix_path.replace(f"{drive_letter_raw}:", mount_point, 1)
    else:
        print("No disk drive number found.")

    return unix_path


def cp_win_to_linux(winFilePath, linuxTargetPath):
    winFilePath = repr(winFilePath).strip("'")
    winFilePath_linuxStyle = linuxPath_handler(winFilePath)

    cp_command = "cp " + winFilePath_linuxStyle + " " + linuxTargetPath
    return cp_command


def cp_linux_to_win(linuxFilePath, winTargetPath):
    winTargetPath = repr(winTargetPath).strip("'")
    winTargetPath_linuxStyle = linuxPath_handler(winTargetPath)

    cp_command = "cp " + linuxFilePath + " " + winTargetPath_linuxStyle
    return cp_command


def mv_win_to_linux(winFilePath, linuxTargetPath):
    winFilePath = repr(winFilePath).strip("'")
    winFilePath_linuxStyle = linuxPath_handler(winFilePath)

    mv_command = "mv " + winFilePath_linuxStyle + " " + linuxTargetPath
    return mv_command


def mv_linux_to_win(linuxFilePath, winTargetPath):
    winTargetPath = repr(winTargetPath).strip("'")
    winTargetPath_linuxStyle = linuxPath_handler(winTargetPath)

    mv_command = "mv " + linuxFilePath + " " + winTargetPath_linuxStyle
    return mv_command


def winPath_to_linuxPath(windows_path):
    windows_path = repr(windows_path).strip("'")
    winPath_linuxStyle = linuxPath_handler(windows_path)
    return winPath_linuxStyle
