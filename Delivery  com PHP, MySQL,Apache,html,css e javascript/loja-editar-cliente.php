<html>

<head>
    <title>Sistema de Gerenciamento de Vendas</title>
    <meta charset="UTF-8">
</head>

<body>

<h1>Alteração de Clientes</h1>

<?php

$cpf = $_REQUEST["cpf"];

// Estabelecer conexão com o banco de dados
$conexao = mysqli_connect('localhost', 'root', '', 'loja') 
    or die("ERRO: Sem conexão.");

// Comando SQL para selecionar o cliente
$sql = "SELECT nome, telefone FROM cliente WHERE cpf = '$cpf'";

$res = mysqli_query($conexao, $sql) or die("A consulta falhou: " . mysqli_error($conexao) . "<br>SQL: " . $sql);

if ($campo = mysqli_fetch_array($res)) {
    ?>

    <form action="loja-alterar-cliente.php" method="post">
        <p>
            CPF: <input type="text" name="cpf" value="<?php echo $cpf; ?>" readonly />
        </p>
        <p>
            Nome: <input type="text" name="nome" value="<?php echo utf8_encode($campo["nome"]); ?>" />
        </p>
        <p>
            Telefone: <input type="text" name="telefone" value="<?php echo $campo["telefone"]; ?>" />
        </p>
        <p><input value="Salvar" type="submit" /></p>
    </form>

    <?php
}

mysqli_free_result($res);
mysqli_close($conexao);

?>

</body>

</html>
