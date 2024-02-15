# Write your MySQL query statement below
SELECT full.student_id, full.student_name, full.subject_name, COUNT(e.student_id) as attended_exams
FROM
    (SELECT *
    FROM Students stu
    CROSS JOIN Subjects sub) as full
LEFT JOIN Examinations e
ON full.subject_name = e.subject_name AND full.student_id = e.student_id
GROUP BY e.subject_name, full.student_id, full.subject_name
ORDER BY full.student_id, full.subject_name 