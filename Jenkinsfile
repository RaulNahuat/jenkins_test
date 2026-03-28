pipeline {
    // 'agent any' le dice a Jenkins que ejecute este pipeline en cualquier nodo disponible
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Descarga el código más reciente de tu repositorio de GitHub
                checkout scm
                echo 'Código descargado correctamente.'
            }
        }
        
        stage('Instalar y Probar Backend') {
            steps {
                echo 'Preparando el entorno...'
                // Aquí irían los comandos reales del servidor, por ejemplo:
                // sh 'python3 -m venv venv'
                // sh '. venv/bin/activate && pip install -r requirements.txt'
                // sh 'pytest'
            }
        }

        stage('Construir Frontend') {
            steps {
                echo 'Construyendo la aplicación React...'
                // Aquí ejecuta la construcción del frontend:
                // sh 'npm install'
                // sh 'npm run build'
            }
        }

        stage('Despliegue (Simulado)') {
            steps {
                echo 'Iniciando el proceso de despliegue...'
                // Aquí podrías enlazarlo con Docker o Dokploy para levantar los servicios
                // sh 'docker-compose up -d --build'
            }
        }
    }

    // La sección 'post' se ejecuta siempre al final, sin importar si falló o fue exitoso
    post {
        success {
            echo '¡El pipeline se ejecutó con éxito! Todo está listo.'
        }
        failure {
            echo 'Algo salió mal en el pipeline. Revisa los logs en Jenkins.'
        }
    }
}