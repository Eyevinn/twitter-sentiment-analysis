#test module . Generate html table for overview of probabilities. 
def insert_top(file):
    file.write("<html>")
    file.write("<head>")
    
    
    file.write("<link rel='stylesheet' type='text/css' href='style.css'>")
    
    
    file.write("</head>")
    file.write("<body>")
    file.write("<?php exec('python main.py');?>")

def insert_bottom(file):
    file.write("</body>")
    file.write("</head>")
    file.write("</html>")


def test(file,model):
    
    
    data = model["a"]
    data_2 = model["s"]
    file.write("<table id='table1'>")
    file.write("<tr><th id = 'aheader'>Class A  </th></tr>")
    for i in data:
        
        file.write("<tr><th>"+i+"</th> <td>"+str(data[i])+"</td></tr>")

    file.write("</table>")

    file.write("<table id='table2'>")
    file.write("<tr><th id = 'sheader'>Class S </th></tr>")
    for i in data_2:
    
        file.write("<tr><th>"+i+"</th> <td>"+str(data_2[i])+"</td></tr>")
    file.write("</table>")