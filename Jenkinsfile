pipeline {
    agent any
    stages {
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
