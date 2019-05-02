#!/usr/bin/env python3

class ansicolors:
    RED = '\033[0;31m'
    ENDC = '\033[0m'

def print_calendar( month_delta = 0 ):

    import datetime
    now = datetime.datetime.now()

    then = now - datetime.timedelta( days = -month_delta * 365 / 12 )

    import calendar
    calendar.setfirstweekday( calendar.SUNDAY )
    cal = calendar.month( then.year, then.month )
    today = then.day
    if( month_delta == 0 ):
        cals = cal.split( '\n' )
        fromstr = str( then.day )
        tostr = ansicolors.RED + str( then.day ) + ansicolors.ENDC
        for n, r in enumerate( cals[ 2: ] ):
            if( str( then.day ) in r.split() ):
                cals[ n + 2 ] = r.replace( fromstr, tostr )
            cal = '\n'.join( cals )
        print( cal )
        return( cal )

import sys
print_calendar( int( sys.argv[1] ) )
