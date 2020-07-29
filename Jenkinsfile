properties([pipelineTriggers([githubPush()])])

pipeline {
    agent any
    stages {
        stage('install pytest') {
            steps {
                sh 'pip install pytest'   
            }
            
        }
        stage('fetch') {
            steps {
                sh 'git clone https://github.com/erenaspire7/Calc-Test.git'
            }
        }
        stage('test') {
            steps {
                sh 'python -m pytest test_calculator.py '
            }
        }
    }
    post {
        always {
            echo 'Job execution complete.'
        }
        unsuccessful {
            echo 'Job execution status is failed, please check error logs'
        }
        cleanup {
            sh 'rm -rf Calc-Test'
        }
    }
}
