import os
from dotenv import load_dotenv
from app import create_app
from config import DevelopmentConfig

load_dotenv()

app = create_app(DevelopmentConfig)
# Run the app if this file is executed
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=os.getenv("DEBUG"))
