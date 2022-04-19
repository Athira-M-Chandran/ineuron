### Palindrome

1. write a formula which returns "Palindrome" or "Not Palindrome" for a given word in (palindrome.xslx)

=IF(<br>
  EXACT(<br>
    LOWER(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(B4,",",""),"'",""),".",""),"?",""),"!","")," ","")),<br>
    LOWER(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(TEXTJOIN("",1,MID(B4,ABS(ROW(INDIRECT("1:"&LEN(B4)))-(LEN(B4)+1)),1)),",",""),"'",""),".",""),"?",""),"!","")," ",""))<br>
    ),<br>
    "Palindrome","Not Pallindrome")<br>
