-- A/B testing metrics

SELECT
    group_name,
    SUM(click) * 1.0 / SUM(impression) AS ctr,
    SUM(purchase) * 1.0 / SUM(click) AS conversion_rate
FROM ab_test_events
GROUP BY group_name;
