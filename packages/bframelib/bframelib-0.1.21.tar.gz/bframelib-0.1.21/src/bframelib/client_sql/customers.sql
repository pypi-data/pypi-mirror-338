{% if _BF_BRANCH_ID == 1 %}
SELECT * EXCLUDE(rank)
FROM (
    SELECT raw.*, ROW_NUMBER() OVER(
        PARTITION BY raw.id
        ORDER BY raw.version DESC
    ) AS rank
    FROM (
        SELECT *
        FROM bframe._raw_customers
    ) AS raw
)
WHERE rank = 1
{% else %}
SELECT * EXCLUDE(rank)
FROM (
    SELECT raw.*, ROW_NUMBER() OVER(
        PARTITION BY raw.id
        ORDER BY raw.version DESC
    ) AS rank
    FROM (
        SELECT *
        FROM bframe._raw_customers
        UNION ALL
        SELECT *
        FROM bframe._local_customers
    ) AS raw
)
WHERE rank = 1
{% endif %}