"""
Main Flask Application for AI Astrology Web App
------------------------------------------------
This file contains all the routes and handles HTTP requests.
It serves as the entry point for the web application.
"""

from flask import Flask, render_template, request, jsonify, send_file
from astrology_engine import AstrologyEngine
from report_generator import ReportGenerator
from pdf_generator import PDFGenerator
import json
from datetime import datetime
import io

# Initialize Flask app
app = Flask(__name__)

# Initialize our custom modules
astrology_engine = AstrologyEngine()
report_generator = ReportGenerator()
pdf_generator = PDFGenerator()


@app.route('/')
def home():
    """
    Home route - displays the input form.
    This is the landing page where users enter their details.
    """
    return render_template('index.html')


@app.route('/generate-report', methods=['POST'])
def generate_report():
    """
    API endpoint to generate an astrology report.
    Receives user data via POST request and returns a comprehensive report.
    """
    try:
        # Get form data from the request
        user_data = {
            'full_name': request.form.get('full_name', ''),
            'gender': request.form.get('gender', ''),
            'date_of_birth': request.form.get('date_of_birth', ''),
            'time_of_birth': request.form.get('time_of_birth', ''),
            'place_of_birth': request.form.get('place_of_birth', ''),
            'country': request.form.get('country', ''),
            'current_city': request.form.get('current_city', ''),
            'relationship_status': request.form.get('relationship_status', ''),
            'occupation': request.form.get('occupation', ''),
            'education_level': request.form.get('education_level', '')
        }
        
        # Calculate basic astrology data (zodiac signs, elements, etc.)
        astrology_data = astrology_engine.calculate_astrology(user_data)
        
        # Generate the full personalized report
        full_report = report_generator.generate_full_report(user_data, astrology_data)
        
        # Combine all data for the response
        response_data = {
            'success': True,
            'user_data': user_data,
            'astrology_data': astrology_data,
            'report': full_report
        }
        
        return jsonify(response_data)
    
    except Exception as e:
        # Handle any errors gracefully
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/download-pdf', methods=['POST'])
def download_pdf():
    """
    Generates and downloads the report as a PDF file.
    """
    try:
        # Parse the JSON data from the request
        data = request.get_json()
        
        # Generate the PDF
        pdf_buffer = pdf_generator.create_pdf(
            data.get('user_data', {}),
            data.get('astrology_data', {}),
            data.get('report', {})
        )
        
        # Send the PDF as a downloadable file
        return send_file(
            pdf_buffer,
            mimetype='application/pdf',
            as_attachment=True,
            download_name=f"astrology_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        )
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/report')
def report_page():
    """
    Renders the report display page.
    The actual report data is loaded dynamically via JavaScript.
    """
    return render_template('report.html')


# Run the application in debug mode during development
print("__name__=", __name__)
if __name__ == "__main__":
    app.run(debug=True, port=5000)
