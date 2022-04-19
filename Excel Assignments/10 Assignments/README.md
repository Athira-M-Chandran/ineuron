### Sum-for-Merged-Cells

Produce the Sum for Merged Cells Headers (Sum-for-Merged-Cells.xlsx)

You need to write a single formula which can be dragged right and down to generate the sum for below table

**=SUM(OFFSET($A$1,ROWS($1:1),MATCH(B$13,$1:$1,0)-1,,IFERROR(MATCH(C$13,$1:$1,0),COUNTA($2:$2)+1)-MATCH(B$13,$1:$1,0)))**
