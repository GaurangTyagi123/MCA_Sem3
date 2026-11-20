FILE INTEGRITY VERIFICATION — PRACTICAL

Aim
To verify file integrity using hashing algorithms and display
'Integrity Verified' or 'Integrity Compromised'.

Algorithms used
- MD5
- SHA-1
- SHA-256
- SHA-512

How it works
1. The program reads a file in binary chunks.
2. hashlib calculates a digest for each selected algorithm.
3. The original digest is retained as the reference value.
4. The current digest is compared with the reference digest.
5. Matching digests mean the file has not changed; a mismatch
   indicates that the file contents have changed.

How to run
1. Install Python 3 (no third-party packages are required).
2. Open a terminal in this folder.
3. Run: python file_integrity_verification.py

Expected observation
- The original file reports 'Integrity Verified' for all algorithms.
- After the program modifies the sample file, it reports
  'Integrity Compromised' for all algorithms.

Note
MD5 and SHA-1 are included to demonstrate different hashing
algorithms, but they are not recommended for security-sensitive
modern applications. SHA-256 or SHA-512 is preferred.
