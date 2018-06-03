DELETE FROM addresses;
DELETE FROM users;

INSERT INTO users(first_name, last_name) VALUES ("Masud", "Morshed");
INSERT INTO users(first_name, last_name) VALUES ("Nasir", "Uddin");
INSERT INTO users(first_name, last_name) VALUES ("Giash", "Uddin");
INSERT INTO users(first_name, last_name) VALUES ("Tamim", "Iqbal");
INSERT INTO users(first_name, last_name) VALUES ("Ariful", "Hasan");

INSERT INTO addresses(user_id, email, address) VALUES (101, "masud@gmail.gamil.com", "Bangladesh");
INSERT INTO addresses(user_id, email, address) VALUES (102, "nasir@gmail.gamil.com", "India");
INSERT INTO addresses(user_id, email, address) VALUES (103, "giash@gmail.gamil.com", "United State");
INSERT INTO addresses(user_id, email, address) VALUES (104, "tamim@gmail.gamil.com", "Pakistan");
INSERT INTO addresses(user_id, email, address) VALUES (105, "arif@gmail.gamil.com", "Russia");
