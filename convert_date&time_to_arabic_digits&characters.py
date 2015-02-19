# -*- coding: utf-8 -*-
'''
convert_date&time to arabic digits&characters
Author: Askao
'''
import HTMLParser, datetime

number_list = [
     "&#1632;","&#1633;","&#1634;","&#1635;","&#1636;",
     "&#1637;","&#1638;","&#1639;","&#1640;","&#1641;"
];
month_list = [
     "يناير","فبراير","مارس","ابريل","مايو","يونيو","يوليو",
     "أغسطس","سبتمبر","أكتوبر","نوفمبر","ديسمبر"
];
    
h = HTMLParser.HTMLParser()
# convert each digit in the current day to arabic digits
arabic_day = ""
for n in str(datetime.datetime.now().day):
    arabic_day += h.unescape(number_list[int(n)])
# convert current month to arabic month
arabic_month = month_list[datetime.datetime.now().month-1]
# convert each digit in the current year to arabic digits
arabic_year = ""
for n in str(datetime.datetime.now().year):
    arabic_year += h.unescape(number_list[int(n)])
# convert each digit in the current hour to arabic digits
arabic_hour = ""
for n in str(datetime.datetime.now().hour):
    arabic_hour += h.unescape(number_list[int(n)])
# convert each digit in the current minute to arabic digits
arabic_minute = ""
for n in str(datetime.datetime.now().minute):
    arabic_minute += h.unescape(number_list[int(n)])

print "current date in arabic: " + arabic_day + " " + unicode(arabic_month, 'utf8') + ", " + arabic_year
print "current time in arabic: " + arabic_hour + ":" + arabic_minute
