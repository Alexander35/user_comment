\c magnit_1;

INSERT INTO region(name) VALUES 
	('Краснодарский Край'),
	('Ставропольский Край'),
	('Ростовская Область');

INSERT INTO town (name, region) VALUES
    ( 'Краснодар',     (SELECT id from region WHERE name='Краснодарский Край') ),
    ( 'Кропоткин', (SELECT id from region WHERE name='Краснодарский Край' ) ),
    ( 'Славянск',     (SELECT id from region WHERE name='Краснодарский Край') )
    ( 'Ростов',     (SELECT id from region WHERE name='Ростовская Область') ),
    ( 'Шахты', (SELECT id from region WHERE name='Ростовская Область' ) ),
    ( 'Батайск',     (SELECT id from region WHERE name='Ростовская Область') ),
    ( 'Ставрополь',     (SELECT id from region WHERE name='Ставропольский Край') ),
    ( 'Пятигорск', (SELECT id from region WHERE name='Ставропольский Край' ) ),
    ( 'Кисловодск',     (SELECT id from region WHERE name='Ставропольский Край') );	