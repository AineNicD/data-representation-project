CREATE DATABASE Vaccination;

USE Vaccination;


CREATE TABLE users (
    id int(11) NOT NULL AUTO_INCREMENT,
    username VARCHAR (250),
    pass VARCHAR (250),
    PRIMARY KEY(id));

INSERT INTO users (username, pass)
Values ( 'user1', 'pass1');

INSERT INTO users (username, pass)
Values ( 'user2', 'pass2');


CREATE TABLE recipients (
    id int(250) NOT NULL,
    firstname VARCHAR (250),
    surname VARCHAR (250),
    vaccine VARCHAR (250),
    PRIMARY KEY(id)
);

INSERT INTO recipients VALUES
('0851112222', 'James', 'Murphy', 'Pfizer'),
('0872124280', 'Mary', 'Conneely', 'Pfizer'),
('0887971222', 'John', 'Barett', 'Johnson'),
('0821373473', 'Brad', 'Hughes', 'Moderna'),
('0459715643', 'Lilly', 'Hill', 'Pfizer'),
('0727279080', 'Ann', 'King', 'Moderna'),
('0894261241', 'Cecilia', 'Gray', 'Pfizer'),
('0827826732', 'Jacob', 'Ross', 'Johnson'),
('0832953100', 'Tim', 'Davidson', 'Johnson');

CREATE TABLE vaccinators (
    reg_no int(250) NOT NULL,
    firstname varchar(250) NOT NULL,
    surname varchar(250) NOT NULL,
    profession varchar(250) NOT NULL,
    PRIMARY KEY (reg_no)
);

INSERT INTO vaccinators VALUES
('607040', 'Adelina', 'Rankin', 'paramedic'),
('065620', 'Riaan', 'Stacey', 'nurse'),
('788797', 'Jeanne', 'Smart', 'doctor'),
('282137', 'Karam', 'Melia', 'pharmacist'),
('283237', 'Russ', 'Swords', 'nurse'),
('21237', 'Chanel', 'Boot', 'receptionist'),
('284537', 'James', 'Acaster', 'pharmacist');


