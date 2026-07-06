pipeline {
	agent any

	environment {
		DOCKERHUB_CREDENTIAL = credentials('dockerhub-creds')
		DOCKERHUB_IMAGE = 'vyankatesh23/practice-calculator'
		}

	stages {
		stage ('checkout') {
			steps {
				checkout scm
				}
			}
		
		stage ('Run Test') {
			steps {
				sh 'pip install -r requirements.txt --break-system-package'
				sh 'pytest'
				}
			}

		stage ('Build Image') {
			steps {
				sh 'docker build -t $DOCKERHUB_IMAGE .'
				}
			}
		
		stage ('login to docker') {
			steps {
				sh 'echo $DOCKERHUB_CREDENTIAL_PSW | docker login -u $DOCKERHUB_CREDENTIAL_USR --password-stdin'
				}
			}
	
		stage ('push image') {
			steps {
				sh 'docker push $DOCKERHUB_IMAGE' 
				}
			}
		}
	}
