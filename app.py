from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def bfhl():
    if request.method == 'POST':
        # Get data from the request JSON
        data = request.json.get('data', [])
        full_name = request.json.get('full_name')
        dob = request.json.get('dob')

        # Check if both full_name and dob are provided
        if not full_name or not dob:
            return jsonify({"is_success": False, "message": "Full name and date of birth are required."}), 400

        # Generate the user_id based on full_name and dob
        user_id = f"{full_name.lower().replace(' ', '_')}_{dob}"
        
        # Hardcoded email and roll_number for the example
        email = "john@xyz.com"
        roll_number = "ABCD123"
        
        # Process the input data
        numbers = [item for item in data if item.isdigit()]
        alphabets = [item for item in data if item.isalpha()]
        lowercase_alphabets = [item for item in alphabets if item.islower()]
        highest_lowercase_alphabet = max(lowercase_alphabets) if lowercase_alphabets else None
        
        # Construct the response
        response = {
            "is_success": True,
            "user_id": user_id,
            "email": email,
            "roll_number": roll_number,
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": [highest_lowercase_alphabet] if highest_lowercase_alphabet else []
        }
        return jsonify(response)
    
    # If the method is not POST, return an error
    return jsonify({"message": "Method not allowed"}), 405

@app.route('/bfhl', methods=['GET'])
def get_bfhl():
    return jsonify({"operation_code": 1})

if __name__ == '__main__':
    app.run(debug=True)
