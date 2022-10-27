CREATE DATABASE IF NOT EXISTS school; 
USE school;

DROP TABLE IF EXISTS teacher CASCADE;
CREATE TABLE teacher (
    id INT NOT NULL AUTO_INCREMENT,
    last_name VARCHAR(12),
    first_name VARCHAR(10),
    PRIMARY KEY (id)
)ENGINE=InnoDB;

DROP TABLE IF EXISTS subject CASCADE;
CREATE TABLE subject (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(11),
    PRIMARY KEY (id)
)ENGINE=InnoDB;

DROP TABLE IF EXISTS room CASCADE;
CREATE TABLE room (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(4),
    building VARCHAR(2),
    floor INT,
    room INT,
    PRIMARY KEY (id)
)ENGINE=InnoDB;

DROP TABLE IF EXISTS curs CASCADE;
CREATE TABLE curs (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(3),
    teacher INT,
    subject INT,
    PRIMARY KEY (id),
    FOREIGN KEY (teacher) REFERENCES teacher (id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (subject) REFERENCES subject (id) ON UPDATE CASCADE ON DELETE CASCADE
)ENGINE=InnoDB;

DROP TABLE IF EXISTS times CASCADE;
CREATE TABLE times (
    hour INT,
    start_time TIME,
    end_time TIME,
    PRIMARY KEY (hour)
)ENGINE=InnoDB; 

DROP TABLE IF EXISTS day CASCADE;
CREATE TABLE day (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(9),
    PRIMARY KEY (id)
)ENGINE=InnoDB;

DROP TABLE IF EXISTS semester CASCADE;
CREATE TABLE semester (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(2),
    PRIMARY KEY (id)
)ENGINE=InnoDB;

DROP TABLE IF EXISTS timetable CASCADE;
CREATE TABLE timetable (
    id INT NOT NULL AUTO_INCREMENT,
    day INT,
    hour INT,
    curs INT,
    room INT,
    semester INT,
    PRIMARY KEY (id),
    FOREIGN KEY (day) REFERENCES day (id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (hour) REFERENCES times (hour) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (curs) REFERENCES curs (id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (room) REFERENCES room (id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (semester) REFERENCES semester (id) ON UPDATE CASCADE ON DELETE CASCADE
)ENGINE=InnoDB;

INSERT INTO times VALUES 
(0, '07:35:00', '08:20:00'),
(1, '08:15:00', '09:00:00'),
(2, '09:10:00', '09:55:00'),
(3, '10:15:00', '11:00:00'),
(4, '11:10:00', '11:55:00'),
(5, '12:30:00', '13:15:00'),
(6, '13:25:00', '14:10:00'),
(7, '14:20:00', '15:05:00'),
(8, '15:15:00', '16:00:00'),
(9, '16:00:00', '16:45:00');

INSERT INTO day (name) VALUES
('Monday'),
('Tuesday'),
('Wednesday'),
('Thursday'),
('Friday');

INSERT INTO semester (name) VALUES
('Q1'),
('Q2'),
('Q3'),
('Q4');

INSERT INTO subject (name) VALUES
('english'),
('physics'),
('history'),
('mathematics'),
('astronomy'),
('informatics'),
('musics'), 
('german'),
('swimming'),
('psychology');

INSERT INTO teacher (last_name, first_name) VALUES
('Garibagaoglu', 'Ayse'),
('Ogrisek', 'Gerald'),
('Roschinsky', 'Diane'),
('Herpel', 'Ralph'),
('Plocke', 'Gaby'),
('Ziemer', 'Jörg'),
('Göttner', 'Ulrike'),
('Repkow', 'Norman'),
('Petters', 'Christiane');

INSERT INTO room (name, building, floor, room) VALUES
('A109', 'A', 1, 9),
('A118', 'A', 1, 18),
('A112', 'A', 1, 12),
('A004', 'A', 0, 4),
('A027', 'A', 0, 27),
('A302', 'A', 3, 2),
('A211', 'A', 2, 11),
('SW', 'SW', NULL, NULL),
('A207', 'A', 2, 7),
('A108', 'A', 1, 8);

INSERT INTO curs (name, teacher, subject) VALUES
('G11', 1, 1),
('L12', 2, 2),
('G18', 3, 3),
('G25', 5, 4),
('G39', 2, 5),
('L17', 4, 6),
('G06', 6, 7),
('G02', 7, 8),
('G48', 8, 9), 
('G24', 9, 10);

INSERT INTO timetable (day, hour, curs, room, semester) VALUES
(1, 1, 1, 1, 1),
(1, 2, 1, 1, 1),
(1, 3, 2, 2, 1),
(1, 4, 2, 2, 1),
(1, 5, 3, 3, 1),
(1, 6, 4, 4, 1),
(1, 7, 4, 4, 1),
(2, 1, 5, 2, 1),
(2, 2, 5, 2, 1),
(2, 3, 6, 5, 1),
(2, 4, 6, 5, 1), 
(2, 6, 7, 6, 1),
(2, 7, 7, 6, 1),
(3, 1, 3, 3, 1),
(3, 2, 3, 3, 1), 
(3, 3, 2, 2, 1), 
(3, 4, 2, 2, 1),
(3, 5, 8, 7, 1),
(3, 6, 8, 7, 1),
(3, 7, 9, 8, 1), 
(3, 8, 9, 8, 1),
(4, 1, 10, 3, 1),
(4, 2, 10, 3, 1),
(4, 3, 6, 5, 1), 
(4, 4, 6, 5, 1),
(4, 5, 5, 2, 1),
(5, 1, 4, 4, 1), 
(5, 2, 7, 6, 1), 
(5, 3, 2, 2, 1),
(5, 4, 6, 5, 1), 
(5, 5, 1, 1, 1), 
(5, 6, 8, 10, 1), 
(5, 7, 10, 9, 1);
