INSERT INTO students (name, second_name) VALUES ('evgeniy', 'sapychev' )

INSERT INTO books (title, taken_by_student_id) VALUES ('py_test', 435)

INSERT INTO books (title, taken_by_student_id) VALUES ('книга', 435)

INSERT INTO `groups`  (title, start_date, end_date) VALUES ('Давно купил, и не закончил2', 'summer24', 'summer25')

UPDATE students s set group_id  = (select id from st4.`groups` ORDER BY id DESC LIMIT 1) where s.id = 435

INSERT INTO subjets (title) VALUES ('Сорян, выше заменил всем id, потом поправил, но не восстановил')

INSERT INTO subjets (title) VALUES ('pythone_best_subj')

INSERT into lessons (title, subject_id ) VALUES ('сегодня', 294)

INSERT into lessons (title, subject_id ) VALUES ('завтра', 294)

INSERT into lessons (title, subject_id ) VALUES ('послезавтра', 295)

INSERT into lessons (title, subject_id ) VALUES ('вчера', 295)

INSERT into marks (value, lesson_id, student_id) VALUES (2, 660, 435)

INSERT into marks (value, lesson_id, student_id) VALUES (3, 661, 435)

INSERT into marks (value, lesson_id, student_id) VALUES (4, 662, 435)

INSERT into marks (value, lesson_id, student_id) VALUES (5, 663, 435)

select value from st4.marks m where student_id = 435

select title from st4.books where books.taken_by_student_id  = 435

SELECT * 
from students s2
JOIN st4.marks m on s2.id = m.student_id
JOIN st4.books b on s2.id = b.taken_by_student_id 
JOIN st4.lessons l  on l.id  = m.lesson_id 
JOIN st4.subjets s on s.id = l.subject_id
where s2.id = 435
