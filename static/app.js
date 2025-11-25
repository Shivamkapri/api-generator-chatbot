// Drag & Drop and File Picker
const uploadArea = document.getElementById('uploadArea');
const fileInput = document.getElementById('fileInput');
const browseBtn = document.getElementById('browseBtn');
const languageSelect = document.getElementById('language');
const otherLanguage = document.getElementById('otherLanguage');
const uploadForm = document.getElementById('uploadForm');
const codeOutput = document.getElementById('codeOutput');
const downloadBtn = document.getElementById('downloadBtn');

let uploadedFile = null;
let generatedCode = '';

// Drag & Drop events
uploadArea.addEventListener('dragover', (e) => {
    e.preventDefault();
    uploadArea.classList.add('dragover');
});
uploadArea.addEventListener('dragleave', () => {
    uploadArea.classList.remove('dragover');
});
uploadArea.addEventListener('drop', (e) => {
    e.preventDefault();
    uploadArea.classList.remove('dragover');
    if (e.dataTransfer.files.length) {
        fileInput.files = e.dataTransfer.files;
        uploadedFile = e.dataTransfer.files[0];
    }
});

browseBtn.addEventListener('click', () => fileInput.click());
fileInput.addEventListener('change', (e) => {
    if (e.target.files.length) {
        uploadedFile = e.target.files[0];
    }
});

// Language select
languageSelect.addEventListener('change', () => {
    if (languageSelect.value === 'other') {
        otherLanguage.style.display = 'inline-block';
    } else {
        otherLanguage.style.display = 'none';
    }
});

// Form submit
uploadForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    if (!uploadedFile) {
        alert('Please upload a file.');
        return;
    }
    let language = languageSelect.value;
    if (language === 'other') {
        language = otherLanguage.value.trim();
        if (!language) {
            alert('Please enter a language.');
            return;
        }
    }
    const formData = new FormData();
    formData.append('file', uploadedFile);
    formData.append('language', language);
    codeOutput.textContent = 'Generating code...';
    downloadBtn.style.display = 'none';
    try {
        const response = await fetch('/generate', {
            method: 'POST',
            body: formData
        });
        if (!response.ok) throw new Error('Failed to generate code');
        const data = await response.json();
        generatedCode = data.code;
        codeOutput.textContent = generatedCode;
        downloadBtn.style.display = 'block';
    } catch (err) {
        codeOutput.textContent = 'Error: ' + err.message;
    }
});

downloadBtn.addEventListener('click', () => {
    const blob = new Blob([generatedCode], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'generated_code.txt';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
});
