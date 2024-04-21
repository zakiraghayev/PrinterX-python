from flask import Flask, request, jsonify
import escpos.printer

app = Flask(__name__)

@app.route('/print', methods=['POST'])
def print_text():
    try:
        # Assuming USB connection; adapt parameters as necessary
        p = escpos.printer.Usb(0x04b8, 0x0202)
        text = request.json.get('text', 'No text provided')
        p.text(text + "\n")
        p.cut()
        return jsonify(success=True, message="Printed successfully"), 200
    except Exception as e:
        return jsonify(success=False, message=str(e)), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
