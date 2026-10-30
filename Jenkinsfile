pipeline {
    agent any
    triggers {
        githubPush()
    }
    stages {
        stage('Build') {
            steps {
                git branch: 'main', url: 'https://github.com/abidurahmanshinwari2-art/assignment-2.git'
                script {
                    docker.image('abidkhan2/assignment2-web:v1').pull()
                    docker.image('mysql:8.0').pull()
                }
                sh 'docker compose -f docker-compose.part2.yml -p assignment2part2 down'
                sh 'docker compose -f docker-compose.part2.yml -p assignment2part2 up -d'
            }
        }
    }
    post {
        always {
            script {
                def authorEmail = sh(script: 'git log -1 --format=%ae', returnStdout: true).trim()
                emailext(
                    subject: "Assignment 2 build ${currentBuild.currentResult}: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                    body: "Build result: ${currentBuild.currentResult}\nJob: ${env.JOB_NAME}\nBuild: ${env.BUILD_URL}\nTriggered by: ${authorEmail}",
                    to: authorEmail
                )
            }
        }
    }
}
