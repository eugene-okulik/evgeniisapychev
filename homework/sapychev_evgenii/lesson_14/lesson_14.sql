INSERT INTO students (name, second_name) VALUES ('evgeniy', 'sapychev' )

INSERT INTO books (title, taken_by_student_id) VALUES ('py_test', (select id from st4.students where second_name = 'sapychev'))

INSERT INTO books (title, taken_by_student_id) VALUES ('книга, а как найти время для учебы', (select id from st4.students where second_name = 'sapychev'))

INSERT INTO `groups`  (title, start_date, end_date) VALUES ('Давно купил, и не закончил2', 'summer24', 'summer25')

UPDATE students s set group_id  = (select id from st4.`groups` ORDER BY id DESC LIMIT 1) where s.second_name = 'sapychev'

INSERT INTO subjets (title) VALUES ('Сорян, выше заменил всем id, потом поправил, но не восстановил')

INSERT INTO subjets (title) VALUES ('pythone_best_subj')

INSERT into lessons (title, subject_id ) VALUES ('завтра', (select id from st4.subjets s where title = 'Сорян, выше заменил всем id, потом поправил, но не восстановил'))

INSERT into lessons (title, subject_id ) VALUES ('послезавтра', (select id from st4.subjets s where title = 'pythone_best_subj'))

INSERT into marks (value, lesson_id, student_id) VALUES (2, (select id from st4.lessons where title = 'завтра'), (select id from st4.students where second_name = 'sapychev'))

INSERT into marks (value, lesson_id, student_id) VALUES (3, (select id from st4.lessons where title = 'вчера'), (select id from st4.students where second_name = 'sapychev'))

INSERT into marks (value, lesson_id, student_id) VALUES (4, (select id from st4.lessons where title = 'сегодня'), (select id from st4.students where second_name = 'sapychev'))

INSERT into marks (value, lesson_id, student_id) VALUES (5, (select id from st4.lessons where title = 'послезавтра'), (select id from st4.students where second_name = 'sapychev'))

select value from st4.marks m where student_id = (select id from st4.students where second_name = 'sapychev')

select title from st4.books where books.taken_by_student_id  = (select id from st4.students where second_name = 'sapychev')

SELECT * 
from students s2
JOIN st4.marks m on s2.id = m.student_id
JOIN st4.books b on s2.id = b.taken_by_student_id 
JOIN st4.lessons l  on l.id  = m.lesson_id 
JOIN st4.subjets s on s.id = l.subject_id
where s2.second_name = 'sapychev'
