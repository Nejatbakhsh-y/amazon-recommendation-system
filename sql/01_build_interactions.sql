-- Build interaction scores

WITH weighted_events AS (
    SELECT
        user_id,
        product_id,
        event_type,
        CASE
            WHEN event_type = 'view' THEN 1
            WHEN event_type = 'click' THEN 3
            WHEN event_type = 'add_to_cart' THEN 5
            WHEN event_type = 'purchase' THEN 10
            ELSE 0
        END AS event_weight
    FROM sample_events
),

aggregated_interactions AS (
    SELECT
        user_id,
        product_id,
        SUM(event_weight) AS interaction_score
    FROM weighted_events
    GROUP BY user_id, product_id
)

SELECT *
FROM aggregated_interactions;
