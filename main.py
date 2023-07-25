from flask import Flask, render_template, request

app = Flask(__name__)

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# alphabets = ['    a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/shift")
def shift():
    return render_template("shift.html")
@app.route("/result")
def result():
    return render_template("result.html")

@app.route("/ceaser-encrypt", methods=['POST'])
def c_encrypt():
    plaintext = request.form["plaintext"].lower()
    operation = request.form["operation"]

    if operation == "encrypt":
        shift = 3  # Set the shift value to 3 for encryption
        encrypted_text = ""
        for letter in plaintext:
            if letter in alphabets:
                position = alphabets.index(letter)
                new_position = (position + shift) % 26
                encrypted_text += alphabets[new_position]
            else:
                encrypted_text += letter
        return render_template('result.html', result=encrypted_text)

    elif operation == "decrypt":
        shift = 3  # Set the shift value to 3 for decryption
        decrypted_text = ""
        for letter in plaintext:
            if letter in alphabets:
                position = alphabets.index(letter)
                new_position = (position - shift) % 26
                decrypted_text += alphabets[new_position]
            else:
                decrypted_text += letter
        return render_template('result.html', result=decrypted_text)


@app.route("/shift-encrypt", methods=['POST'])
def s_encrypt():
    plaintext = request.form["plaintext"].lower()
    operation = request.form["operation"]
    shift_amount = int(request.form["shift"])

    if operation == "encrypt":
        encrypted_text = ""
        for letter in plaintext:
            if letter in alphabets:
                position = alphabets.index(letter)
                new_position = (position + shift_amount) % 26
                encrypted_text += alphabets[new_position]
            else:
                encrypted_text += letter
        return render_template('result.html', result=encrypted_text)

    elif operation == "decrypt":
        decrypted_text = ""
        for letter in plaintext:
            if letter in alphabets:
                position = alphabets.index(letter)
                new_position = (position - shift_amount) % 26
                decrypted_text += alphabets[new_position]
            else:
                decrypted_text += letter
        return render_template('result.html', result=decrypted_text)

if __name__ == "__main__":
    app.run(debug=True)
