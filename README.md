# Text-Based-Calculator
This script evaluates a series of assignment operators provided as command-line input and prints the final values of the variables.
<br/>

<b>Operators</b><br/>
The following operators are valid:<br/>
=, *=, /=, +=, -=, +, -, *, /, ++, --<br/>
This version does not work for other operators such as (), ^, |, %, ~, etc.<br/>
<br/>

<b>Variables</b><br/>
The variables must be strictly single-character, like <i>i</i>. The script does not work for variables such as <i>count</i>.<br/>

<b>Numbers</b><br/>
The script does not work for negative numbers. All non-negative real numbers are okay.<br/><br/>

For example,<br/>
i = 0<br/>
j = ++i<br/>
x = i++ + 5<br/>
y = 5 + 3 * 10<br/>
i += y<br/>
<br/>
Result:<br/>
{i=37, j=1, x=6, y= 35}
