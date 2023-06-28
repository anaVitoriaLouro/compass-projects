//Captura o elemento pelo id e fica "esperando" um clique no botão "Validar meus dados" para ativar a função validate
document.getElementById("botao_submit").addEventListener("click", validate)

/** 
Obtém o valor do campo **nome** na página index.html e retorna como uma string.
@function
@returns {string} O valor do campo "nome".
*/
function getNome(){
  const nome = document.getElementById("nome").value
  return nome
}

/** 
Obtém o valor do campo **email** na página index.html e retorna como uma string.
@function
@returns {string} O valor do campo "email".
*/
function getEmail(){
  const email = document.getElementById("email").value
  return email
}

/** 
Obtém o valor do número de telefone a partir do campo **numero** na página index.html e retorna como uma string.
@function
@returns {string} O valor do campo "numero".
*/
function getTelefone(){
  const telefone = document.getElementById("numero").value
  return telefone
}

/**
 * Classe que valida nomes de pessoas.
 * @class ValidaNome
 */
class ValidaNome {  

  /** 
  Avalia se a string **nome** contém somente caracteres válidos para um nome de pessoa.
  Nomes com acento ou com o caracter "ç" são aceitos.

  @param {string} nome - String contendo o nome a ser validado.
  @returns {string|boolean} - Retorna o nome caso seja válido ou false caso seja inválido.
  @example
  const nomeValido = ValidaNome.ehNome('José da Silva');
  return nomeValido; // Output: José da Silva
  
  const nomeInvalido = ValidaNome.ehNome('João123');
  return false; // Output: false
  */        
  static ehNome(nome){
    if (/^[a-zA-ZÀ-ú\sçÇ]+$/.test(nome)) {
      return nome;
    } else {
      return false;
    }
  }
}

/**
 * Classe para validação de endereço de email.
 * @class ValidaEmail
 */
class ValidaEmail {

  /** 
  O método ehEmail() avalia se a string **email** possui um padrão válido para um endereço de email.
  São aceitos somente os tipos de domínio .com .edu. .net .br e .org
  O domínio do email deve consistir de no mínimo dois caracteres.

  @param {string} email - String contendo o email a ser validado.
  @returns {string|boolean} - Retorna o email caso seja válido ou false caso seja inválido.
  @example
  const emailValido = ValidaEmail.ehEmail('teste@dominio.com');
  return emailValido; // Output: teste@dominio.com
  
  const emailInvalido = ValidaNome.ehEmail('usuario@a.gov');
  return false; // Output: false
  */ 
  static ehEmail(email) {
    const regexEmail = /^[a-z0-9._%+-]+@[a-z0-9.-]+\.(com|org|net|br|edu)$/;
    if (regexEmail.test(email)) {
      let dominio = email.split("@")[1].split(".")[0];
      if (dominio.length >= 2){
        return email;
      }
    } else{
      return false;
    }       
  }
}

/**
 * Classe para validação de um número de telefone.
 * @class ValidaTelefone
 */
class ValidaTelefone {

  /** 
  O método ehTelefone() avalia se a string **numero** está no formato exigido para um número de telefone: (NN)NNNN-NNNN

  @param {string} numero - String contendo o numero de telefone a ser validado.
  @returns {string|boolean} - Retorna o numero de telefone caso seja válido ou false caso seja inválido.
  @example
  const numeroValido = ValidaTelefone.ehTelefone('(12)3456-7890');
  return telefoneValido; // Output: (12)3456-7890
  
  const numeroInvalido = ValidaTelefone.ehTelefone('99 1234 5678');
  return false; // Output: false
  */ 
  static ehTelefone(numero) {
    const regexTelefone = /^\(\d{2}\)\d{4}-\d{4}$/;
    if (regexTelefone.test(numero)) {
      return numero;
    } else{
      return false;
    }       
  }
}
         


//Início do trecho principal do código

/**
Valida dados fornecidos pelo usuário. 
Recebe os valores dos campos de entrada de dados (nome, email e telefone) do formulário HTML e verifica se são valores válidos.
Retorna mensagens de erro ou confirmação para os campos "Nome", "E-mail" e "Telefone".
@function
@param {Event} event - O evento que acionou a validação.
 */
function validate(event){

  //Armazena as referências dos elementos DOM onde os resultados da validação serão exibidos usando o seletor $ do jQuery.
  let $result_email = $("#result_email")        
  let $result_name = $("#result_name")
  let $result_numero = $("#result_numero")
  //Limpa o conteúdo dos elementos HTML para que uma nova mensagem (de confirmação ou erro) seja gerada toda vez que o botão "Validar meus dados" for clicado.
  $result_email.text("")
  $result_name.text("")
  $result_numero.text("")
  //Obtém os valores dos campos de entrada de dados usando o método val() do jQuery.
  let email = $("#email").val()
  let name = $("#name").val()
  let numero = $("#numero").val()
  
  //Chama os métodos ehNome(), ehEmail() e ehTelefone() das classes ValidaNome, ValidaEmail e ValidaTelefone para avaliar os valores digitados pelo usuário.
  //Retorna mensagens com estilo específicos em caso de validação (verde), ou não (vermelho) dos dados digitados.
  if(!ValidaNome.ehNome(name)){
    $result_name.text("Nome inválido!")
    $result_name.css("color", "red")
  } else{  
    $result_name.text("Nome válido: " + name)
    $result_name.css("color", "green")
  }

  if(!ValidaEmail.ehEmail(email.toLowerCase())){
    $result_email.text("Endereço de email inválido! Tipos de domínio aceitos: .com, .net, .br, .org ou .br")
    $result_email.css("color", "red")
  } else{  
    $result_email.text("Email válido: " + email)
    $result_email.css("color", "green")
  }

  if(!ValidaTelefone.ehTelefone(numero)){
    $result_numero.text("Número de telefone inválido! Por favor, utilize o formato (NN)NNNN-NNNN")
    $result_numero.css("color", "red")
  } else {
    $result_numero.text("Telefone válido: " + numero)
    $result_numero.css("color", "green")
  }

//A instrução prevent default evita que a página não atualize e os dados já digitados nos inputs sejam perdidos.
  event.preventDefault()
}
