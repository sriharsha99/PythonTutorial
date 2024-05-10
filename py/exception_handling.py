def else_case():
    try:
        # result = 10 + '10'
        result = 10 + 10
    except:
        print ("hey it looks like you aren't added correctly")
    else:
        print ("Add went well")
        print (result)


def finally_case():
    try:
        f = open('adb.txt', 'r')
        f.write("write a test line")
    except TypeError:
        print ("There was a type error")
    except OSError:
        print ("Hey you have a OS error")
    finally:
        print ("i always run")

def ask_for_int():
    while True:
        try:
            result = int(input("please provide integer"))
        except:
            print ("whoops! this is not integer")
            continue
        else:
            print ("Thanks for providing integer")
            break
        finally:
            print ("end of try/except/final")
            print ("i will always run at the end")

# else_case()
# finally_case()
ask_for_int()