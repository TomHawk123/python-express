import os


class Config:
    """Base configuration."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_secret_key_here')
    DB1 = os.environ.get(
        'DB1', 'DB1 environment variable not set.')
    DB2 = os.environ.get(
        'DB2', 'DB2 environment variable not set.')
    # Flask-Session, Flask-Login, or Flask-Mail configurations can also go here


class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    # Other development-specific settings like debug toolbar configurations


class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True
    # Testing-specific settings like test database URIs


class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    # Production-specific settings like logging to a file or an external service

# You can add more configurations as needed
