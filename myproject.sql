SELECT * FROM users;
SELECT * FROM qoutes;
SELECT * FROM favorites;

SELECT * FROM users
LEFT JOIN qoutes
ON users.id = qoutes.user_id WHERE users.id = 2;

SELECT users.id, users.name, users.password, qoutes.author, qoutes.qoute, favorites.qoute_id FROM users
LEFT JOIN qoutes
ON users.id = qoutes.user_id
LEFT JOIN favorites
on qoutes.id = favorites.qoute_id;

SELECT * FROM users
LEFT JOIN favorites
ON users.id = favorites.user_id;