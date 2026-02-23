import os
import hashlib
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg'}
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

def safe_upload_file(file, upload_folder):
    """
    SAFE: Secure file upload with validation
    """
    # Validate file extension
    filename = secure_filename(file.filename)
    if '.' not in filename:
        raise ValueError("File must have extension")
    
    ext = filename.rsplit('.', 1)[1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise ValueError(f"Extension {ext} not allowed")
    
    # Validate file size
    file.seek(0, os.SEEK_END)
    size = file.tell()
    file.seek(0)
    
    if size > MAX_FILE_SIZE:
        raise ValueError("File too large")
    
    # Generate safe filename with hash
    hash_name = hashlib.sha256(filename.encode()).hexdigest()[:16]
    safe_name = f"{hash_name}.{ext}"
    
    # Save to validated path
    save_path = os.path.join(upload_folder, safe_name)
    file.save(save_path)
    
    return safe_name
