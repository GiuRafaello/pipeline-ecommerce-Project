SELECT
    id_cliente,
    INITCAP(TRIM(nome)) AS nome,
    LOWER(TRIM(email)) AS email,
    TRIM(cidade) AS cidade,
    TRIM(estado) AS estado,
    data_cadastro
FROM {{ source('bronze', 'clientes') }}