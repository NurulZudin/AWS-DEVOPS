from flask import Flask,render_template,request

app=Flask(__name__)


@app.route('/',methods=["GET"])
def index():
        return render_template('index.html')

def Convert_Roman( num):
        symbol = [ "M", "CM", "D", "CD","C", "XC", "L", "XL","X", "IX", "V", "IV","I"]
        value = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        roman_num = ''
        i = 0
        while  num > 0:
            for x in range(num // value[i]):
                roman_num += symbol[i]
            num %= value[i]
            i += 1
        return roman_num

print("###This program converts decimal numbers to Roman Numerals ###")
print('(To exit the program, please type "exit" )')


condition=True
while condition :
    try:
        Input_Text=input("Please enter a number between 1 and 3999, inclusively : ")
        Number = int(Input_Text )
        if 4000>Number>0 :
            print(Convert_Roman(Number))
        else:
            print("Not Valid Input !!!")
    except ValueError:
        if Input_Text.lower() == "exit":
            condition=False
            print("Exiting the program... Good Bye")
        else:
            print("Not Valid Input !!!")

@app.route('/total',methods=["GET","POST"])
def total():
        if request.method=="POST":
                value=request.form.get("value")
                return render_template('number.html',total=num2roman(int(value)))
        else:
                return render_template('number.html')

                
                

if __name__=='__main__':
        app.run(host='0.0.0.0',port=80)                                
