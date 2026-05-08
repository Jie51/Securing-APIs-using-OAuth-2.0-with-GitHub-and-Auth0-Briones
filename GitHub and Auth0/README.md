# OAuth 2.0 Integration with GitHub

## Project Overview
[cite_start]This laboratory activity demonstrates how to implement the OAuth 2.0 authorization framework using Python and Flask[cite: 2, 14]. [cite_start]The application allows users to log in using their GitHub accounts and secures specific API endpoints using authentication sessions[cite: 10, 11].

## Features
- [cite_start]**GitHub OAuth Login**: Users can authenticate using their GitHub credentials[cite: 16].
- [cite_start]**Protected Routes**: The `/profile` and `/api/secure-data` routes are restricted to authenticated users only[cite: 84, 163].
- [cite_start]**Session Management**: Uses Flask sessions to track login status and handle logouts[cite: 11, 96].

## Prerequisites
- Python 3.x
- [cite_start]GitHub Developer Account (to create OAuth App) [cite: 31]

## Installation & Setup
1. **Clone the repository**:
   ```bash
   git clone <your-repo-link>
   cd <folder-name>