SELECT
    p.id_pedido,
    p.data_pedido,
    p.id_cliente,
    c.nome AS nome_cliente,
    p.id_produto,
    pr.titulo AS produto,
    pr.categoria,
    p.quantidade,
    pr.preco,
    p.quantidade * pr.preco AS valor_total,
    p.status
FROM {{ ref('stg_pedidos') }} AS p
LEFT JOIN {{ ref('stg_clientes') }} AS c
    ON p.id_cliente = c.id_cliente
LEFT JOIN {{ ref('stg_produtos') }} AS pr
    ON p.id_produto = pr.id