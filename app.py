from src.alllib import *
from src.routes.employee import employee
from src.routes.admin import admin

app = Flask(__name__)

cors = CORS(app, resources={ r'/*': {'origins': '*'}}, supports_credentials=True)
app.config['CORS_HEADERS'] = 'Content-Type'

# For register the blueprint
app.register_blueprint(employee, url_prefix="/employee")
app.register_blueprint(admin, url_prefix="/admin")















if __name__ == "__main__":
  app.run(host="0.0.0.0",port="6055", debug=os.getenv('debug'))
