from flask import Flask, request, make_response
import json
from flask_cors import CORS, cross_origin
import pymysql
from flask import *
import requests
from flask.json import JSONEncoder
import os
import hashlib
import jwt
from dotenv import load_dotenv
import os
import time
import calendar

# Load environment variables from .env file
load_dotenv()