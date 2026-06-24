SELECT
    pr.id AS id_produto,
    pr.titulo AS produto,
    pr.categoria,
    pr.preco,
    COUNT(DISTINCT ped.id_pedido) AS total_pedidos,
    SUM(ped.quantidade) AS unidades_vendidas,
    SUM(ped.quantidade * pr.preco) AS faturamento_total,
    ROUND(AVG(av.nota), 2) AS nota_media,
    COUNT(DISTINCT av.id_avaliacao) AS total_avaliacoes
FROM {{ ref('stg_produtos') }} AS pr
LEFT JOIN {{ ref('stg_pedidos') }} AS ped
    ON pr.id = ped.id_produto
LEFT JOIN {{ ref('stg_avaliacoes') }} AS av
    ON pr.id = av.id_produto
GROUP BY pr.id, pr.titulo, pr.categoria, pr.preco
ORDER BY faturamento_total DESC