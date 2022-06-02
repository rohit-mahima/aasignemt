from flask import Flask, render_template, request
import os

app=Flask(__name__)

@app.route('/login', methods=['GET'])
def content():
    file=request.args.get('filename')
    start_line=int(request.args.get('start_line'))
    end_line=int(request.args.get('end_line'))

    with open(''.join(file),'r') as f:
        content=f.read()
        l=content.split("\n")   
        
    return render_template('content.html',l=l,start_line=start_line,end_line=end_line)

if __name__=='__main__':
    app.run(port=8000,debug=True)