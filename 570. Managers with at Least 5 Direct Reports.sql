SELECT e.name
FROM Employee e,
    (SELECT managerId, COUNT(managerId) AS direct
    FROM Employee
    GROUP BY managerId) AS tmp
WHERE tmp.direct >= 5 and e.id = tmp.managerId