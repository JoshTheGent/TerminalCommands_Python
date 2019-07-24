import sys

def createCProgram(params):
    extention = ".c"
    fileHan = open(params[1]+extention, 'w')
    if( len(params) > 2 ):
        if(params[2] == "school" and len(params) > 3):
            school = ["/*\n",
                    "*\tStudent ID: 1001296598\n",
                    "*\tName: Joshua Tran\n",
                    "*\tClass: ",
                    params[3] + "\n",
                    "*/\n\n"]
            fileHan.writelines(school)
        else:
            if(params[2] == "school"):
                school = ["/*\n",
                    "*\tStudent ID: 1001296598\n",
                    "*\tName: Joshua Tran\n",
                    "*/\n\n"]
                fileHan.writelines(school)

    includes = ["#include <stdio.h>\n",
                "#include <stdlib.h>\n",
                "#include <math.h>\n",
                "#include <string.h>\n\n"]
    fileHan.writelines(includes)

    body = ["int main()\n",
            "{\n",
            "\tprintf(\"hello world.\");\n",
            "\treturn 0;\n",
            "}\n"]
    fileHan.writelines(body)

params = sys.argv

if(len(params) > 1):
    createCProgram(params)
    print("your program has been set up with parameters:")
    print(params)
else:
    print("Not Enough Parameters.")
    quit()


    