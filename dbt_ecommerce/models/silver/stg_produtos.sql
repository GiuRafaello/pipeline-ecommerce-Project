SELECT
    id,
    TRIM(title) AS titulo,
    price AS preco,
    TRIM(category) AS categoria,
    TRIM(description) AS descricao
FROM {{ source('bronze', 'produtos_api') }}