import json
import os
from datetime import datetime
from flask import Flask, render_template_string, request, jsonify, send_file
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
import io

app = Flask(__name__)

# HTML Template embedded in the code
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Accessible Resume Builder</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background-color: #f4f4f4;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        
        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            text-align: center;
            padding: 2rem;
            border-radius: 10px;
            margin-bottom: 2rem;
        }
        
        .main-content {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 2rem;
        }
        
        .form-section, .preview-section {
            background: white;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        
        .form-group {
            margin-bottom: 1.5rem;
        }
        
        label {
            display: block;
            margin-bottom: 0.5rem;
            font-weight: bold;
            color: #555;
        }
        
        input, textarea, select {
            width: 100%;
            padding: 0.75rem;
            border: 2px solid #ddd;
            border-radius: 5px;
            font-size: 1rem;
            transition: border-color 0.3s;
        }
        
        input:focus, textarea:focus, select:focus {
            outline: none;
            border-color: #667eea;
        }
        
        textarea {
            resize: vertical;
            min-height: 100px;
        }
        
        .btn {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 0.75rem 1.5rem;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 1rem;
            margin-right: 0.5rem;
            margin-bottom: 0.5rem;
            transition: transform 0.2s;
        }
        
        .btn:hover {
            transform: translateY(-2px);
        }
        
        .btn-secondary {
            background: #6c757d;
        }
        
        .dynamic-section {
            border: 2px dashed #ddd;
            padding: 1rem;
            margin-bottom: 1rem;
            border-radius: 5px;
        }
        
        .remove-btn {
            background: #dc3545;
            color: white;
            border: none;
            padding: 0.25rem 0.5rem;
            border-radius: 3px;
            cursor: pointer;
            float: right;
        }
        
        .preview {
            border: 1px solid #ddd;
            padding: 2rem;
            background: white;
            min-height: 600px;
        }
        
        .preview h1 {
            color: #333;
            border-bottom: 2px solid #667eea;
            padding-bottom: 0.5rem;
        }
        
        .preview h2 {
            color: #667eea;
            margin-top: 1.5rem;
            margin-bottom: 0.5rem;
        }
        
        .preview .contact-info {
            margin-bottom: 1rem;
        }
        
        .preview .job, .preview .education, .preview .project {
            margin-bottom: 1rem;
            padding-bottom: 0.5rem;
            border-bottom: 1px solid #eee;
        }
        
        @media (max-width: 768px) {
            .main-content {
                grid-template-columns: 1fr;
            }
        }
        
        .accessibility-features {
            background: #e8f4fd;
            padding: 1rem;
            border-radius: 5px;
            margin-bottom: 1rem;
            border-left: 4px solid #667eea;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🌟 Accessible Resume Builder</h1>
            <p>Create professional, accessible resumes with ease</p>
        </div>
        
        <div class="accessibility-features">
            <h3>♿ Accessibility Features</h3>
            <p>This tool includes screen reader support, keyboard navigation, high contrast colors, and semantic HTML structure for maximum accessibility.</p>
        </div>
        
        <div class="main-content">
            <div class="form-section">
                <h2>📝 Resume Information</h2>
                <form id="resumeForm">
                    <!-- Personal Information -->
                    <div class="form-group">
                        <label for="fullName">Full Name *</label>
                        <input type="text" id="fullName" name="fullName" required aria-describedby="nameHelp">
                        <small id="nameHelp">Enter your full legal name</small>
                    </div>
                    
                    <div class="form-group">
                        <label for="email">Email *</label>
                        <input type="email" id="email" name="email" required>
                    </div>
                    
                    <div class="form-group">
                        <label for="phone">Phone</label>
                        <input type="tel" id="phone" name="phone">
                    </div>
                    
                    <div class="form-group">
                        <label for="location">Location</label>
                        <input type="text" id="location" name="location" placeholder="City, State">
                    </div>
                    
                    <div class="form-group">
                        <label for="linkedin">LinkedIn Profile</label>
                        <input type="url" id="linkedin" name="linkedin" placeholder="https://linkedin.com/in/yourprofile">
                    </div>
                    
                    <div class="form-group">
                        <label for="summary">Professional Summary</label>
                        <textarea id="summary" name="summary" placeholder="Brief overview of your professional background and goals"></textarea>
                    </div>
                    
                    <!-- Experience Section -->
                    <h3>💼 Work Experience</h3>
                    <div id="experienceContainer">
                        <div class="dynamic-section">
                            <button type="button" class="remove-btn" onclick="removeSection(this)">Remove</button>
                            <div class="form-group">
                                <label>Job Title</label>
                                <input type="text" name="jobTitle[]" placeholder="Software Developer">
                            </div>
                            <div class="form-group">
                                <label>Company</label>
                                <input type="text" name="company[]" placeholder="Tech Corp">
                            </div>
                            <div class="form-group">
                                <label>Duration</label>
                                <input type="text" name="duration[]" placeholder="Jan 2020 - Present">
                            </div>
                            <div class="form-group">
                                <label>Description</label>
                                <textarea name="jobDescription[]" placeholder="Key responsibilities and achievements"></textarea>
                            </div>
                        </div>
                    </div>
                    <button type="button" class="btn btn-secondary" onclick="addExperience()">+ Add Experience</button>
                    
                    <!-- Education Section -->
                    <h3>🎓 Education</h3>
                    <div id="educationContainer">
                        <div class="dynamic-section">
                            <button type="button" class="remove-btn" onclick="removeSection(this)">Remove</button>
                            <div class="form-group">
                                <label>Degree</label>
                                <input type="text" name="degree[]" placeholder="Bachelor of Science">
                            </div>
                            <div class="form-group">
                                <label>School</label>
                                <input type="text" name="school[]" placeholder="University Name">
                            </div>
                            <div class="form-group">
                                <label>Year</label>
                                <input type="text" name="gradYear[]" placeholder="2020">
                            </div>
                        </div>
                    </div>
                    <button type="button" class="btn btn-secondary" onclick="addEducation()">+ Add Education</button>
                    
                    <!-- Skills Section -->
                    <div class="form-group">
                        <label for="skills">Skills</label>
                        <textarea id="skills" name="skills" placeholder="JavaScript, Python, React, Node.js (comma-separated)"></textarea>
                    </div>
                    
                    <!-- Projects Section -->
                    <h3>🚀 Projects</h3>
                    <div id="projectsContainer">
                        <div class="dynamic-section">
                            <button type="button" class="remove-btn" onclick="removeSection(this)">Remove</button>
                            <div class="form-group">
                                <label>Project Name</label>
                                <input type="text" name="projectName[]" placeholder="Awesome Web App">
                            </div>
                            <div class="form-group">
                                <label>Technologies</label>
                                <input type="text" name="projectTech[]" placeholder="React, Node.js, MongoDB">
                            </div>
                            <div class="form-group">
                                <label>Description</label>
                                <textarea name="projectDescription[]" placeholder="Project description and key features"></textarea>
                            </div>
                        </div>
                    </div>
                    <button type="button" class="btn btn-secondary" onclick="addProject()">+ Add Project</button>
                    
                    <div style="margin-top: 2rem;">
                        <button type="button" class="btn" onclick="updatePreview()">🔄 Update Preview</button>
                        <button type="button" class="btn" onclick="downloadPDF()">📄 Download PDF</button>
                        <button type="button" class="btn btn-secondary" onclick="saveData()">💾 Save Data</button>
                        <button type="button" class="btn btn-secondary" onclick="loadData()">📂 Load Data</button>
                    </div>
                </form>
            </div>
            
            <div class="preview-section">
                <h2>👀 Live Preview</h2>
                <div id="resumePreview" class="preview">
                    <h1>Your Name</h1>
                    <div class="contact-info">
                        <p>📧 your.email@example.com | 📱 (555) 123-4567</p>
                        <p>📍 Your Location | 🔗 LinkedIn Profile</p>
                    </div>
                    
                    <h2>Professional Summary</h2>
                    <p>Your professional summary will appear here...</p>
                    
                    <h2>Work Experience</h2>
                    <div class="job">
                        <h3>Job Title - Company</h3>
                        <p><em>Duration</em></p>
                        <p>Job description will appear here...</p>
                    </div>
                    
                    <h2>Education</h2>
                    <div class="education">
                        <h3>Degree - School</h3>
                        <p><em>Year</em></p>
                    </div>
                    
                    <h2>Skills</h2>
                    <p>Your skills will be listed here...</p>
                    
                    <h2>Projects</h2>
                    <div class="project">
                        <h3>Project Name</h3>
                        <p><strong>Technologies:</strong> Tech stack</p>
                        <p>Project description...</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
    
    <script>
        // Dynamic form functions
        function addExperience() {
            const container = document.getElementById('experienceContainer');
            const newSection = document.createElement('div');
            newSection.className = 'dynamic-section';
            newSection.innerHTML = `
                <button type="button" class="remove-btn" onclick="removeSection(this)">Remove</button>
                <div class="form-group">
                    <label>Job Title</label>
                    <input type="text" name="jobTitle[]" placeholder="Software Developer">
                </div>
                <div class="form-group">
                    <label>Company</label>
                    <input type="text" name="company[]" placeholder="Tech Corp">
                </div>
                <div class="form-group">
                    <label>Duration</label>
                    <input type="text" name="duration[]" placeholder="Jan 2020 - Present">
                </div>
                <div class="form-group">
                    <label>Description</label>
                    <textarea name="jobDescription[]" placeholder="Key responsibilities and achievements"></textarea>
                </div>
            `;
            container.appendChild(newSection);
        }
        
        function addEducation() {
            const container = document.getElementById('educationContainer');
            const newSection = document.createElement('div');
            newSection.className = 'dynamic-section';
            newSection.innerHTML = `
                <button type="button" class="remove-btn" onclick="removeSection(this)">Remove</button>
                <div class="form-group">
                    <label>Degree</label>
                    <input type="text" name="degree[]" placeholder="Bachelor of Science">
                </div>
                <div class="form-group">
                    <label>School</label>
                    <input type="text" name="school[]" placeholder="University Name">
                </div>
                <div class="form-group">
                    <label>Year</label>
                    <input type="text" name="gradYear[]" placeholder="2020">
                </div>
            `;
            container.appendChild(newSection);
        }
        
        function addProject() {
            const container = document.getElementById('projectsContainer');
            const newSection = document.createElement('div');
            newSection.className = 'dynamic-section';
            newSection.innerHTML = `
                <button type="button" class="remove-btn" onclick="removeSection(this)">Remove</button>
                <div class="form-group">
                    <label>Project Name</label>
                    <input type="text" name="projectName[]" placeholder="Awesome Web App">
                </div>
                <div class="form-group">
                    <label>Technologies</label>
                    <input type="text" name="projectTech[]" placeholder="React, Node.js, MongoDB">
                </div>
                <div class="form-group">
                    <label>Description</label>
                    <textarea name="projectDescription[]" placeholder="Project description and key features"></textarea>
                </div>
            `;
            container.appendChild(newSection);
        }
        
        function removeSection(button) {
            button.parentElement.remove();
            updatePreview();
        }
        
        function updatePreview() {
            const formData = new FormData(document.getElementById('resumeForm'));
            const data = {};
            
            // Get single values
            data.fullName = formData.get('fullName') || 'Your Name';
            data.email = formData.get('email') || 'your.email@example.com';
            data.phone = formData.get('phone') || '(555) 123-4567';
            data.location = formData.get('location') || 'Your Location';
            data.linkedin = formData.get('linkedin') || 'LinkedIn Profile';
            data.summary = formData.get('summary') || 'Your professional summary will appear here...';
            data.skills = formData.get('skills') || 'Your skills will be listed here...';
            
            // Get array values
            data.jobTitles = formData.getAll('jobTitle[]');
            data.companies = formData.getAll('company[]');
            data.durations = formData.getAll('duration[]');
            data.jobDescriptions = formData.getAll('jobDescription[]');
            
            data.degrees = formData.getAll('degree[]');
            data.schools = formData.getAll('school[]');
            data.gradYears = formData.getAll('gradYear[]');
            
            data.projectNames = formData.getAll('projectName[]');
            data.projectTechs = formData.getAll('projectTech[]');
            data.projectDescriptions = formData.getAll('projectDescription[]');
            
            // Update preview
            let previewHTML = `
                <h1>${data.fullName}</h1>
                <div class="contact-info">
                    <p>📧 ${data.email} | 📱 ${data.phone}</p>
                    <p>📍 ${data.location} | 🔗 ${data.linkedin}</p>
                </div>
                
                <h2>Professional Summary</h2>
                <p>${data.summary}</p>
                
                <h2>Work Experience</h2>
            `;
            
            // Add experience entries
            for (let i = 0; i < data.jobTitles.length; i++) {
                if (data.jobTitles[i]) {
                    previewHTML += `
                        <div class="job">
                            <h3>${data.jobTitles[i]} - ${data.companies[i] || 'Company'}</h3>
                            <p><em>${data.durations[i] || 'Duration'}</em></p>
                            <p>${data.jobDescriptions[i] || 'Job description...'}</p>
                        </div>
                    `;
                }
            }
            
            previewHTML += '<h2>Education</h2>';
            
            // Add education entries
            for (let i = 0; i < data.degrees.length; i++) {
                if (data.degrees[i]) {
                    previewHTML += `
                        <div class="education">
                            <h3>${data.degrees[i]} - ${data.schools[i] || 'School'}</h3>
                            <p><em>${data.gradYears[i] || 'Year'}</em></p>
                        </div>
                    `;
                }
            }
            
            previewHTML += `<h2>Skills</h2><p>${data.skills}</p><h2>Projects</h2>`;
            
            // Add project entries
            for (let i = 0; i < data.projectNames.length; i++) {
                if (data.projectNames[i]) {
                    previewHTML += `
                        <div class="project">
                            <h3>${data.projectNames[i]}</h3>
                            <p><strong>Technologies:</strong> ${data.projectTechs[i] || 'Tech stack'}</p>
                            <p>${data.projectDescriptions[i] || 'Project description...'}</p>
                        </div>
                    `;
                }
            }
            
            document.getElementById('resumePreview').innerHTML = previewHTML;
        }
        
        function saveData() {
            const formData = new FormData(document.getElementById('resumeForm'));
            const data = {};
            for (let [key, value] of formData.entries()) {
                if (data[key]) {
                    if (Array.isArray(data[key])) {
                        data[key].push(value);
                    } else {
                        data[key] = [data[key], value];
                    }
                } else {
                    data[key] = value;
                }
            }
            
            fetch('/save', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(data)
            }).then(response => response.json())
              .then(data => alert('Data saved successfully!'))
              .catch(error => alert('Error saving data'));
        }
        
        function loadData() {
            fetch('/load')
                .then(response => response.json())
                .then(data => {
                    if (data.error) {
                        alert('No saved data found');
                        return;
                    }
                    
                    // Populate form fields
                    Object.keys(data).forEach(key => {
                        const element = document.querySelector(`[name="${key}"]`);
                        if (element) {
                            element.value = data[key];
                        }
                    });
                    
                    updatePreview();
                    alert('Data loaded successfully!');
                })
                .catch(error => alert('Error loading data'));
        }
        
        function downloadPDF() {
            const formData = new FormData(document.getElementById('resumeForm'));
            fetch('/generate_pdf', {
                method: 'POST',
                body: formData
            }).then(response => response.blob())
              .then(blob => {
                  const url = window.URL.createObjectURL(blob);
                  const a = document.createElement('a');
                  a.style.display = 'none';
                  a.href = url;
                  a.download = 'resume.pdf';
                  document.body.appendChild(a);
                  a.click();
                  window.URL.revokeObjectURL(url);
              })
              .catch(error => alert('Error generating PDF'));
        }
        
        // Auto-update preview on input
        document.addEventListener('input', updatePreview);
        
        // Initialize preview
        updatePreview();
        
        // Keyboard accessibility
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Tab') {
                // Ensure proper tab navigation
                const focusableElements = document.querySelectorAll('input, textarea, button, select');
                const currentIndex = Array.from(focusableElements).indexOf(document.activeElement);
                
                if (e.shiftKey && currentIndex === 0) {
                    e.preventDefault();
                    focusableElements[focusableElements.length - 1].focus();
                } else if (!e.shiftKey && currentIndex === focusableElements.length - 1) {
                    e.preventDefault();
                    focusableElements[0].focus();
                }
            }
        });
    </script>
