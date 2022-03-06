pipeline {
    agent any

    stages {
        stage('checking out code from GitHub') {
            steps {
                git credentialsId: 'GitHubcredentials', url: 'git@github.com:dsenthil17/cicd.git'
            }
        }
        stage('Executing the code') {
            steps {
                sh 'python helloworld.py -m "hello world"'
            }
        }
    }
}
