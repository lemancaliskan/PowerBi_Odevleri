-- 1. Tablolar --
CREATE TABLE developers (
    id SERIAL PRIMARY KEY,
    company_name VARCHAR(100) NOT NULL,
    country VARCHAR(50),
    founded_year INT
)

CREATE TABLE games (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    release_date DATE,
    rating DECIMAL(3,1),
    developer_id INT REFERENCES developers(id) ON DELETE CASCADE
)

CREATE TABLE genres (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description VARCHAR(255)
)

CREATE TABLE games_genres (
    id SERIAL PRIMARY KEY,
    game_id INT REFERENCES games(id) ON DELETE CASCADE,
    genre_id INT REFERENCES genres(id) ON DELETE CASCADE
)

-- 2. Veri Ekleme (INSERT) -- 
INSERT INTO developers (company_name, country, founded_year) VALUES
('CD Projekt Red', 'Poland', 1994),
('Rockstar Games', 'USA', 1998),
('Bethesda', 'USA', 1986),
('Ubisoft', 'France', 1986),
('Valve', 'USA', 1996);

INSERT INTO genres (name, description) VALUES
('RPG', 'Role Playing Game'),
('Open World', 'Açık dünya oyunları'),
('Horror', 'Korku oyunları'),
('FPS', 'First Person Shooter'),
('Sports', 'Spor oyunları');

INSERT INTO games (title, price, release_date, rating, developer_id) VALUES
('The Witcher 3', 700.00, '2015-05-19', 9.5, 1),
('Cyberpunk 2077', 800.00, '2020-12-10', 7.8, 1),
('GTA V', 950.00, '2013-09-17', 9.3, 2),
('Red Dead Redemption 2', 500.00, '2018-10-26', 9.7, 2),
('Skyrim', 650.00, '2011-11-11', 9.0, 3),
('Fallout 4', 750.00, '2015-11-10', 8.7, 3),
('Assassin''s Creed Valhalla', 600.00, '2020-11-10', 8.5, 4),
('Far Cry 6', 820.00, '2021-10-07', 8.2, 4),
('Half-Life: Alyx', 1050.00, '2020-03-23', 9.0, 5),
('Portal 2', 400.00, '2011-04-19', 9.4, 5);

INSERT INTO games_genres (game_id, genre_id) VALUES
(1, 1),
(1, 2),
(2, 1),
(2, 2),
(3, 2),
(3, 4),
(4, 2),
(4, 1),
(5, 1),
(5, 2),
(6, 1),
(6, 4),
(7, 1),
(7, 2),
(8, 4),
(8, 2),
(9, 4),
(9, 3),
(10, 4);

-- 3. UPDATE/DELETE
-- İndirim Zamanı: %10 İndirim
UPDATE games
SET price = price * 0.9;

-- Hata Düzeltme
UPDATE games
SET rating = 9.0
WHERE title = 'Cyberpunk 2077';

-- Kaldırma
DELETE FROM games_genres WHERE game_id = 10;
DELETE FROM games WHERE id = 10;

-- 4. Raporlama (SELECT/JOIN)
--Tüm Oyunlar Listesi
SELECT g.title AS "Oyun Adı", g.price AS "Fiyat", d.company_name AS "Geliştirici"
FROM games g
JOIN developers d ON g.developer_id = d.id;

-- Kategori Filtresi: Sadece RPG olan oyunlar
SELECT g.title, g.rating
FROM games g
JOIN games_genres gg ON g.id = gg.game_id
JOIN genres gn ON gg.genre_id = gn.id
WHERE gn.name = 'RPG';

-- Fiyat Analizi: 500 TL üzerindeki oyunlar
SELECT title, price 
FROM games 
WHERE price > 500 
ORDER BY price DESC;

-- Arama: İçinde "War" kelimesi geçen oyunlar
SELECT * FROM games 
WHERE title LIKE '%War%';