import os

# Fill out your github info here
email = 'yourname@users.noreply.github.com'
username = 'yourname'

class Text:

    intro = '''
    Create a blank repo on github.com. Name the folder on your local drive
    the exact same name as the repo you created on github. Run this script 
    in the same directory level as your other repo folders.

    Pick the folder you'd like to push to by picking the number on the left
    '''

class GitTool:


    def __init__(self):
        self.git_list = []
        self.git_dict = {}

    def push(self, folder):
        os.chdir(folder)
        os.system('git init')
        os.system('git config user.email ' + email)
        os.system('git config user.name ' + username)
        # os.system('git pull')
        os.system('git add .')
        os.system('git commit -m "first commit"')
        os.system('git remote add origin git@github.com:' + username + '/' + folder + '.git')
        os.system('git push -u origin master')

    def get_folders(self):
        a = os.listdir()
        for x in a:
            if os.path.isdir(x):
                self.git_list.append(x)

        for num, val in enumerate(self.git_list):
            print('{}---{}'.format(num, val))
            self.git_dict[num] = val

    def main(self):
        self.get_folders()
        folder_input = input(Text.intro)
        if folder_input:
            self.push(self.git_dict[int(folder_input)])


if __name__ == '__main__':
    tool =  GitTool()
    tool.main()
