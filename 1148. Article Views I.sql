# Write your MySQL query statement below
"""
Method 1:
Use GROUP BY to remove duplicates
"""
SELECT author_id as id
FROM Views
WHERE author_id = viewer_id
GROUP BY id
ORDER BY id

"""
Method 2:
SELECT distinct, much faster
"""
SELECT distinct author_id as id
FROM Views
WHERE author_id = viewer_id
ORDER BY id
