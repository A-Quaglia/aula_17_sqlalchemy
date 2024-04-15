SELECT fornecedores.nome, SUM(produtos.preco) AS total_preco
FROM produtos
JOIN fornecedores ON produtos.fornecedor_id  = fornecedores.id
GROUP BY fornecedores.nome;

-- Fornecedor A	100
-- Fornecedor B	200
-- Fornecedor C	300
-- Fornecedor D	400
-- Fornecedor E	500