</body>
</html>
"""

class ResumeBuilder:
    def __init__(self):
        self.data_file = 'resume_data.json'
    
    def save_resume_data(self, data):
        """Save resume data to JSON file"""
        try:
            with open(self.data_file, 'w') as f:
                json.dump(data, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving data: {e}")
            return False
    
    def load_resume_data(self):
        """Load resume data from JSON file"""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            return None
        except Exception as e:
            print(f"Error loading data: {e}")
            return None
    
    def generate_pdf(self, data):
        """Generate PDF resume from data"""
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter, topMargin=0.5*inch)
        styles = getSampleStyleSheet()
        story = []
        
        # Custom styles
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=18,
            spaceAfter=12,
            textColor='#333333'
        )
        
        heading_style = ParagraphStyle(
            'CustomHeading',
            parent=styles['Heading2'],
            fontSize=14,
            spaceAfter=6,
            textColor='#667eea'
        )
        
        # Title
        story.append(Paragraph(data.get('fullName', 'Resume'), title_style))
        
        # Contact Info
        contact_info = []
        if data.get('email'):
            contact_info.append(f"Email: {data['email']}")
        if data.get('phone'):
            contact_info.append(f"Phone: {data['phone']}")
        if data.get('location'):
            contact_info.append(f"Location: {data['location']}")
        if data.get('linkedin'):
            contact_info.append(f"LinkedIn: {data['linkedin']}")
        
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

# Initialize the resume builder
resume_builder = ResumeBuilder()

@app.route('/')
def index():
    """Main page with the resume builder form"""
    return render_template_string(HTML_TEMPLATE)

@app.route('/save', methods=['POST'])
def save_data():
    """Save resume data to JSON file"""
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
    """Load resume data from JSON file"""
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
    """Generate and download PDF resume"""
    try:
        data = request.form.to_dict(flat=False)
        # Convert single-item lists to strings for non-array fields
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
    print("🚀 Starting Accessible Resume Builder...")
    print("📋 Features included:")
    print("   ✅ Single-file application")
    print("   ✅ Accessible design with ARIA labels")
    print("   ✅ Real-time preview")
    print("   ✅ PDF generation")
    print("   ✅ Data persistence")
    print("   ✅ Dynamic form sections")
    print("   ✅ Responsive design")
    print("   ✅ Keyboard navigation support")
    print("\n🌐 Open your browser and go to: http://localhost:5000")
    print("📝 Fill out the form and watch the live preview update!")
    print("💾 Save your data and generate professional PDFs")
    
    # Install required packages if not available
    try:
        import flask
        import reportlab
    except ImportError:
        print("\n⚠️  Missing dependencies. Please install:")
        print("pip install flask reportlab")
        exit(1)
    
    app.run(debug=True, host='0.0.0.0', port=5000)
