# import os
# import json
# from datetime import datetime
# from flask import Flask, render_template, request, jsonify, send_file
# from reportlab.lib.pagesizes import letter
# from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
# from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
# from reportlab.lib.units import inch
# import io

# app = Flask(__name__, static_folder='static', template_folder='templates')

# # ---- Resume Builder Logic ----
# class ResumeBuilder:
#     def __init__(self):
#         self.data_file = 'resume_data.json'

#     def save_resume_data(self, data):
#         try:
#             with open(self.data_file, 'w') as f:
#                 json.dump(data, f, indent=2)
#             return True
#         except Exception as e:
#             print(f"Error saving data: {e}")
#             return False

#     def load_resume_data(self):
#         try:
#             if os.path.exists(self.data_file):
#                 with open(self.data_file, 'r') as f:
#                     return json.load(f)
#             return None
#         except Exception as e:
#             print(f"Error loading data: {e}")
#             return None

#     def generate_pdf(self, data):
#         buffer = io.BytesIO()
#         doc = SimpleDocTemplate(buffer, pagesize=letter, topMargin=0.5*inch)
#         styles = getSampleStyleSheet()
#         story = []

#         # Custom styles
#         title_style = ParagraphStyle('CustomTitle', parent=styles['Heading1'], fontSize=18, spaceAfter=12, textColor='#333333')
#         heading_style = ParagraphStyle('CustomHeading', parent=styles['Heading2'], fontSize=14, spaceAfter=6, textColor='#667eea')

#         # Title
#         story.append(Paragraph(data.get('fullName', 'Resume'), title_style))

#         # Contact Info
#         contact_info = []
#         if data.get('email'): contact_info.append(f"Email: {data['email']}")
#         if data.get('phone'): contact_info.append(f"Phone: {data['phone']}")
#         if data.get('location'): contact_info.append(f"Location: {data['location']}")
#         if data.get('linkedin'): contact_info.append(f"LinkedIn: {data['linkedin']}")
#         if contact_info:
#             story.append(Paragraph(" | ".join(contact_info), styles['Normal']))
#             story.append(Spacer(1, 12))

#         # Professional Summary
#         if data.get('summary'):
#             story.append(Paragraph("Professional Summary", heading_style))
#             story.append(Paragraph(data['summary'], styles['Normal']))
#             story.append(Spacer(1, 12))

#         # Work Experience
#         job_titles = data.get('jobTitle[]', []) if isinstance(data.get('jobTitle[]'), list) else [data.get('jobTitle[]')] if data.get('jobTitle[]') else []
#         companies = data.get('company[]', []) if isinstance(data.get('company[]'), list) else [data.get('company[]')] if data.get('company[]') else []
#         durations = data.get('duration[]', []) if isinstance(data.get('duration[]'), list) else [data.get('duration[]')] if data.get('duration[]') else []
#         descriptions = data.get('jobDescription[]', []) if isinstance(data.get('jobDescription[]'), list) else [data.get('jobDescription[]')] if data.get('jobDescription[]') else []

#         if job_titles and any(job_titles):
#             story.append(Paragraph("Work Experience", heading_style))
#             for i in range(len(job_titles)):
#                 if i < len(job_titles) and job_titles[i]:
#                     job_title = job_titles[i] if i < len(job_titles) else ""
#                     company = companies[i] if i < len(companies) else ""
#                     duration = durations[i] if i < len(durations) else ""
#                     description = descriptions[i] if i < len(descriptions) else ""
#                     story.append(Paragraph(f"<b>{job_title} - {company}</b>", styles['Normal']))
#                     if duration:
#                         story.append(Paragraph(f"<i>{duration}</i>", styles['Normal']))
#                     if description:
#                         story.append(Paragraph(description, styles['Normal']))
#                     story.append(Spacer(1, 6))

#         # Education
#         degrees = data.get('degree[]', []) if isinstance(data.get('degree[]'), list) else [data.get('degree[]')] if data.get('degree[]') else []
#         schools = data.get('school[]', []) if isinstance(data.get('school[]'), list) else [data.get('school[]')] if data.get('school[]') else []
#         years = data.get('gradYear[]', []) if isinstance(data.get('gradYear[]'), list) else [data.get('gradYear[]')] if data.get('gradYear[]') else []

#         if degrees and any(degrees):
#             story.append(Paragraph("Education", heading_style))
#             for i in range(len(degrees)):
#                 if i < len(degrees) and degrees[i]:
#                     degree = degrees[i] if i < len(degrees) else ""
#                     school = schools[i] if i < len(schools) else ""
#                     year = years[i] if i < len(years) else ""
#                     story.append(Paragraph(f"<b>{degree} - {school}</b>", styles['Normal']))
#                     if year:
#                         story.append(Paragraph(f"<i>{year}</i>", styles['Normal']))
#                     story.append(Spacer(1, 6))

#         # Skills
#         if data.get('skills'):
#             story.append(Paragraph("Skills", heading_style))
#             story.append(Paragraph(data['skills'], styles['Normal']))
#             story.append(Spacer(1, 12))

