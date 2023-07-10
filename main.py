from flask import Flask, render_template, request

app = Flask(__name__)

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/shift")
def shift():
    return render_template("shift.html")
@app.route("/result")
def result():
    return render_template("result.html")

@app.route("/ceaser-encrypt",methods=['POST'])
def c_encrypt():
    plaintext = request.form["plaintext"].lower()
    operation = request.form["operation"]
    
    if operation == "encrypt":
        encrypted_text = ""
        for letter in plaintext:
            if letter in alphabets:
                position = alphabets.index(letter)
                new_position = position + 3
                encrypted_text += alphabets[new_position]
            else:
                encrypted_text += letter
        return render_template('result.html',result=encrypted_text)
        # return (f"The Ceaser Cipher encoded text is '{encrypted_text}'")

    elif operation == "decrypt":
        decrypted_text = ""
        for letter in plaintext:
            if letter in alphabets:
                position = alphabets.index(letter)
                new_position = position - 3
                decrypted_text += alphabets[new_position]
            else:
                decrypted_text += letter
        return render_template('result.html',result=decrypted_text)

        # return f"The Ceaser Cipher decoded text is '{decrypted_text}'"

@app.route("/shift-encrypt",methods=['POST'])
def s_encrypt():
    plaintext = request.form["plaintext"].lower()
    operation = request.form["operation"]
    shift_amount= int(request.form["shift"])
    print(shift_amount)

    if operation == "encrypt":
        encrypted_text = ""
        for letter in plaintext:
          if letter in alphabets: 
            position = alphabets.index(letter)
            new_position = position + shift_amount
            encrypted_text += alphabets[new_position]
          else:
            encrypted_text += letter
        return render_template('result.html',result=encrypted_text)
        # return (f"The Shift Cipher encoded text is '{encrypted_text}'")


    elif operation == "decrypt":
        decrypted_text = ""
        for letter in plaintext:
          if letter in alphabets:
            position = alphabets.index(letter)
            new_position = position - shift_amount
            decrypted_text += alphabets[new_position]
          else:
            decrypted_text += letter
        return render_template('result.html',result=decrypted_text)

        # return (f"The Shift Cipher decoded text is '{decrypted_text}'")

if __name__ == "__main__":
    app.run(debug=True)
