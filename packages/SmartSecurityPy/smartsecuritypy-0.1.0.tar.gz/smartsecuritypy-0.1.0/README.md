# 🔐 SmartSecurityPy

**SmartSecurityPy** é uma biblioteca Python leve e poderosa para tarefas de segurança como **hash de senha**, **criptografia simétrica** e **validação de JWTs**. Ideal para APIs, backends e projetos que precisam de proteção de dados sensíveis.

---

## ⚙️ Instalação

```bash
pip install SmartSecurityPy
```

> Requer Python 3.7 ou superior

---

## ✨ Funcionalidades

### 🔑 Hash de Senhas com Bcrypt
```python
from SmartSecurityPy import hasher

hashed = hasher.hash_password("minha_senha_segura")
print(hashed)

# Verificação
autenticado = hasher.verify_password("minha_senha_segura", hashed)
print(autenticado)  # True
```

---

### 🔒 Criptografia e Descriptografia com Fernet
```python
from SmartSecurityPy import crypto

# Gera uma chave segura
key = crypto.generate_key()

# Criptografa uma mensagem
mensagem = "dado confidencial"
token = crypto.encrypt_message(mensagem, key)

# Descriptografa
original = crypto.decrypt_message(token, key)
print(original)  # "dado confidencial"
```

---

### 🪙 JWT (JSON Web Tokens)
```python
from SmartSecurityPy import jwt_handler

# Cria um token JWT
data = {"user_id": 123, "role": "admin"}
token = jwt_handler.create_token(data, expires_in_minutes=30)

# Decodifica o token
decoded = jwt_handler.decode_token(token)
print(decoded)

# Verifica se é válido
print(jwt_handler.is_token_valid(token))  # True
```

---

## 📁 Estrutura do Projeto

```
SmartSecurityPy/
├── SmartSecurityPy/
│   ├── __init__.py
│   ├── hasher.py          # 🔑 Hash de senha
│   ├── crypto.py          # 🔒 Criptografia simétrica
│   └── jwt_handler.py     # 🪙 Geração e validação de JWT
│
├── tests/
│   ├── test_hasher.py
│   ├── test_crypto.py
│   └── test_jwt_handler.py
│
├── setup.py
├── pyproject.toml
├── README.md
└── LICENSE
```

---

## 🧪 Testes
Execute os testes com `pytest`:

```bash
pytest tests/
```

---

## 🧠 Autor
**Roberto Lima**  
🔗 GitHub: [robertolima-dev](https://github.com/robertolima-dev)  
📧 Email: robertolima.izphera@gmail.com

---

## 💬 **Contato**

- 📧 **Email**: robertolima.izphera@gmail.com
- 💼 **LinkedIn**: [Roberto Lima](https://www.linkedin.com/in/roberto-lima-01/)
- 💼 **Website**: [Roberto Lima](https://robertolima-developer.vercel.app/)
- 💼 **Gravatar**: [Roberto Lima](https://gravatar.com/deliciouslyautomaticf57dc92af0)

---

## ⭐ **Gostou do projeto?**

Deixe uma ⭐ no repositório e compartilhe com a comunidade! 🚀✨  

```bash
git clone https://github.com/robertolima-dev/SmartSecurityPy.git
cd SmartSecurityPy
pip install -e .
```

---

## 🌟 **O que este README oferece?**
- 🎯 **Descrição clara** do projeto e seu propósito.  
- 🛠 **Instruções detalhadas de instalação** e **uso prático**.  
- 🏗 **Estrutura do projeto** para facilitar a navegação.  
- 📝 **Licença e informações do autor** para transparência.


---

## 📄 Licença
MIT License - use livremente com reconhecimento. 🚀
