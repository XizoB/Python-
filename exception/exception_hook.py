#-*-coding:utf-8-*-

import linecache
import pprint
import sys

def mytraceback_output(typ, value, tb):
    startstr = "\n>>>>>>>>>> TRACEBACK >>>>>>>>>>"
    stackstr = ["\nTraceback:"]
    localstr = ["\nLocals:"]

    try:
        while tb:
            f = tb.tb_frame
            c = f.f_code
            linecache.checkcache(c.co_filename)
            line = linecache.getline(c.co_filename, f.f_lineno, f.f_globals)
            stackstr.append('File "%s", in %s' % (c.co_filename, c.co_name))
            stackstr.append(" > %d: %s" % (f.f_lineno, line.strip() if line else None))
            for l in pprint.pformat(f.f_locals, width=70).split('\n'):
                localstr.append("\t%s" % l)
            
            tb = tb.tb_next
    except Exception as e:
        stackstr.append(str(e))

    
    stackstr.append("%s: %s" % (type.__name__, value))
    
    stackstr = '\n'.join(stackstr)
    localstr = '\n'.join(localstr)

    endstr = '\n<<<<<<<<<<<<< END <<<<<<<<<<<<<\n'

    outstr = ''.join([startstr,stackstr,localstr, endstr])
    print(outstr)

def foo():
    a = 100 /0
    return a

def main():
    sys.excepthook = mytraceback_output
    foo()


if __name__ == '__main__':
    main()



