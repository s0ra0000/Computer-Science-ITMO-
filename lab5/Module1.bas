Attribute VB_Name = "Module1"
Sub Macro_1()
Dim rg As Range
Dim cond1 As FormatCondition, cond2 As FormatCondition
Set rg = Range("G4:Y7")

'clear any existing conditional formatting
rg.FormatConditions.Delete

'define the rule for each conditional format
Set cond1 = rg.FormatConditions.Add(xlTextString, TextOperator:=xlContains, String:="=0")
Set cond2 = rg.FormatConditions.Add(xlTextString, TextOperator:=xlContains, String:="=1")

'define the format applied for each conditional format
With cond1
.Interior.Color = RGB(112, 173, 71)
.Font.Color = vbWhite
End With

With cond2
.Interior.Color = RGB(68, 114, 196)
.Font.Color = vbWhite
End With

End Sub
