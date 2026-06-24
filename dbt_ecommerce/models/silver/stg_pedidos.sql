SELECT
    id_pedido,
    id_cliente,
    id_produto,
    quantidade,
    LOWER(TRIM(status)) AS status,
    data_pedido
FROM {{ source('bronze', 'pedidos') }}