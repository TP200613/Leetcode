#Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.
class Solution(object):
    def convertToTitle(self, columnNumber):
        a=""
        while columnNumber>0:
            columnNumber-=1
            a=chr(columnNumber%26+65)+a
            columnNumber//=26
        return a

