drop table projet ;
drop table user ;

CREATE TABLE projet (id integer not null primary key autoincrement,
                        nom TEXT,
                        langage TEXT,
                        code TEXT);

CREATE TABLE user (id integer not null primary key autoincrement,
                        ip_adresse TEXT,
                        navigateur TEXT,
                        date_heure TIMESTAMP);