from flask import Flask, render_template, request, redirect, url_for, flash
from data import USER_DATA

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_super_segura_aqui_123'  # Mude isso em produção!

# Configuração para usar a pasta 'tampletes' como está no seu projeto
app.template_folder = 'tampletes'

@app.route('/')
def index():
    """Rota principal - exibe o portfólio"""
    return render_template('index.html', data=USER_DATA)

@app.route('/submit', methods=['POST'])
def submit():
    """Processa o formulário de contacto"""
    try:
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Validação básica
        if not name or not email or not message:
            flash('Todos os campos são obrigatórios!', 'error')
            return redirect(url_for('index') + '#contacto')
        
        # Aqui você pode adicionar lógica para enviar email, salvar no banco, etc.
        print(f"\n{'='*50}")
        print(f"NOVA MENSAGEM DE CONTACTO")
        print(f"{'='*50}")
        print(f"Nome: {name}")
        print(f"Email: {email}")
        print(f"Mensagem: {message}")
        print(f"{'='*50}\n")
        
        flash(f'Obrigado, {name}! Mensagem recebida com sucesso. Responderei em breve!', 'success')
        return redirect(url_for('index') + '#contacto')
        
    except Exception as e:
        print(f"Erro ao processar formulário: {e}")
        flash('Ocorreu um erro ao enviar a mensagem. Tente novamente.', 'error')
        return redirect(url_for('index') + '#contacto')

@app.errorhandler(404)
def page_not_found(e):
    """Página não encontrada"""
    return redirect(url_for('index'))

@app.errorhandler(500)
def internal_error(e):
    """Erro interno do servidor"""
    flash('Ocorreu um erro no servidor. Por favor, tente novamente.', 'error')
    return redirect(url_for('index'))

if __name__ == '__main__':
    print("\n" + "="*60)
    print("🚀 PORTFÓLIO FLASK - SERVIDOR INICIADO")
    print("="*60)
    print("📍 URL: http://127.0.0.1:5000")
    print("📍 URL: http://localhost:5000")
    print("💡 Pressione CTRL+C para parar o servidor")
    print("="*60 + "\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
