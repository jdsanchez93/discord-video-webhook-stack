# garage-webcam

Usage

1. Build docker image with:
`docker build -t temp-local-upload:0.0.4-deleteme .`

Or, if not using docker, make sure python dependencies are installed:
`pip install -r requirements.txt`

2. Add env-file.txt with environment variables for aws credentials:
```
AWS_ACCESS_KEY_ID=...
AWS_SECRET_ACCESS_KEY=...
```

3. Run script with:
`./docker-upload.ps1`
