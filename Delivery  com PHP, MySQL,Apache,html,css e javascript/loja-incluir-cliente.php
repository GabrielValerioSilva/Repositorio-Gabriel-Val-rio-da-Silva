<html>
<head>
    <title>Sistema de Gerenciamento de Vendas</title>
    <meta charset="UTF-8">
</head>
<body>
    <h1>Inclusão de Cliente</h1>

    <?php
    // Recuperando os dados do formulário
    $cpf = $_REQUEST["cpf"];
    $nome = $_REQUEST["nome"];
    $telefone = $_REQUEST["telefone"];

    // Estabelecendo a conexão com o banco de dados
    $conexao = mysqli_connect('localhost', 'root', '', 'loja')
    or die("ERRO: Sem conexão.");

    // Montando a consulta SQL para inserção
    $sql = "INSERT INTO cliente (cpf, nome, telefone) VALUES ('$cpf', '$nome', '$telefone')";

    // Executando a consulta
    mysqli_query($conexao, $sql)
    or die("A inclusão falhou: " . mysqli_error($conexao) . "<br>SQL: " . $sql);

    // Fechando a conexão com o banco de dados
    mysqli_close($conexao);
    ?>

    <h2>Cadastro realizado com sucesso!</h2>

    <br />
    <a href="loja-relacao-cliente.php">Voltar</a>
</body>
</html>
