from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/mypage/me')
def me():
    return render_template('o_mnie.html')

@app.route('/mypage/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        print('GET received')
        return render_template('kontakt.html')
    elif request.method == 'POST':
        print('POST received')
        print(request.form['message'])
        return redirect('/mypage/me')
    
if __name__ == '__main__':
    app.run(debug=True)