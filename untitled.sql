ALTER TABLE `implementation_person	` DROP FOREIGN KEY FKimplementa605874;
ALTER TABLE `implementation_person	` DROP FOREIGN KEY FKimplementa594814;
ALTER TABLE room_implementation DROP FOREIGN KEY FKroom_imple506436;
ALTER TABLE room_implementation DROP FOREIGN KEY FKroom_imple977683;
ALTER TABLE implementation_subgroup DROP FOREIGN KEY FKimplementa408881;
ALTER TABLE implementation_subgroup DROP FOREIGN KEY FKimplementa380177;
ALTER TABLE `person	_degreeprogram` DROP FOREIGN KEY `FKperson	_de160513`;
ALTER TABLE `person	_degreeprogram` DROP FOREIGN KEY `FKperson	_de123455`;
ALTER TABLE course DROP FOREIGN KEY FKcourse108073;
ALTER TABLE implementation DROP FOREIGN KEY FKimplementa589065;
ALTER TABLE subgroup DROP FOREIGN KEY FKsubgroup112378;
ALTER TABLE curriculum DROP FOREIGN KEY FKcurriculum190929;
DROP TABLE IF EXISTS course;
DROP TABLE IF EXISTS person;
DROP TABLE IF EXISTS degreeprogram;
DROP TABLE IF EXISTS room;
DROP TABLE IF EXISTS curriculum;
DROP TABLE IF EXISTS implementation;
DROP TABLE IF EXISTS subgroup;
DROP TABLE IF EXISTS implementation_person;
DROP TABLE IF EXISTS room_implementation;
DROP TABLE IF EXISTS implementation_subgroup;
DROP TABLE IF EXISTS `person	_degreeprogram`;
CREATE TABLE course (id int(11) NOT NULL AUTO_INCREMENT, Code varchar(20), Name varchar(20), Changes varchar(50), Languages varchar(50), Credit int(11), `Size` int(11), P1 int(11), P2 int(11), P3 int(11), P4 int(11), P5 int(11), Total int(11), curriculumid int(10) NOT NULL, PRIMARY KEY (id), UNIQUE INDEX (id), INDEX (Code)) CHARACTER SET UTF8;
CREATE TABLE person (id int(11) NOT NULL AUTO_INCREMENT, Code varchar(7) NOT NULL UNIQUE, Name varchar(50) NOT NULL UNIQUE, PRIMARY KEY (id), UNIQUE INDEX (id)) CHARACTER SET UTF8;
CREATE TABLE degreeprogram (id int(11) NOT NULL AUTO_INCREMENT, Code varchar(10) NOT NULL, Name varchar(50), PRIMARY KEY (id), UNIQUE INDEX (id), UNIQUE INDEX (Code)) CHARACTER SET UTF8;
CREATE TABLE room (id int(11) NOT NULL AUTO_INCREMENT, Code varchar(50) NOT NULL, Seats int(10), Topic varchar(50), PRIMARY KEY (id), UNIQUE INDEX (id), UNIQUE INDEX (Code)) CHARACTER SET UTF8;
CREATE TABLE curriculum (id int(10) NOT NULL AUTO_INCREMENT, Name varchar(30), degreeprogramid int(11) NOT NULL, PRIMARY KEY (id), UNIQUE INDEX (id)) CHARACTER SET UTF8;
CREATE TABLE implementation (id int(11) NOT NULL AUTO_INCREMENT, courseid int(11) NOT NULL, PRIMARY KEY (id), UNIQUE INDEX (id)) CHARACTER SET UTF8;
CREATE TABLE subgroup (id int(11) NOT NULL AUTO_INCREMENT, Code varchar(20) NOT NULL, Department varchar(30) NOT NULL, degreeprogramid int(11) NOT NULL, PRIMARY KEY (id), UNIQUE INDEX (id), UNIQUE INDEX (Code)) CHARACTER SET UTF8;
CREATE TABLE implementation_person (implementationid int(11) NOT NULL, `person	id` int(11) NOT NULL, PRIMARY KEY (implementationid, `person	id`)) CHARACTER SET UTF8;
CREATE TABLE room_implementation (roomid int(11) NOT NULL, implementationid int(11) NOT NULL, PRIMARY KEY (roomid, implementationid)) CHARACTER SET UTF8;
CREATE TABLE implementation_subgroup (implementationid int(11) NOT NULL, subgroupid int(11) NOT NULL, PRIMARY KEY (implementationid, subgroupid)) CHARACTER SET UTF8;
CREATE TABLE `person	_degreeprogram` (`person	id` int(11) NOT NULL, degreeprogramid int(11) NOT NULL, PRIMARY KEY (`person	id`, degreeprogramid)) CHARACTER SET UTF8;
ALTER TABLE `implementation_person	` ADD INDEX FKimplementa605874 (implementationid), ADD CONSTRAINT FKimplementa605874 FOREIGN KEY (implementationid) REFERENCES implementation (id);
ALTER TABLE `implementation_person	` ADD INDEX FKimplementa594814 (`person	id`), ADD CONSTRAINT FKimplementa594814 FOREIGN KEY (`person	id`) REFERENCES `person	` (id);
ALTER TABLE room_implementation ADD INDEX FKroom_imple506436 (roomid), ADD CONSTRAINT FKroom_imple506436 FOREIGN KEY (roomid) REFERENCES room (id);
ALTER TABLE room_implementation ADD INDEX FKroom_imple977683 (implementationid), ADD CONSTRAINT FKroom_imple977683 FOREIGN KEY (implementationid) REFERENCES implementation (id);
ALTER TABLE implementation_subgroup ADD INDEX FKimplementa408881 (implementationid), ADD CONSTRAINT FKimplementa408881 FOREIGN KEY (implementationid) REFERENCES implementation (id);
ALTER TABLE implementation_subgroup ADD INDEX FKimplementa380177 (subgroupid), ADD CONSTRAINT FKimplementa380177 FOREIGN KEY (subgroupid) REFERENCES subgroup (id);
ALTER TABLE `person	_degreeprogram` ADD INDEX `FKperson	_de160513` (`person	id`), ADD CONSTRAINT `FKperson	_de160513` FOREIGN KEY (`person	id`) REFERENCES `person	` (id);
ALTER TABLE `person	_degreeprogram` ADD INDEX `FKperson	_de123455` (degreeprogramid), ADD CONSTRAINT `FKperson	_de123455` FOREIGN KEY (degreeprogramid) REFERENCES degreeprogram (id);
ALTER TABLE course ADD INDEX FKcourse108073 (curriculumid), ADD CONSTRAINT FKcourse108073 FOREIGN KEY (curriculumid) REFERENCES curriculum (id);
ALTER TABLE implementation ADD INDEX FKimplementa589065 (courseid), ADD CONSTRAINT FKimplementa589065 FOREIGN KEY (courseid) REFERENCES course (id);
ALTER TABLE subgroup ADD INDEX FKsubgroup112378 (degreeprogramid), ADD CONSTRAINT FKsubgroup112378 FOREIGN KEY (degreeprogramid) REFERENCES degreeprogram (id);
ALTER TABLE curriculum ADD INDEX FKcurriculum190929 (degreeprogramid), ADD CONSTRAINT FKcurriculum190929 FOREIGN KEY (degreeprogramid) REFERENCES degreeprogram (id);
