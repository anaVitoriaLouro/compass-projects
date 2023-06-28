const mensagemSubmit = document.getElementById("mensagem");
const submit = {
  nome: '',
  email: '',
  telefone: ''
}

// Validação de Nome
function validarNome() {
  const nome = document.getElementById("nome").value;
  
  const mensagemElement = document.getElementById("erroNome");
  mensagemSubmit.textContent = "";
  mensagemElement.textContent = "";
  if (nome.length < 2) {
    mensagemElement.textContent = "Nome devera conter no minimo 2 caracteres.";
  } else {
    const validador = new ValidadorNome(nome);
    const resultado = validador.validar();
    if (!resultado) {
      mensagemElement.textContent = "Nome inválido.";
    } else {
      submit.nome = nome;
      if (estaPreenchido())
        document.getElementById('botao-submit').disabled = false;
    }
  }
}

// Validação de E-mail
function validarEmail() {
  const email = document.getElementById("email").value;
  const validador = new ValidadorEmail(email);
  const resultado = validador.validar();

  const mensagemElement = document.getElementById("erroEmail");
  mensagemSubmit.textContent = "";
  mensagemElement.textContent = "";
  if (!resultado) {
    mensagemElement.textContent = "E-mail inválido. O formato deve ser example@example.com";
  } else {
    submit.email = email;
    if (estaPreenchido())
      document.getElementById('botao-submit').disabled = false;
  }
}

// Validação de Telefone
function validarTelefone() {
  const telefone = document.getElementById("telefone").value;
  const validador = new ValidadorTelefone(telefone);
  const resultado = validador.validar();

  const mensagemElement = document.getElementById("erroTelefone");
  mensagemSubmit.textContent = "";
  mensagemElement.textContent = "";
  if (!resultado) {
    mensagemElement.textContent = "Telefone inválido. O formato deve ser (NN)NNNN-NNNN.";
  } else {
    submit.telefone = telefone;
    if (estaPreenchido())
      document.getElementById('botao-submit').disabled = false;
  }
}
class ValidadorNome {
  constructor(nome) {
    this.nome = nome;
  }

  validar() {
    const regex = /(^[A-ZÀ-úa-z\s]+$)/
    if (!regex.test(this.nome)) {
      return false;
    }
    return true;
  }
}
  
class ValidadorTelefone {
  constructor(telefone) {
    this.telefone = telefone;
  }

  validar() {
    const regex = /^\(\d{2}\)\d{4}-\d{4}$/; // regex para verificar se o telefone está no formato correto
    if (!regex.test(this.telefone)) {
      return false
    }
    return true
  }
}
class ValidadorEmail {
  constructor(email) {
    this.email = email;
  }

  validar() {
    const regex = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    if (!regex.test(this.email)) {
      return false
    }
    return true;
  }
}

 
//Chamadas de validação
function estaPreenchido() {
  if (submit.nome && submit.email && submit.telefone) {
    return true;
  }
  return false
}

document.getElementById("telefone").addEventListener("keyup", (e) => {
  //(NN)NNNN-NNNN
  const key = e.target.value;
  if (key.length === 1)
    e.target.value = `(${key}`

  if (key.length === 3)
    e.target.value = `(${key.substring(1, 3)})`

  if (key.length >= 8)
    e.target.value = `(${key.substring(1, 3)})${key.substring(4, 8)}-${key.substring(9)}`
});

document.getElementById("botao-submit").addEventListener("click", (e) => {
  e.preventDefault();
  if (estaPreenchido()) {
    mensagemSubmit.innerText = `Nome: ${submit.nome}\n 
      E-mail: ${submit.email}\n 
      Telefone: ${submit.telefone}\n`;
  }

}); 