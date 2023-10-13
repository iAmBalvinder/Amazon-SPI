import json
import unidecode


def main_writer(f, argument):
    try:
        f.write(str(argument))
    except UnicodeEncodeError:
        f.write(unidecode.unidecode(argument))


def logger(*argv, logfile="log.txt", singleLine=False):
    """
    Writes Logs to LogFile
    """
    with open(logfile, "a+") as f:
        for arg in argv:
            if arg == "{}":
                continue
            if type(arg) == dict and len(arg) != 0:
                json_object = json.dumps(arg, indent=4, default=str)
                f.write(str(json_object))
                f.flush()

            elif type(arg) == list and len(arg) != 0:
                for each in arg:
                    main_writer(f, each)
                    f.write("\n")
                    f.flush()
            else:
                main_writer(f, arg)
                f.flush()
            if not singleLine:
                f.write("\n")
        if singleLine:
            f.write("\n")
