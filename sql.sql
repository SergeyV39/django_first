create table book(
    book_id int primary key auto_increment,
    title varchar(50),
    author varchar(30),
    price decimal(8, 2),
    amount int);

insert into book(
title,
author,
price,
amount)
values(
'Мастер и Маргарита',
'Булгаков М.А.',
'670.99',
'3')

select * from book

select author, title, price from book

select title as Название, author as Автор
from book

SELECT title, author, price, amount,
     price * amount AS total
FROM book;

SELECT title,
    price,
    ROUND((price*18/100)/(1+18/100),2) AS tax,
    ROUND(price/(1+18/100),2) AS price_tax
FROM book;

SELECT title, amount, price,
    IF(amount<4, price*0.5, price*0.7) AS sale
FROM book;

SELECT title, amount, price,
    ROUND(IF(amount < 4, price * 0.5, IF(amount < 11, price * 0.7, price * 0.9)), 2) AS sale,
    IF(amount < 4, 'скидка 50%', IF(amount < 11, 'скидка 30%', 'скидка 10%')) AS Ваша_скидка
FROM book;

SELECT title, price
FROM book
WHERE price <> 600;

SELECT title, author, price
FROM book
WHERE author = 'Булгаков М.А.' OR author = 'Есенин С.А.' AND price > 600;

SELECT title, amount
FROM book
WHERE amount BETWEEN 5 AND 14;

SELECT title, amount
FROM book
WHERE amount BETWEEN 5 AND 14;

SELECT author, title, amount AS Количество
FROM book
WHERE price < 750
ORDER BY author, amount DESC;

SELECT title FROM book
WHERE title LIKE "_% и _%" /*отбирает слово И внутри названия */
    OR title LIKE "и _%" /*отбирает слово И в начале названия */
    OR title LIKE "_% и" /*отбирает слово И в конце названия */
    OR title LIKE "и" /* отбирает название, состоящее из одного слова И */

SELECT DISTINCT author
FROM book;

SELECT  author
FROM book
GROUP BY author;

