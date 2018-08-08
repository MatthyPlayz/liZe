# -*- coding: utf-8 -*—

version = "0.0.1" # DO NOT CHANGE UNLESS MODS ADDED, THEN ADD (MODDED) TO END
version_rounded = "0 (first version)"

# functions
def __ABOUT__():
    print("liZe console version %s" % (version))

def __ABOUT_VERSION__():
    print(version)
def mathadd():
    vala = int(raw_input("VAL1 "))
    valb = int(raw_input("VAL2 "))
    print(vala + valb)
# input
def do_ask():
    do_ask.inputa = raw_input("DO: ")

print("liZe console %s" % (version))
do_ask()
inputa = do_ask.inputa

if(do_ask.inputa == "about<arg1<version>>"):
    __ABOUT_VERSION__()
    do_ask()

if(do_ask.inputa == "math<add<>>"):
    mathadd()
    do_ask()
    inputa = do_ask.inputa
    
if("print<" and ">" in do_ask.inputa):
    a = str(inputa.rsplit("print<"))
    b = a.rsplit(">")
    c = b[0]
    d = c.strip("[]")
    e = d[5:len(d)]
    print(e)
    do_ask()
    inputa = do_ask.inputa
if(do_ask.inputa == "about<>"):
    __ABOUT__()
    do_ask()
    inputa = do_ask.inputa

if(do_ask.inputa == "about<arg1<version>>"):
    __ABOUT_VERSION__()
    do_ask()
    inputa = do_ask.inputa

if(do_ask.inputa == "about<arg1<version>arg2<rounded>>"):
    print(version_rounded)
    do_ask()
    inputa = do_ask.inputa

if(do_ask.inputa == "stext<error<texterror>>"):
        raise NameError("<TextError> was defined by %user%. ERROR information: \n  @eU1 => Typing error. Most likely variable or function name was misspelled or defined in a faulty way.")
        print("\n" * 5)
        print("SIMPLIFIED:\n Typing error. Most likely variable or function name was misspelled or defined in a faulty way")
