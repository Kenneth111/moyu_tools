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