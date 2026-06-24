SELECT
    ` id_avaliacao` AS id_avaliacao,
    id_produto,
    id_cliente,
    ` nota` AS nota,
    TRIM(` titulo`) AS titulo,
    TRIM(` comentario`) AS comentario,
    recomenda,
    data_avaliacao
FROM {{ source('bronze', 'avaliacoes') }}