pipeline {
    agent any
    stages {
        stage('fetch') {
            steps {
                sh 'git clone https://github.com/erenaspire7/Calc-Test.git'
            }
        }
        stage('run') {
            steps {
                sh 'python calculator.py'
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
    }
}