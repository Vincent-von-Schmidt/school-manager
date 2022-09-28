CREATE DATABASE IF NOT EXISTS school; 
USE school;

DROP TABLE IF EXISTS public.teacher CASCADE;
CREATE TABLE public.teacher (
    id SERIAL,
    last_name VARCHAR,
    first_name VARCHAR,
    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS public.subject CASCADE;
CREATE TABLE public.subject (
    id SERIAL,
    name VARCHAR,
    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS public.room CASCADE;
CREATE TABLE public.room (
    id SERIAL,
    name VARCHAR(4),
    building VARCHAR(2),
    floor INT,
    room INT,
    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS public.curs CASCADE;
CREATE TABLE public.curs (
    id SERIAL,
    name VARCHAR(3),
    teacher INT,
    subject INT,
    room INT,
    PRIMARY KEY (id),
    FOREIGN KEY (teacher) REFERENCES public.teacher (id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (subject) REFERENCES public.subject (id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (room) REFERENCES public.room (id) ON UPDATE CASCADE ON DELETE CASCADE
);

DROP TABLE IF EXISTS public.times CASCADE;
CREATE TABLE public.times (
    hour INT,
    start_time TIME,
    end_time TIME,
    PRIMARY KEY (hour)
); 

DROP TABLE IF EXISTS public.day CASCADE;
CREATE TABLE public.day (
    id SERIAL,
    name VARCHAR(9),
    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS public.semester CASCADE;
CREATE TABLE public.semester (
    id SERIAL,
    name VARCHAR(2),
    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS public.timetable CASCADE;
CREATE TABLE public.timetable (
    id SERIAL,
    day INT,
    hour INT,
    curs INT,
    semester INT,
    PRIMARY KEY (id),
    FOREIGN KEY (day) REFERENCES public.day (id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (hour) REFERENCES public.times (hour) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (curs) REFERENCES public.curs (id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (semester) REFERENCES public.semester (id) ON UPDATE CASCADE ON DELETE CASCADE
);

INSERT INTO public.times VALUES 
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

INSERT INTO public.day (name) VALUES
('Monday'),
('Tuesday'),
('Wednesday'),
('Thursday'),
('Friday');

INSERT INTO public.semester (name) VALUES
('Q1'),
('Q2'),
('Q3'),
('Q4');

INSERT INTO public.subject (name) VALUES
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

INSERT INTO public.teacher (last_name, first_name) VALUES
('Garibagaoglu', 'Ayse'),
('Ogrisek', 'Gerald'),
('Roschinsky', 'Diane'),
('Herpel', 'Ralph'),
('Plocke', 'Gaby'),
('Ziemer', 'Jörg'),
('Göttner', 'Ulrike'),
('Repkow', 'Norman'),
('Petters', 'Christiane');

INSERT INTO public.room (name, building, floor, room) VALUES
('A109', 'A', 1, 9),
('A118', 'A', 1, 18),
('A112', 'A', 1, 12),
('A004', 'A', 0, 4),
('A027', 'A', 0, 27),
('A302', 'A', 3, 2),
('A211', 'A', 2, 11),
('SW', 'SW', NULL, NULL),
('A207', 'A', 2, 7);

INSERT INTO public.curs (name, teacher, subject, room) VALUES
('G11', 1, 1, 1),
('L12', 2, 2, 2),
('G18', 3, 3, 3),
('G25', 5, 4, 4),
('G39', 2, 5, 2),
('L17', 4, 6, 5),
('G06', 6, 7, 6),
('G02', 7, 8, 7),
('G48', 8, 9, 8), 
('G24', 9, 10, 9);

INSERT INTO public.timetable (day, hour, curs, semester) VALUES
(1, 1, 1, 1),
(1, 2, 1, 1),
(1, 3, 2, 1),
(1, 4, 2, 1),
(1, 5, 3, 1),
(1, 6, 4, 1),
(1, 7, 4, 1),
(2, 1, 5, 1),
(2, 2, 5, 1),
(2, 3, 6, 1),
(2, 4, 6, 1), 
(2, 6, 7, 1),
(2, 7, 7, 1),
(3, 1, 3, 1),
(3, 2, 3, 1), 
(3, 3, 2, 1), 
(3, 4, 2, 1),
(3, 5, 8, 1),
(3, 6, 8, 1),
(3, 7, 9, 1), 
(3, 8, 9, 1),
(4, 1, 10, 1),
(4, 2, 10, 1),
(4, 3, 6, 1), 
(4, 4, 6, 1),
(4, 5, 5, 1),
(5, 1, 4, 1), 
(5, 2, 7, 1), 
(5, 3, 2, 1),
(5, 4, 6, 1), 
(5, 5, 1, 1), 
(5, 6, 8, 1), 
(5, 7, 10, 1);
