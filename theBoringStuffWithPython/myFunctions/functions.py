
class list():
    def listfinder(list, findingObj):
        a = list.index(findingObj)
        return a

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

