import string
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import RSLPStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split  # Importação adicionada
from sklearn.ensemble import RandomForestClassifier
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading
import webbrowser
import json
from pathlib import Path

# Configura caminhos
BASE_DIR = Path(__file__).parent
TEMPLATE_DIR = BASE_DIR / 'templates'
ASSETS_DIR = BASE_DIR / 'assets'

class RequestHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_header('Content-type', 'application/json')
        self.end_headers()
    
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open(TEMPLATE_DIR / 'index.html', 'rb') as f:
                self.wfile.write(f.read())
        
        elif self.path == '/styles.css':
            self.send_response(200)
            self.send_header('Content-type', 'text/css')
            self.end_headers()
            with open(ASSETS_DIR / 'styles.css', 'rb') as f:
                self.wfile.write(f.read())
                
    def do_POST(self):
        if self.path == '/analyze':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            try:
                data = json.loads(post_data.decode('utf-8'))
                email_text = data.get('text', '')
                
                if not email_text:
                    raise ValueError("Texto vazio recebido")
                
                processed_email = preprocess_text(email_text)
                x_email = vectorizer.transform([processed_email])
                probs = clf.predict_proba(x_email)[0]
                
                response = {
                    'is_spam': int(probs[1] >= limiar_spam),
                    'probabilities': {
                        'spam': float(probs[1]),
                        'ham': float(probs[0])
                    }
                }
                
                self.send_response(200)
                self._set_headers()
                self.wfile.write(json.dumps(response).encode('utf-8'))
                
            except Exception as e:
                error_msg = f"Erro durante análise: {str(e)}"
                print(error_msg)
                self.send_response(500)
                self._set_headers()
                self.wfile.write(json.dumps({
                    'success': False,
                    'error': error_msg
                }).encode('utf-8'))

def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation)).split()
    text = [stemmer.stem(word) for word in text if word not in stopwords_set]
    return ' '.join(text)

if __name__ == "__main__":
    # Configuração inicial
    TEMPLATE_DIR.mkdir(exist_ok=True)
    ASSETS_DIR.mkdir(exist_ok=True)
    
    # Carrega e treina o modelo
    print("Carregando e treinando o modelo...")
    nltk.download('stopwords', quiet=True)
    nltk.download('rslp', quiet=True)
    
    df = pd.read_csv('Spam_dataset.csv')
    stemmer = RSLPStemmer()
    stopwords_set = set(stopwords.words('portuguese'))
    
    corpus = [preprocess_text(t) for t in df['text']]
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(corpus).toarray()
    y = df.label_num
    
    # Divisão treino/teste (agora com a importação correta)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    clf = RandomForestClassifier(n_jobs=-1, random_state=42)
    clf.fit(X_train, y_train)
    
    limiar_spam = 0.55
    print(f"Modelo treinado - Acurácia: {clf.score(X_test, y_test):.2%}")
    
    # Inicia servidor
    server = HTTPServer(('localhost', 8000), RequestHandler)
    print("\n Servidor iniciado em http://localhost:8000")
    webbrowser.open("http://localhost:8000")
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:

        print("\n Servidor encerrado")
