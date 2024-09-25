<html>
<head>
    <title>Sistema de Gerenciamento de Vendas</title>
    <meta charset="UTF-8">
</head>
<body>
    <h1>Clientes Cadastrados</h1>

    <?php
    // Estabelecendo a conexão com o banco de dados
    $conexao = mysqli_connect('localhost', 'root', '', 'loja')
    or die("ERRO: Sem conexão.");

    // Consulta SQL para selecionar os clientes
    $sql = "SELECT cpf, nome, telefone FROM cliente";
    $res = mysqli_query($conexao, $sql)
    or die("A consulta falhou: " . mysqli_error($conexao) . "<br>SQL: " . $sql);

    // Criando a tabela para exibir os dados
    echo "<table border='1'><tr>" .
         "<td>&nbsp;</td><td>CPF</td><td>Nome</td>" .
         "<td>Telefone</td></tr>";

    // Loop para exibir os dados dos clientes
    while ($campo = mysqli_fetch_array($res)) {
        echo "<tr><td>" .
             "<a href='13-loja-editar-cliente.php?cpf=" . $campo["cpf"] . "'><img src='imagens/alterar.gif'></a>" .
             "<a href='13-loja-excluir-cliente.php?cpf=" . $campo["cpf"] . "'><img src='imagens/excluir.gif'></a>" .
             "</td>" .
             "<td>" . $campo["cpf"] . "</td><td>" . utf8_encode($campo["nome"]) . "</td><td>" . $campo["telefone"] . "</td></tr>";
    }

    echo "</table>";

    // Liberando os resultados e fechando a conexão
    mysqli_free_result($res);
    mysqli_close($conexao);
    ?>

    <br />
    <a href="loja-cadastro-cliente.php">Novo cliente...</a>
</body>
</html>
