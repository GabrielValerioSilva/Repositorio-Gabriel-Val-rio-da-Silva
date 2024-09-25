<?php
$conexao = mysqli_connect('localhost', 'root', '', 'loja')
or die("ERRO: Sem conexão.");

$sql = "SELECT cpf, nome, telefone FROM cliente";
$resultado = mysqli_query($conexao, $sql)
or die("A consulta falhou: ". mysqli_error($conexao). "<br>SQL:". $sql);

while ($campo = mysqli_fetch_array($resultado)) {
    echo "CPF: " . $campo["cpf"] . "<br />Nome: " . $campo["nome"] . "<br />Telefone: " . $campo["telefone"];
}

mysqli_free_result($resultado);
mysqli_close($conexao);
?>
