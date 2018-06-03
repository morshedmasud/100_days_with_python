DELETE FROM addresses;
DELETE FROM users;

INSERT INTO users(first_name, last_name) VALUES ("Masud", "Morshed");
INSERT INTO users(first_name, last_name) VALUES ("Nasir", "Uddin");
INSERT INTO users(first_name, last_name) VALUES ("Giash", "Uddin");
INSERT INTO users(first_name, last_name) VALUES ("Tamim", "Iqbal");
INSERT INTO users(first_name, last_name) VALUES ("Ariful", "Hasan");

INSERT INTO addresses(user_id, email, address) VALUES (11, "masud@gmail.gamil.com", "BD");
INSERT INTO addresses(user_id, email, address) VALUES (21, "nasir@gmail.gamil.com", "Id");
INSERT INTO addresses(user_id, email, address) VALUES (31, "giash@gmail.gamil.com", "US");
INSERT INTO addresses(user_id, email, address) VALUES (41, "tamim@gmail.gamil.com", "Pak");
INSERT INTO addresses(user_id, email, address) VALUES (51, "arif@gmail.gamil.com", "Rs");
