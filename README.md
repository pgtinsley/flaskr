# Flaskr README

## To run off Paly: 

### 1st Window: 
1. Run: `bash start_ingest.sh`

### 2nd window: 
1. Go to backend/ 
2. Run `export FLASK_APP=api.py` 
3. Run `flask run` 

### 3rd window 
1. Log into paly with port forwarding to 3000 
  `Ssh -L 3000:localhost:3000 <username>@paly.cse.nd.edu`
2. Go to frontend/ 
3. Run `npm install` 
4. Run `npm start` 
