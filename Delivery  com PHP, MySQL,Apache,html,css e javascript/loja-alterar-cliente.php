<html>

<head>
    <title>Sistema de Gerenciamento de Vendas</title>
    <meta charset="UTF-8">
</head>

<body>

<h1>Alteração de Cliente</h1>

<?php

// Receber os dados do formulário
$cpf = $_REQUEST["cpf"];
$nome = $_REQUEST["nome"];
$telefone = $_REQUEST["telefone"];

// Estabelecer conexão com o banco de dados
$conexao = mysqli_connect('localhost', 'root', '', 'loja') // Altere conforme suas credenciais
or die("ERRO: Sem conexão.");

// Comando SQL para atualizar os dados do cliente
$sql = "UPDATE cliente SET nome = '$nome', telefone = '$telefone' WHERE cpf = '$cpf'";

if (mysqli_query($conexao, $sql)) {
    echo "<h2>Alteração realizada com sucesso!</h2>";
} else {
    die("A alteração falhou: " . mysqli_error($conexao) . "<br>SQL: " . $sql);
}

// Fechar a conexão com o banco de dados
mysqli_close($conexao);
?>

<br />
<a href="loja-relacao-cliente.php">Voltar</a>

</body>

</html>
