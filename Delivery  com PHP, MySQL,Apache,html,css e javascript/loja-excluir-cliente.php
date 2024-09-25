<html>

<head>
    <title>Sistema de Gerenciamento de Vendas</title>
    <meta charset="UTF-8">
</head>

<body>

<h1>Exclusão de Cliente</h1>

<?php

$cpf = $_REQUEST["cpf"];

// Estabelecer conexão com o banco de dados
$conexao = mysqli_connect('localhost', 'root', '', 'loja') // Altere para suas credenciais
    or die("ERRO: Sem conexão.");

// Comando SQL para excluir o cliente
$sql = "DELETE FROM cliente WHERE cpf = '$cpf'";

// Executar a consulta e verificar erros
if (mysqli_query($conexao, $sql)) {
    echo "<h2>Cliente apagado com sucesso!</h2>";
} else {
    die("A exclusão falhou: " . mysqli_error($conexao) . "<br>SQL: " . $sql);
}

// Fechar a conexão
mysqli_close($conexao);
?>

<br />
<a href="loja-relacao-cliente.php">Voltar</a>

</body>
</html>
