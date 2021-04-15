from flask import Flask,render_template,request

app=Flask(__name__)


@app.route('/',methods=["GET"])
def index():
        return render_template('index.html')

num_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

def num2roman(num):

    roman = ''

    while num > 0:
        for i, r in num_map:
            while num >= i:
                roman += r
                num -= i

    return roman        

@app.route('/total',methods=["GET","POST"])
def total():
        if request.method=="POST":
                value=request.form.get("value")
                return render_template('number.html',total=num2roman(int(value)))
        else:
                return render_template('number.html')

                
                

if __name__=='__main__':
        app.run(host='0.0.0.0',port=80)                                