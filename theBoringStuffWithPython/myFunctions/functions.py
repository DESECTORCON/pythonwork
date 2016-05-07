#! /usr/bin/env python3.4

# from chapter4_lists
class list():
    def listfinder(list, findingObj):
        a = list.index(findingObj)
        return a


# from chapter7:
class stringFinder():
    def stringFinder29(string, findString, print_exe=True):
        import re, pyperclip
        if print_exe:
            print('Your runing s.e "ver2.6".')
            print('stringFinding'.center(30, '='))
            Regex = re.compile(findString)
            print('searching'.ljust(30, '-'))
            returnV = Regex.search(string)
            copyV = input('Done.(do you want to copy it?)')
            if copyV == 'yes' or copyV == 'y':
                pyperclip.copy(returnV.group())
                print('copy done!')
                print('progame off...')
        elif not print_exe:
            Regex = re.compile(findString)
            returnV = Regex.search(string)

            pyperclip.copy(returnV.group())
            return returnV.group()


# from chapter7:
# this is a strong password Detectioner. 강한 비밀번호만 골르는 펑션 이예요.
# by: choeminjun Idea by: Al Sweigart
class strongPasswordFinder():
    def finder(string):
        import re                                                # importing re Function.
        SPV = re.compile('(([a-zA-Z\d]{7})+).+', re.IGNORECASE)  # makeing inspectionObj.
        returnV = SPV.search(string)                             # searching for strongPassword.(Has alphabet and numbers and 7characters long.)
        if returnV == None or returnV == '' or returnV == []:    # if no match found, then return None.
            print('There is no strong password in this string.')
            return None
        return returnV                                           # return the strong password.


