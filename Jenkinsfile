pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS=credentials('dockerhub')
    }

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/nileshamlapure/fastapi.git'
            }
        }
        
        stage('Run Pylama') {
            steps {
                script{
                    sh "pip install pylama[toml]"
                }
            }
        }
        stage('Approval-CodeOwner') {
            steps {
                script {
                    env.Release = input message: "Provide the owner approval", ok: "Done", parameters: [string(defaultValue: 'yes', name: 'Approval Status', trim: true)]
                    echo "Code Owner Approved"
                }
            }
        }
        stage('Deploy To UvicornDev') {
            steps {
                script{
                        sh 'sudo docker-compose up -d --build'
                }
            }
        }
        stage('Execute Tests') {
            steps {
                script{
                        sh "sudo docker-compose exec -T app pytest test/test.py"

                }
            }
        }
        stage('Push Image to Private Repo') {
            steps {
                script{
                    sh  '''
                        echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin
                        sudo docker push 808748/samta:latest
                    '''

                }
            }
        }
    }
}
