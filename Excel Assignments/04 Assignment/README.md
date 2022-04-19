### Find-the-Position-of-Word

1. Find the Position of Word (Find-the-Position-of-Word.xlsx)

Suppose you have been given a word say "and" and you need to find which word position is this

1. In Mr. and Mrs. Smith - Position of "and" is 2 as this is the 2nd word, the position is not 5. <br>
2. In Samarand Smith and Kittie Smith - the position is 3 not 2 as "and" is appearing in the first word also but not as a single word.<br>
3. You need to write a formula which finds the word position for the word "and"<br>

**=SEARCH(B2,A2)-LEN(SUBSTITUTE(LEFT(A2,SEARCH(B2,A2))," ",""))+1**
