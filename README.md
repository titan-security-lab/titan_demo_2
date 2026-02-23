# TITAN Validation Test Suite

Extended test suite for TITAN vulnerability scanner validation.

## 🔴 Vulnerable Functions (10)

1. **vuln_path_traversal.py** - Path Traversal (CWE-22)
2. **vuln_xxe.py** - XML External Entity (CWE-611)
3. **vuln_command_injection.java** - Command Injection (CWE-78)
4. **vuln_deserialization.py** - Insecure Deserialization (CWE-502)
5. **vuln_ldap_injection.java** - LDAP Injection (CWE-90)
6. **vuln_ssrf.py** - Server-Side Request Forgery (CWE-918)
7. **vuln_hardcoded_credentials.py** - Hardcoded Credentials (CWE-798)
8. **vuln_weak_random.py** - Weak Random (CWE-330)
9. **vuln_race_condition.py** - Race Condition (CWE-362)
10. **vuln_buffer_overflow.c** - Buffer Overflow (CWE-120)

## ✅ Safe Functions (5)

1. **safe_file_upload.py** - Secure file upload with validation
2. **safe_jwt.py** - Secure JWT generation
3. **safe_password.py** - Secure password hashing with bcrypt
4. **safe_input_validation.py** - Proper input sanitization
5. **safe_api_call.py** - Safe API calls with validation

## Expected Results

- **Vulnerable:** 10/10 should be detected
- **Safe:** 5/5 should be marked safe
- **Target Accuracy:** 100% (15/15)
