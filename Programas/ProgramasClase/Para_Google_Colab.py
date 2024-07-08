# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 11:14:48 2024

@author: rober
"""

from google.colab import auth
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
from oauth2client.client import GoogleCredentials

auth.authenticate_user()
gauth = GoogleAuth()
gauth.credentials = GoogleCredentials.get_application_default()
drive = GoogleDrive(gauth)

#El ID es el número que aparece al compartir el archivo
#https://drive.google.com/file/d/1CE8N1aV8UTBS-XyR7cQ971o8PvqeGDcL/view?usp=sharing
myfile = drive.CreateFile({'id': '1CE8N1aV8UTBS-XyR7cQ971o8PvqeGDcL'})
myfile.GetContentFile('datos1.txt')