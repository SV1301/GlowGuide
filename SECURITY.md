# Security Policy

## Supported Versions

The current hackathon MVP is version `0.1.0`.

## Reporting a Vulnerability

If you find a security issue, please open a private report with the project maintainer or create an issue without exposing sensitive details publicly.

## Current Security Notes

- The review page uses a simple demo passcode for MVP purposes.
- Do not use the demo passcode system for production.
- Do not commit `.env` files or secrets.
- User contributions must be reviewed before publication.

## Future Security Improvements

- Add proper maintainer authentication.
- Add role-based access control.
- Move hosted data to Supabase PostgreSQL or another managed database.
- Add input validation and spam protection.