#         # Projects
#         project_names = data.get('projectName[]', []) if isinstance(data.get('projectName[]'), list) else [data.get('projectName[]')] if data.get('projectName[]') else []
#         project_techs = data.get('projectTech[]', []) if isinstance(data.get('projectTech[]'), list) else [data.get('projectTech[]')] if data.get('projectTech[]') else []
#         project_descriptions = data.get('projectDescription[]', []) if isinstance(data.get('projectDescription[]'), list) else [data.get('projectDescription[]')] if data.get('projectDescription[]') else []

#         if project_names and any(project_names):
#             story.append(Paragraph("Projects", heading_style))
#             for i in range(len(project_names)):
#                 if i < len(project_names) and project_names[i]:
#                     name = project_names[i] if i < len(project_names) else ""
#                     tech = project_techs[i] if i < len(project_techs) else ""
#                     desc = project_descriptions[i] if i < len(project_descriptions) else ""
#                     story.append(Paragraph(f"<b>{name}</b>", styles['Normal']))
#                     if tech:
#                         story.append(Paragraph(f"<b>Technologies:</b> {tech}", styles['Normal']))
#                     if desc:
#                         story.append(Paragraph(desc, styles['Normal']))
#                     story.append(Spacer(1, 6))

#         doc.build(story)
#         buffer.seek(0)
#         return buffer

# resume_builder = ResumeBuilder()

# # ---- Routes ----

# @app.route('/')
# def home():
#     # Render the job platform (index.html)
#     return render_template('index.html')

# @app.route('/resume')
# def resume():
#     # Render the resume builder (resume.html)
#     return render_template('resume.html')

# @app.route('/save', methods=['POST'])
# def save_data():
#     try:
#         data = request.get_json()
#         if resume_builder.save_resume_data(data):
#             return jsonify({"success": True, "message": "Data saved successfully"})
#         else:
#             return jsonify({"success": False, "message": "Error saving data"})
#     except Exception as e:
#         return jsonify({"success": False, "message": str(e)})

# @app.route('/load', methods=['GET'])
# def load_data():
#     try:
#         data = resume_builder.load_resume_data()
#         if data:
#             return jsonify(data)
#         else:
#             return jsonify({"error": "No saved data found"})
#     except Exception as e:
#         return jsonify({"error": str(e)})

# @app.route('/generate_pdf', methods=['POST'])
# def generate_pdf():
#     try:
#         data = request.form.to_dict(flat=False)
#         for key, value in data.items():
#             if isinstance(value, list) and len(value) == 1 and not key.endswith('[]'):
#                 data[key] = value[0]
#         pdf_buffer = resume_builder.generate_pdf(data)
#         return send_file(
#             pdf_buffer,
#             as_attachment=True,
#             download_name=f"resume_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf",
#             mimetype='application/pdf'
#         )
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
    

import os
import json
from datetime import datetime
from flask import Flask, render_template, request, jsonify, send_file
from flask_cors import CORS
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
import io

app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)  # Enable CORS for all routes

