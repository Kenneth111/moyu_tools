import sys, getopt, time
import requests
import bs4
from commons.curses_functions import initCurses, mPrint

def main(argv):
    sourcefile = "news.py"
    t = 6
    n = 5
    try:
        opts, args = getopt.getopt(argv,"s:n:")
    except getopt.GetoptError:
        print ('news.py -s <sourcefile> -t <time (mins)> -n <the number of news displayed>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('stock.py -s <sourcefile> -t <time (mins)> -n <the number of news displayed>')
            sys.exit()
        elif opt == "-s":
            sourcefile = arg
        elif opt == "-t":
            t = int(arg) * 6    
        elif opt == "-n":
            n = int(arg)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }
    url = 'http://www.chinanews.com/importnews.html'
    r = requests.get(url, headers=headers)
    content = bs4.BeautifulSoup(r.content.decode("utf-8", "ignore"), "lxml")
    elements = content.find_all(class_="dd_bt")
    cou = n
    titles_links = []
    for element in elements:
        if len(element.a.contents) > 0 and len(element.a.contents[0].strip()) > 0:
            titles_links.append("".join([" " + a for a in element.a.contents[0]]) + "    " + element.a["href"])
            cou -= 1
            if cou < 0:
                break
        stdscr = initCurses()
    # display codes
    with open(sourcefile, "r") as f:
        for linenum, line in enumerate(f.readlines()):
            y = linenum * 2 + 1
            x = 0
            mPrint(stdscr, x, y, line.strip(), False)
    for i in range(n):
        x = 0
        y = i * 2
        mPrint(stdscr, x, y, titles_links[i], True)
    stdscr.refresh()
    time.sleep(t * 10)

if __name__ == "__main__":
    main(sys.argv[1:])
    