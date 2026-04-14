import os

class Config:
    # Load configuration settings from environment variables
    ENVIRONMENT = os.getenv('ENVIRONMENT', 'development')
    DEBUG = os.getenv('DEBUG', 'False') == 'True'
    DATABASE_URL = os.getenv('DATABASE_URL')
    API_KEY = os.getenv('API_KEY')
    # Add other configuration settings as needed

class BotSettings:
    # Bot specific settings
    BOT_NAME = os.getenv('BOT_NAME', 'MyBot')
    BOT_TOKEN = os.getenv('BOT_TOKEN')
    # Add other bot settings as needed