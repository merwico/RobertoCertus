pipeline {
    agent any

    environment {
        GIT_CRED_ID = 'github-cred'
    }

    stages {
        stage('Preparar entorno') {
            steps {
                echo "Creando entorno virtual..."
                echo "Antigua ruta C:\\Users\\ROBERTO\\AppData\\Local\\Programs\\Python\\Python313\\python.exe"
                echo "Nueva ruta C:\\Usersv\malu3\\AppData\\Local\\Programs\\Python\\Python314\\python.exe"
                bat '"C:\\Usersv\malu3\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m venv venv'
                bat 'venv\\Scripts\\activate && pip install -r requirements.txt'
            }
        }
       
        stage('Configurar Git') {
            steps {
                echo "Configurando credenciales de Git..."
                withCredentials([usernamePassword(credentialsId: "${GIT_CRED_ID}", usernameVariable: 'GIT_USER', passwordVariable: 'GIT_TOKEN')]) {
                    bat '''
                    "C:\\Program Files\\Git\\bin\\git.exe" config --global user.name "Jenkins Bot"
                    "C:\\Program Files\\Git\\bin\\git.exe" config --global user.email "jenkins@local"
                    "C:\\Program Files\\Git\\bin\\git.exe" remote set-url origin https://%GIT_USER%:%GIT_TOKEN%@github.com/merwico/RobertoCertus.git
                    '''
                    }
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
