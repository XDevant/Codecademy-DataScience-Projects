# 0

.headers on
.mode csv
.import CSV/chat.csv chat
.import CSV/stream.csv stream
.mode list

#1

SELECT * FROM chat LIMIT 20;

SELECT * FROM stream LIMIT 20;

#2

SELECT DISTINCT game 
FROM stream 
ORDER BY 1;

#3

SELECT DISTINCT channel 
FROM stream 
ORDER BY 1;

#4

.mode csv
.once CSV/topgames.csv
SELECT game, COUNT(*) AS viewers 
FROM stream 
GROUP BY game 
ORDER BY 2 DESC
LIMIT 10;
.mode list

#5

SELECT country,COUNT(*) AS views
FROM stream
WHERE game='League of Legends'
GROUP BY 1
ORDER BY 2 DESC;

#5bis

.mode csv
.once CSV/wwlol.csv
WITH wwlol AS (
  SELECT country,COUNT(*) AS views
  FROM stream
  WHERE game='League of Legends'
  GROUP BY 1
  ORDER BY 2 DESC)
SELECT CASE
 WHEN wwlol.views > 2800 THEN wwlol.country
 ELSE 'Other145'
 END AS country,
       SUM(views) AS viewers
FROM wwlol
GROUP BY 1
ORDER BY 2 DESC;
.mode list

#6

SELECT player, COUNT(*) AS views
FROM stream
GROUP BY 1
ORDER BY 2 DESC;

#7

SELECT DISTINCT game, 
    CASE
     WHEN (game = 'League of Legends') OR (game = 'Dota 2') OR (game = 'Heroes of the Storm') THEN 'MOBA'
     WHEN game = 'Counter-Strike: Global Offensive' THEN 'FPS'
     WHEN (game = 'DayZ') OR (game = 'ARK: Survival Evolved') THEN 'Survival'
     ELSE 'Other'
    END AS genre
FROM stream
GROUP BY 1
ORDER BY 2;

#8

SELECT time
FROM stream
LIMIT 10;

#9

SELECT time,
   strftime('%S', time)
FROM stream
GROUP BY 1
LIMIT 20;

#10

.mode csv
.once CSV/usviewperhour.csv

SELECT strftime('%H', time),
COUNT(*) AS viewers
FROM stream
WHERE country = 'FR'
GROUP BY 1;

.mode list

#11

SELECT * 
FROM stream 
JOIN chat
 ON stream.device_id = chat.device_id
LIMIT 10;

#12

SELECT stream.*, COUNT(chat.time) AS chats 
FROM stream 
LEFT JOIN chat 
ON stream.device_id = chat.device_id 
GROUP BY 1;