pipeline {
    agent any

    stages {
        stage('Test') {
            steps {
                script {
                    // Uruchom testy jednostkowe
                    sh 'python -m unittest discover'
                }
            }
        }
    }

    post {
        always {
            // Zachowaj wynik w Jenkinsie
            junit 'test-results/results.xml'
        }
    }
}