# ---- Resume Builder Logic ----
class ResumeBuilder:
    def __init__(self):
        self.data_file = 'resume_data.json'

    def save_resume_data(self, data):
        try:
            with open(self.data_file, 'w') as f:
                json.dump(data, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving data: {e}")
            return False

    def load_resume_data(self):
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            return None
        except Exception as e:
            print(f"Error loading data: {e}")
            return None

    def generate_pdf(self, data):
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter, topMargin=0.5*inch)
        styles = getSampleStyleSheet()
        story = []

        # Custom styles
        title_style = ParagraphStyle('CustomTitle', parent=styles['Heading1'], fontSize=18, spaceAfter=12, textColor='#333333')
        heading_style = ParagraphStyle('CustomHeading', parent=styles['Heading2'], fontSize=14, spaceAfter=6, textColor='#667eea')

        # Title
        story.append(Paragraph(data.get('fullName', 'Resume'), title_style))

        # Contact Info
        contact_info = []
        if data.get('email'): contact_info.append(f"Email: {data['email']}")
        if data.get('phone'): contact_info.append(f"Phone: {data['phone']}")
        if data.get('location'): contact_info.append(f"Location: {data['location']}")
        if data.get('linkedin'): contact_info.append(f"LinkedIn: {data['linkedin']}")
        if contact_info:
            story.append(Paragraph(" | ".join(contact_info), styles['Normal']))
            story.append(Spacer(1, 12))

        # Professional Summary
        if data.get('summary'):
            story.append(Paragraph("Professional Summary", heading_style))
            story.append(Paragraph(data['summary'], styles['Normal']))
            story.append(Spacer(1, 12))

        # Work Experience
        job_titles = data.get('jobTitle[]', []) if isinstance(data.get('jobTitle[]'), list) else [data.get('jobTitle[]')] if data.get('jobTitle[]') else []
        companies = data.get('company[]', []) if isinstance(data.get('company[]'), list) else [data.get('company[]')] if data.get('company[]') else []
        durations = data.get('duration[]', []) if isinstance(data.get('duration[]'), list) else [data.get('duration[]')] if data.get('duration[]') else []
        descriptions = data.get('jobDescription[]', []) if isinstance(data.get('jobDescription[]'), list) else [data.get('jobDescription[]')] if data.get('jobDescription[]') else []

        if job_titles and any(job_titles):
            story.append(Paragraph("Work Experience", heading_style))
            for i in range(len(job_titles)):
                if i < len(job_titles) and job_titles[i]:
                    job_title = job_titles[i] if i < len(job_titles) else ""
                    company = companies[i] if i < len(companies) else ""
                    duration = durations[i] if i < len(durations) else ""
                    description = descriptions[i] if i < len(descriptions) else ""
                    story.append(Paragraph(f"<b>{job_title} - {company}</b>", styles['Normal']))
                    if duration:
                        story.append(Paragraph(f"<i>{duration}</i>", styles['Normal']))
                    if description:
                        story.append(Paragraph(description, styles['Normal']))
                    story.append(Spacer(1, 6))

        # Education
        degrees = data.get('degree[]', []) if isinstance(data.get('degree[]'), list) else [data.get('degree[]')] if data.get('degree[]') else []
        schools = data.get('school[]', []) if isinstance(data.get('school[]'), list) else [data.get('school[]')] if data.get('school[]') else []
        years = data.get('gradYear[]', []) if isinstance(data.get('gradYear[]'), list) else [data.get('gradYear[]')] if data.get('gradYear[]') else []

        if degrees and any(degrees):
            story.append(Paragraph("Education", heading_style))
            for i in range(len(degrees)):
                if i < len(degrees) and degrees[i]:
                    degree = degrees[i] if i < len(degrees) else ""
                    school = schools[i] if i < len(schools) else ""
                    year = years[i] if i < len(years) else ""
                    story.append(Paragraph(f"<b>{degree} - {school}</b>", styles['Normal']))
                    if year:
                        story.append(Paragraph(f"<i>{year}</i>", styles['Normal']))
                    story.append(Spacer(1, 6))

        # Skills
        if data.get('skills'):
            story.append(Paragraph("Skills", heading_style))
            story.append(Paragraph(data['skills'], styles['Normal']))
            story.append(Spacer(1, 12))

        # Projects
        project_names = data.get('projectName[]', []) if isinstance(data.get('projectName[]'), list) else [data.get('projectName[]')] if data.get('projectName[]') else []
        project_techs = data.get('projectTech[]', []) if isinstance(data.get('projectTech[]'), list) else [data.get('projectTech[]')] if data.get('projectTech[]') else []
        project_descriptions = data.get('projectDescription[]', []) if isinstance(data.get('projectDescription[]'), list) else [data.get('projectDescription[]')] if data.get('projectDescription[]') else []

        if project_names and any(project_names):
            story.append(Paragraph("Projects", heading_style))
            for i in range(len(project_names)):
                if i < len(project_names) and project_names[i]:
                    name = project_names[i] if i < len(project_names) else ""
                    tech = project_techs[i] if i < len(project_techs) else ""
                    desc = project_descriptions[i] if i < len(project_descriptions) else ""
                    story.append(Paragraph(f"<b>{name}</b>", styles['Normal']))
                    if tech:
                        story.append(Paragraph(f"<b>Technologies:</b> {tech}", styles['Normal']))
                    if desc:
                        story.append(Paragraph(desc, styles['Normal']))
                    story.append(Spacer(1, 6))

        doc.build(story)
        buffer.seek(0)
        return buffer

resume_builder = ResumeBuilder()

# ---- Routes ----

@app.route('/')
def home():
    # Render the job platform (index.html)
    return render_template('index.html')

@app.route('/resume')
def resume():
    # Render the resume builder (resume.html)
    return render_template('resume.html')

@app.route('/api/resume-builder')
def resume_builder_api():
    # API endpoint that returns resume builder URL
    return jsonify({
        "success": True,
        "redirect_url": f"{request.url_root}resume",
        "message": "Resume builder is ready"
    })

@app.route('/save', methods=['POST'])
def save_data():
    try:
        data = request.get_json()
        if resume_builder.save_resume_data(data):
            return jsonify({"success": True, "message": "Data saved successfully"})
        else:
            return jsonify({"success": False, "message": "Error saving data"})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})

@app.route('/load', methods=['GET'])
def load_data():
    try:
        data = resume_builder.load_resume_data()
        if data:
            return jsonify(data)
        else:
            return jsonify({"error": "No saved data found"})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/generate_pdf', methods=['POST'])
def generate_pdf():
    try:
        data = request.form.to_dict(flat=False)
        for key, value in data.items():
            if isinstance(value, list) and len(value) == 1 and not key.endswith('[]'):
                data[key] = value[0]
        pdf_buffer = resume_builder.generate_pdf(data)
        return send_file(
            pdf_buffer,
            as_attachment=True,
            download_name=f"resume_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf",
            mimetype='application/pdf'
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)