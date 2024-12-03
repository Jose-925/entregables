CREATE TABLE Alum (
    id INT PRIMARY KEY,
    nom VARCHAR(50),
    edad INT,
    ciud VARCHAR(50)
);

INSERT INTO Alum (nom, edad, ciud) VALUES ('miguel', 20, 'cali');
INSERT INTO Alum (nom, edad, ciud) VALUES ('maria', 22, 'valledupar');
INSERT INTO Alum (nom, edad, ciud) VALUES ('alejandro', 19, 'arauca');

SELECT * FROM Alum;

SELECT * FROM Alum WHERE ciud = 'Medellín';

SELECT * FROM Alum WHERE edad > 20;
