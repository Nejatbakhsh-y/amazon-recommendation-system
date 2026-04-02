-- Train-test split

WITH ranked_events AS (
    SELECT *,
        ROW_NUMBER() OVER (
            PARTITION BY user_id
            ORDER BY event_time DESC
        ) AS rn
    FROM sample_events
)

SELECT *
FROM ranked_events
WHERE rn > 1;
