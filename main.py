#!/usr/bin/python3

import subprocess
# rodando ls


import os


subprocess.run(["yarn", "init"])
# rodando clear
# subprocess.run(["clear"])

actualPath = os.getcwd()
print(actualPath)

subprocess.__path__ = actualPath

print(subprocess.__path__ + "  :::")


def addDependeces():
    subprocess.run(["yarn", "add", "express"])
    subprocess.run(["yarn", "add", "mysql2"])
    subprocess.run(["yarn", "add", "nodemon", "-D"])
    subprocess.run(["yarn", "add", "cors"])
    subprocess.run(["yarn", "add", "jest"])
    subprocess.run(["yarn", "add", "dotenv"])
    subprocess.run(["yarn", "add", "pino"])
    subprocess.run(["yarn", "add", "pino-pretty"])


#rodando mkdir
def createDirs():
    subprocess.run(["mkdir", "src"])
    subprocess.run(["mkdir", "src/controllers"])
    subprocess.run(["mkdir", "src/database"])
    subprocess.run(["mkdir", "src/middleware"])
    
def createFiles():   
    subprocess.run(["touch", "src/routes.js"])
    subprocess.run(["touch", "src/database/database.js"])
    subprocess.run(["touch", "index.js"])
    subprocess.run(["touch", ".env"])
    subprocess.run(["touch", ".exemple.env"])
    subprocess.run(["touch", "src/logger.js"])
    subprocess.run(["touch", ".env"])
    subprocess.run(["touch", ".gitignore"])

def writeGitIgnoreFile():
    f = open(".gitignore", "a")
    f.write("node_modules\n")
    f.write(".env\n")
    f.write("*.tests.js\n")
    f.close()    

def writeEnvFile():
    f = open('.env', 'a')
    f.write("PORT=3333\n")
    f.write("\n")   
    f.write("MYSQL_USER\n")
    f.write("MYSQL_PASSWORD\n")
    f.write("MYSQL_DATABASE\n")
    f.write("MYSQL_HOST\n")
    f.write("MYSQL_PORT\n")
    f.close()

def initGit():
    subprocess.run(["git", "init"])


addDependeces()
createDirs()
createFiles()
writeGitIgnoreFile()
writeEnvFile()
initGit()