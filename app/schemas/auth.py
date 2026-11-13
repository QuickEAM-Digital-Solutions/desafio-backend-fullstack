"""
Authentication Schemas
=======================
Pydantic v2 models for authentication.

You should implement here:
- RegisterRequest: email (EmailStr), full_name (str), password (str, min length 8)
- LoginRequest: email (EmailStr), password (str)   (if you use a JSON login)
- TokenResponse: access_token (str), token_type (str = "bearer")
- UserResponse: id (UUID), email, full_name, created_at
  (use `model_config = ConfigDict(from_attributes=True)` to build it from
  the SQLAlchemy model)
"""
