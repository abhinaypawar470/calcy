from flask import Flask, render_template, request, jsonify
import os

# Initialize Flask app
app = Flask(__name__)

# Define a route for the calculator
@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    if request.method == "POST":
        try:
            data= request.json
            main_data=data.get('data')
            print("frontend Data: ", main_data)
            result = eval(main_data)
            response = {
                "message": f"Data '{result}' received successfully!",
                "status": "success",
                "data": result  # Add the result to the response
            }
            return jsonify(response)
        except (SyntaxError, ValueError, TypeError) as e:
            return jsonify({"message": f"Error: {str(e)}", "status": "error"}), 400
    return render_template("index.html")

# Run the app
if __name__ == "__main__":
    # port=int(os.environ.get("PORT",8080))
    # app.run(host="0.0.0.0", port=port)
    app.run(debug=True)
