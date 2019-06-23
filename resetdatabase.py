# REMOVES CURRENT MIGRATIONS AND DATABASE FILES
# ONLY FOR DEVELOPMENT USE!
# THIS FILE SHOULD BE INCLUDED IN .gitigmore AS IT IS DANGEROUS TO HAVE STORED WITHIN A PRODUCTION ENVIRONMENT!
import os
import sys
import shutil
import subprocess

SRC_PATH = os.path.join(os.getcwd(), 'src')

def reset_migrations():
    print('REMOVING MIGRATIONS...')
    for contents in os.listdir(SRC_PATH):         # for each file/folder in search path
        dir_path = os.path.join(SRC_PATH, contents)
        if os.path.isdir(dir_path):               # if item is a directory
            migrations_dir = os.path.join(dir_path, 'migrations')
            if os.path.isdir(migrations_dir):     # if folder contains a folder named 'migrations'
                for each in os.listdir(migrations_dir):
                    if each != '__init__.py':
                        target = os.path.join(migrations_dir, each)
                        if os.path.isfile(target):
                            os.remove(target)     # remove file
                        elif os.path.isdir(target):
                            shutil.rmtree(target) # remove directory
                        else:                     # should never reach this case
                            print(f'\tUNEXPECTED ERROR AT {target}')
                            pass

def reset_database():
    print('REMOVING CURRENT DATABASE FILE...')
    try:
        os.remove(os.path.join(SRC_PATH, 'db.sqlite3'))
    except:
        pass

def make_new_migrations():
    print('CREATING NEW MIGRATIONS...')
    _make_migrations = 'python src/manage.py makemigrations'
    _migrate = 'python src/manage.py makemigrations'
    os.popen(_make_migrations).read() # This will run the command and return any output
    os.popen(_migrate).read() # This will run the command and return any output

if __name__ == "__main__":
    reset_migrations()
    reset_database()
    if len(sys.argv) is 2 and sys.argv[1] == 'migrate':
        try:
            make_new_migrations()
        except:
            print('ERROR WHILE CREATING NEW MIGRATIONS. TRY RUNNING COMMANDS MANUALLY.')
            print('python manage.py makemigrations')
            print('python manage.py migrate')
    print('SUCCESSFULLY RESET CURRENT DATABASE CONFIGURATION. BE SURE TO CREATE A NEW SUPERUSER IN ORDER TO LOGIN AS ADMIN.')
