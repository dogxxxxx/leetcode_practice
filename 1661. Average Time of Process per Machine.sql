# Write your MySQL query statement below
SELECT diff.machine_id, ROUND(AVG(diff.time_diff), 3) as processing_time
FROM
    (SELECT end.machine_id, end.process_id, end.end_time-start.start_time as time_diff
    FROM
        (SELECT machine_id, process_id, timestamp as end_time
        FROM Activity
        WHERE activity_type="end") AS end
    JOIN
        (SELECT machine_id, process_id, timestamp as start_time
        FROM Activity
        WHERE activity_type="start") AS start
    ON end.machine_id=start.machine_id AND end.process_id=start.process_id) AS diff
GROUP BY diff.machine_id