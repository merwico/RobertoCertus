pipeline {
    agent any

    environment {
        GIT_CRED = credentials('github-cred')
    }

    stages {
        stage('Preparar entorno') {
            steps {
                echo "Creando entorno virtual..."
                bat '"C:\\Users\\ROBERTO\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m venv venv'
                bat 'venv\\Scripts\\activate && pip install -r requirements.txt'
            }
        }

        stage('Configurar Git') {
            steps {
                echo "Configurando credenciales de Git..."
                bat """
                git config --global user.name "Jenkins Bot"
                git config --global user.email "jenkins@local"
                git remote set-url origin https://${env.GIT_CRED_USR}:${env.GIT_CRED_PSW}@github.com/merwico/RobertoCertus.git
                """
            }
        }

        stage('Ejecutar script') {
            steps {
                echo "Ejecutando script principal..."
                bat 'venv\\Scripts\\activate && python Proyecto.py'
            }
        }
    }

    post {
        success { echo "✅ Pipeline completado con éxito" }
        failure { echo "❌ Error en alguna etapa del pipeline" }
    }
}
