<link rel='stylesheet' href='readme.css'>

# Syntax Highlighter

The program receives a text file containing code in C++, Python or JavaScript and outputs an HTML file containing the same code and highlighting elements from lexical categories that are shared between the three languages.

## How to highlight code

From the folder where all files are stored, run shell script with path to code file as an argument:

    ./run.sh path/to/file.py

In computers that cannot run shell scripts the code can be manually compiled and run:

    gcc scanner.c lex.yy.c -o scanner
    ./scanner < path/to/file.cpp

The highlighted code will be stored in ```output.html```, using the stylesheet ```style.css``` contained in this folder.

## Important notes

- An exception is yet to be implemented so that C++ and JavaScript comments be told apart from Python integer divisions ("//").

- Another exception is yet to be implemented so that Python comments be highlighted if there is no space between "#" and the text. C++ "#" statements should be taken into consideration.

## Sample output

<div id="sample">
<span class='keyword'>keyword</span><br/>
<span class='type'>type</span><br/>
<span class='compare_operator'>compare_operator</span><br/>
<span class='assignment_operator'>assignment_operator</span><br/>
<span class='logical_operator'>logical_operator</span><br/>
<span class='mathematical_operator'>mathematical_operator</span><br/>
<span class='semicolon'>semicolon</span><br/>
<span class='comment'>comment</span><br/>
<span class='bracket'>bracket</span><br/>
<span class='boolean'>boolean</span><br/>
<span class='double_quotes'>double_quotes</span><br/>
<span class='single_quotes'>single_quotes</span><br/>
<span class='number'>number</span><br/>
<br/>
CODE:<br/>
<div id='code'><br/>
#<span class='keyword'>include</span> <span class='compare_operator'><</span>io<span class='type'>str</span>eam<span class='compare_operator'>></span><br/>
<span class='keyword'>using</span> <span class='keyword'>namespace</span> <span class='keyword'>std</span><span class='semicolon'>;</span><br/>
<span class='type'>int</span> <span class='keyword'>main</span><span class='bracket'>(</span><span class='bracket'>)</span><br/>
<span class='bracket'>{</span><br/>
    cout <span class='compare_operator'><</span><span class='compare_operator'><</span> <span class='single_quotes'>'</span>Text<span class='single_quotes'>'</span> <span class='compare_operator'><</span><span class='compare_operator'><</span> endl<span class='semicolon'>;</span><br/>
    <span class='keyword'>return</span> <span class='number'>0</span><span class='semicolon'>;</span>   <span class='comment'>// comment</span><br/>
<span class='bracket'>}</span><br/>
<br/>
<span class='keyword'>from</span> r<span class='logical_operator'>and</span>om <span class='keyword'>import</span> r<span class='logical_operator'>and</span><span class='type'>int</span> <span class='keyword'>as</span> r<br/>
<span class='keyword'>def</span> rn<span class='bracket'>(</span><span class='bracket'>)</span> <span class='mathematical_operator'>-</span><span class='compare_operator'>></span> <span class='type'>str</span>:<br/>
    n <span class='assignment_operator'>=</span> <span class='bracket'>[</span><span class='double_quotes'>"</span>a<span class='double_quotes'>"</span>, <span class='double_quotes'>"</span>b<span class='double_quotes'>"</span>, <span class='double_quotes'>"</span>c<span class='double_quotes'>"</span>, <span class='double_quotes'>"</span>d<span class='double_quotes'>"</span>, <span class='double_quotes'>"</span>e<span class='double_quotes'>"</span>, <span class='double_quotes'>"</span>f<span class='double_quotes'>"</span>, <span class='double_quotes'>"</span>g<span class='double_quotes'>"</span><span class='bracket'>]</span><br/>
    <span class='keyword'>return</span><span class='bracket'>(</span><span class='keyword'>let</span>ters<span class='bracket'>[</span>r<span class='bracket'>(</span><span class='number'>7</span><span class='bracket'>)</span><span class='bracket'>]</span><span class='bracket'>)</span><br/>
<span class='keyword'>print</span><span class='bracket'>(</span>rn<span class='bracket'>(</span><span class='bracket'>)</span><span class='bracket'>)</span>   <span class='comment'># comment</span><br/>
<br/>
</div>
</div>

## Sources consulted

[https://youtu.be/54bo1qaHAfk](https://youtu.be/54bo1qaHAfk)