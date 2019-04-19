import sys, getopt, time
import tushare as ts
import curses

def initCurses():
    stdscr = curses.initscr()
    stdscr.clear()
    stdscr.refresh()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)
    return stdscr

def mPrint(stdscr, x, y, mStr, isComment):
    try:
        if isComment:
            stdscr.attron(curses.color_pair(4))    
            stdscr.addstr(y, x, "// " + mStr)
            stdscr.attroff(curses.color_pair(4))        
        else:
            stdscr.addstr(y, x, mStr)    
    except Exception as identifier:
        return

def strHeader(mList, width):
    mStr = ""
    for header in mList:
        mStr += header.center(width)
    return mStr

def main(argv):
    inputfile = ''
    sourcefile = 'stock.py'
    isShowIndex = False
    # time (seconds): cou * 10
    cou = 6
    # width
    W = 10    
    try:
        opts, args = getopt.getopt(argv,"hf:is:t:",["file="])
    except getopt.GetoptError:
        print ('stock.py -i <stocklist>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('stock.py -f <stocklist> -i -s <sourcefile> -t <time (mins)>')
            sys.exit()
        elif opt in ("-f", "--file"):
            inputfile = arg   
        elif opt == "-i":
            isShowIndex = True
        elif opt == "-s":
            sourcefile = arg
        elif opt == "-t":
            cou = int(arg) * 6
    if inputfile == '':
        print("A stock list file is required: stock.py -i <inputfile>\n")
        exit(-1)
    # read stock codes
    stock_codes = []
    with open(inputfile, "r") as f:
        for code in f.readlines():
            stock_codes.append(code.strip())
    stdscr = initCurses()
    # display codes
    with open(sourcefile, "r") as f:
        for linenum, line in enumerate(f.readlines()):
            y = linenum * 2 + 1
            x = 0
            mPrint(stdscr, x, y, line.strip(), False)
    # display the header
    headerList = ['code','name', 'pre_close', 'price','high','low','volume','amount','time']
    headers = strHeader(headerList, W)
    mPrint(stdscr, 0, 0, headers, True)
    while cou > 0:
        # display real-time stock price
        df = ts.get_realtime_quotes(stock_codes)
        l = len(stock_codes)
        for i in range(l):
            content = ''
            y = (i + 1) * 2
            x = 0
            for value in headerList:
                content += df.loc[i, value].center(W)
            mPrint(stdscr, x, y, content, True)
        # display real-time index
        if isShowIndex:
            df = ts.get_index()
            index_code = ['000001', '399106']
            indexHeaderList = ["code", "name", "preclose", "change", "open", "close", 'high','low', 'amount']
            headers = strHeader(indexHeaderList, W)
            mPrint(stdscr, 0, (l + 1) * 2, headers, True)            
            for i, code in enumerate(index_code):
                tmp_df = df[df["code"] == code]
                x = 0
                y = (l + i + 2) * 2
                content = ""
                index = tmp_df.index[0]
                for value in indexHeaderList:
                    if isinstance(tmp_df.loc[index, value], str):
                        content += tmp_df.loc[index, value].center(W)
                    else:
                        if value in ["preclose", "open", "close", "high", "low"]:
                            tmp_str = "{0: 4.3f}".format(tmp_df.loc[index, value]).center(W)
                            content += tmp_str
                        else:
                            content += tmp_df.loc[index, value].astype("str").center(W)
                mPrint(stdscr, x, y, content, True)
        stdscr.refresh()
        time.sleep(10)
        cou -= 1

if __name__ == "__main__":
    main(sys.argv[1:])