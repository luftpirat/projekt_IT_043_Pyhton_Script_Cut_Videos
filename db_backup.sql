BEGIN TRANSACTION;
CREATE TABLE gruppen (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL
        );
INSERT INTO "gruppen" VALUES(1,'Jonglieren');
INSERT INTO "gruppen" VALUES(2,'Acrobatik');
CREATE TABLE jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            eingabe_datei TEXT NOT NULL,
            eingabe_verzeichnis TEXT NOT NULL,
            ausgabe_datei TEXT NOT NULL,
            startzeit TEXT NOT NULL,
            endzeit TEXT NOT NULL,
            beschreibung TEXT,
            erstellt_am TEXT NOT NULL
        , gruppe TEXT, subgruppe TEXT, untergruppe TEXT);
INSERT INTO "jobs" VALUES(1,'Flat Fronts _ Jongliertrick _ Jonglierkeulen _ Tutorial _ Jonglierversand.de _ Sophia _ Jonglieren.mp4','/mnt/d/Dropbox/Sport/Jonglieren/Tricks/Jonglierversand','flat_front01.mp4','00:01:35','00:01:40','Zwei Keulen: Keulen fliegen von hinten nach vorne durch.','2025-08-22 08:38:13',NULL,NULL,NULL);
INSERT INTO "jobs" VALUES(2,'Flat Fronts _ Jongliertrick _ Jonglierkeulen _ Tutorial _ Jonglierversand.de _ Sophia _ Jonglieren.mp4','/mnt/d/Dropbox/Sport/Jonglieren/Tricks/Jonglierversand','flat_front02_dreiKeulen.mp4','00:02:14','00:02:17','Drei Keulen: Drei Würfe und dann stopp','2025-08-22 08:41:17',NULL,NULL,NULL);
INSERT INTO "jobs" VALUES(3,'Flourish _ Jongliertrick _ Jonglierkeulen _ Tutorial _ Jonglierversand.de _ Sophia _ Jonglieren.mp4','/mnt/d/Dropbox/Sport/Jonglieren/Tricks/Jonglierversand','Flourish_Langsamme_bewegung.mp4','00:01:38','00:01:48','Acht malen. Langsamme Bewegung','2025-08-22 08:54:54',NULL,NULL,NULL);
INSERT INTO "jobs" VALUES(4,'Flourish _ Jongliertrick _ Jonglierkeulen _ Tutorial _ Jonglierversand.de _ Sophia _ Jonglieren.mp4','/mnt/d/Dropbox/Sport/Jonglieren/Tricks/Jonglierversand','Flourish_normale_Bewegung.mp4','00:02:37','00:02:43','Acht malen. Normale Bewegung','2025-08-22 08:56:49',NULL,NULL,NULL);
INSERT INTO "jobs" VALUES(5,'Thumbspin _ Jongliertrick _ Tutorial _ Jonglierversand.de _ Sophia _ Jonglieren _ Keulen.mp4','/mnt/d/Dropbox/Sport/Jonglieren/Tricks/Jonglierversand','Thumbspin01_Drehnung erklärt.mp4','00:01:01','00:01:18','Drehnung erklärt','2025-08-22 09:38:40',NULL,NULL,NULL);
INSERT INTO "jobs" VALUES(6,'Thumbspin _ Jongliertrick _ Tutorial _ Jonglierversand.de _ Sophia _ Jonglieren _ Keulen.mp4','/mnt/d/Dropbox/Sport/Jonglieren/Tricks/Jonglierversand','Thumbspin01_Mehrere Drehungen.mp4','00:01:42','00:02:04','Mehrere Drehnung. Handhaltung ändert sicht. Keulen wird nicht auf der Handfläche gefangen sonder zwischen Zeigefinder und Daumen.','2025-08-22 09:42:46',NULL,NULL,NULL);
INSERT INTO "jobs" VALUES(8,'Learn to juggle BACKCROSSES _ Behind the Back - Advanced Juggling Tutorial.mp4','/mnt/d/Dropbox/Sport/Jonglieren/Tricks/Taylor Tries','Backcrosses01.mp4','00:02:46','00:03:37','Eine Keule. Slow Motion Bewegung.','2025-08-22 09:55:14',NULL,NULL,NULL);
INSERT INTO "jobs" VALUES(10,'Learn to juggle BACKCROSSES _ Behind the Back - Advanced Juggling Tutorial.mp4','/mnt/d/Dropbox/Sport/Jonglieren/Tricks/Taylor Tries','Backcrosses01_ZweiKeulen_ein_Backcross.mp4','00:10:43','00:10:54','Zwei Keulen, ein Backcross. Training Päriferes Sehen. Hohe Kaskade.','2025-08-23 14:25:17',NULL,NULL,NULL);
INSERT INTO "jobs" VALUES(11,'Learn to juggle BACKCROSSES _ Behind the Back - Advanced Juggling Tutorial.mp4','/mnt/d/Dropbox/Sport/Jonglieren/Tricks/Taylor Tries','Backcrosses01_ZweiKeulen_Backcross_Backcross.mp4','00:14:56','00:15:12','Zwei Keulen, Backcross Backcross.','2025-08-23 14:29:54',NULL,NULL,NULL);
INSERT INTO "jobs" VALUES(13,'Learn to juggle BACKCROSSES _ Behind the Back - Advanced Juggling Tutorial.mp4','/mnt/d/Dropbox/Sport/Jonglieren/Tricks/Taylor Tries','04_Backcrosses01_DreiKeulen_Backcross_Backcross_Slomo.mp4','00:18:31','00:18:38','Drei Keulen, Backcross Backcross.  Slomo','2025-08-23 14:34:58',NULL,NULL,NULL);
INSERT INTO "jobs" VALUES(15,'Learn to juggle BACKCROSSES _ Behind the Back - Advanced Juggling Tutorial.mp4','/mnt/d/Dropbox/Sport/Jonglieren/Tricks/Taylor Tries','05_Backcrosses01_DreiKeulen_Drei_Wurfe.mp4','00:19:34','00:19:37','Drei Keulen, Drei Würfe','2025-08-23 14:39:13',NULL,NULL,NULL);
INSERT INTO "jobs" VALUES(16,'Learn to juggle BACKCROSSES _ Behind the Back - Advanced Juggling Tutorial.mp4','/mnt/d/Dropbox/Sport/Jonglieren/Tricks/Taylor Tries','06_Backcrosses01_DreiKeulen_Drei_Wurfe_Slomo_back.mp4','00:19:48','00:20:04','Drei Keule, Solmo, Back','2025-08-23 14:40:06',NULL,NULL,NULL);
INSERT INTO "jobs" VALUES(17,'How to JUGGLE CHOPS with CLUBS and BALLS - Intermediate Juggling Tutorial.mp4','/mnt/d/Dropbox/Sport/Jonglieren/Tricks/Taylor Tries','01_Chops_3 Clubs.mp4','00:05:37','00:05:46','Chops','2025-08-23 14:49:58',NULL,NULL,NULL);
INSERT INTO "jobs" VALUES(18,'02_Learn Reverse Hook-Shot Trap Cascade - Club Class Manipulations - Juggling Tutor.mp4','/mnt/d/Dropbox/Sport/Jonglieren/Club Manipulation/Juggling with Jeremiah - Club Manipulation Tutorials 201','00_trap_cascade.mp4','00:00:02','00:00:10','Trap Cascade','2025-08-24 10:37:10',NULL,NULL,NULL);
INSERT INTO "jobs" VALUES(20,'02_Learn Reverse Hook-Shot Trap Cascade - Club Class Manipulations - Juggling Tutor_Trap.mp4','/mnt/d/Dropbox/Sport/Jonglieren/Club Manipulation/Juggling with Jeremiah - Club Manipulation Tutorials 201/02_Learn Reverse Hook-Shot Trap Cascade - Club Class Manipulations - Juggling Tutor','02_Learn Reverse Hook_step.mp4','00:00:00','00:00:04','Trap Cascade','2025-08-24 17:29:22',NULL,NULL,NULL);
INSERT INTO "jobs" VALUES(21,'Club Balance _ Wie balanciert man eine Jonglierkeule_ _ Jonglierversand.de _ Sophia.mp4','/mnt/d/Dropbox/Sport/Jonglieren/Tricks/Jonglierversand','Club Balance_Kin_01.mp4','00:01:47','00:02:03','Club Balance_Kinn','2025-08-24 19:06:33',NULL,NULL,NULL);
INSERT INTO "jobs" VALUES(22,'Club Balance _ Wie balanciert man eine Jonglierkeule_ _ Jonglierversand.de _ Sophia.mp4','/mnt/d/Dropbox/Sport/Jonglieren/Tricks/Jonglierversand','Club Balance_Nase_01.mp4','00:02:59','00:03:10','Club Balance Nase','2025-08-24 19:08:12',NULL,NULL,NULL);
INSERT INTO "jobs" VALUES(23,'Club Balance _ Wie balanciert man eine Jonglierkeule_ _ Jonglierversand.de _ Sophia.mp4','/mnt/d/Dropbox/Sport/Jonglieren/Tricks/Jonglierversand','Club Balance_Stirn_01.mp4','00:03:34','00:03:46','Club Balance Stirn','2025-08-24 19:09:32',NULL,NULL,NULL);
INSERT INTO "jobs" VALUES(24,'01_Club Spinning_ Fundamental Grips, Crossover & Petals - Club Class Tutorial.mp4','/mnt/d/Dropbox/Sport/Jonglieren/Club Spinning/Juggling with Jeremiah - Club Spinning Tutorials for Beginners','01_Spinning_two_clubs_alter.mp4','00:04:58','00:05:08','01_Spinning_two_clubs alter','2025-08-24 19:49:23','Jonglieren',NULL,'Trick');
INSERT INTO "jobs" VALUES(25,'Jongliertrick _ Columns Jonglierkeulen _ Tutorial _ Jonglierversand.de _ Sophia _ Säulen.mp4','/mnt/d/Dropbox/Sport/Jonglieren/Tricks/Jonglierversand','Columns_seitlich_01.mp4','00:02:15','00:02:21','Columns_seitlich','2025-08-24 19:51:03',NULL,NULL,NULL);
INSERT INTO "jobs" VALUES(26,'09_Learn Clubslinger - Club Manipulation Technique - #juggling #malabarismo #flowarts #tutorial.mp4','/mnt/d/Dropbox/Sport/Jonglieren/Club Manipulation/Juggling with Jeremiah - Club Manipulation Tutorials 201','Clubslinger Step1.mp4','00:00:36','00:00:41','Clubslinger Step1','2025-08-24 20:26:47',NULL,NULL,NULL);
INSERT INTO "jobs" VALUES(27,'09_Learn Clubslinger - Club Manipulation Technique - #juggling #malabarismo #flowarts #tutorial.mp4','/mnt/d/Dropbox/Sport/Jonglieren/Club Manipulation/Juggling with Jeremiah - Club Manipulation Tutorials 201','Clubslinger Step2.mp4','00:00:47','00:00:50','Clubslinger Step2','2025-08-24 20:28:36',NULL,NULL,NULL);
INSERT INTO "jobs" VALUES(28,'09_Learn Clubslinger - Club Manipulation Technique - #juggling #malabarismo #flowarts #tutorial.mp4','/mnt/d/Dropbox/Sport/Jonglieren/Club Manipulation/Juggling with Jeremiah - Club Manipulation Tutorials 201','Clubslinger Step3 Final.mp4','00:01:00','00:01:06','Clubslinger Step3 Final','2025-08-24 20:30:26',NULL,NULL,NULL);
INSERT INTO "jobs" VALUES(29,'01_Club Spinning_ Fundamental Grips, Crossover & Petals - Club Class Tutorial.mp4','/mnt/d/Dropbox/Sport/Jonglieren/Club Spinning/Juggling with Jeremiah - Club Spinning Tutorials for Beginners','01_Spinning_inside.mp4','00:01:52','00:01:57','01_Spinning_inside','2025-08-28 15:49:28',NULL,NULL,NULL);
INSERT INTO "jobs" VALUES(30,'01_Club Spinning_ Fundamental Grips, Crossover & Petals - Club Class Tutorial.mp4','/mnt/d/Dropbox/Sport/Jonglieren/Club Spinning/Juggling with Jeremiah - Club Spinning Tutorials for Beginners','01_Spinning_two_clubs.mp4','00:04:45','00:04:57','01_Spinning_two_clubs','2025-08-28 15:55:32',NULL,NULL,NULL);
INSERT INTO "jobs" VALUES(31,'01_Club Spinning_ Fundamental Grips, Crossover & Petals - Club Class Tutorial.mp4','/mnt/d/Dropbox/Sport/Jonglieren/Club Spinning/Juggling with Jeremiah - Club Spinning Tutorials for Beginners','01_Spinning_two_clubs_alter.mp4','00:04:58','00:05:08','01_Spinning_two_clubs alter','2025-08-28 15:59:28','Jonglieren',NULL,'Spinning');
INSERT INTO "jobs" VALUES(33,'Ninja Star & Cartwheel AcroYoga Tutorial (deutsch _ english subtitled).mp4','/mnt/d/Dropbox/Sport/Acro/Washing Machines/Ninja Star','01_Ninja Star Side Star aufnehmen.mp4','00:04:17','00:04:22','01_Ninja Star Side Star aufnehmen','2025-08-28 17:53:19','Acrobatik',NULL,'Waschmaschine');
INSERT INTO "jobs" VALUES(35,'Ninja Star & Cartwheel AcroYoga Tutorial (deutsch _ english subtitled).mp4','/mnt/d/Dropbox/Sport/Acro/Washing Machines/Ninja Star','01_Ninja Star Side Star Budda.mp4','00:04:28','00:04:42','01_Ninja Star Side Star to Budda','2025-08-28 19:03:20','Acrobatik',NULL,'Waschmaschine');
INSERT INTO "jobs" VALUES(36,'Ninja Star & Cartwheel AcroYoga Tutorial (deutsch _ english subtitled).mp4','/mnt/d/Dropbox/Sport/Acro/Washing Machines/Ninja Star','03_Budda_Side Star.mp4','00:06:34','00:06:43','03_Budda_Side Star','2025-08-28 19:32:38','Acrobatik',NULL,'Waschmaschine');
INSERT INTO "jobs" VALUES(37,'Ninja Star & Cartwheel AcroYoga Tutorial (deutsch _ english subtitled).mp4','/mnt/d/Dropbox/Sport/Acro/Washing Machines/Ninja Star','05_Side Star Reverse Bird.mp4','00:06:56','00:07:16','05_Side Star Reverse Bird','2025-08-28 19:34:15','Acrobatik',NULL,'Waschmaschine');
INSERT INTO "jobs" VALUES(38,'Ninja Star & Cartwheel AcroYoga Tutorial (deutsch _ english subtitled).mp4','/mnt/d/Dropbox/Sport/Acro/Washing Machines/Ninja Star','06_Reverse Bird Side Star.mp4','00:07:29','00:07:38','06_Reverse Bird Side Star','2025-08-28 19:36:41','Acrobatik',NULL,'Waschmaschine');
INSERT INTO "jobs" VALUES(39,'Ninja Star & Cartwheel AcroYoga Tutorial (deutsch _ english subtitled).mp4','/mnt/d/Dropbox/Sport/Acro/Washing Machines/Ninja Star','07 Side Star to Budda.mp4','00:07:55','00:08:00','07 Side Star to Budda','2025-08-28 19:38:04','Acrobatik',NULL,'Waschmaschine');
INSERT INTO "jobs" VALUES(40,'Ninja Star & Cartwheel AcroYoga Tutorial (deutsch _ english subtitled).mp4','/mnt/d/Dropbox/Sport/Acro/Washing Machines/Ninja Star','08 ganzer flow.mp4','00:09:00','00:09:32','08 ganzer flow','2025-08-28 19:40:28','Acrobatik',NULL,'Waschmaschine');
CREATE TABLE untergruppen (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            gruppe_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            FOREIGN KEY(gruppe_id) REFERENCES gruppen(id)
        );
INSERT INTO "untergruppen" VALUES(1,1,'Manipulation');
INSERT INTO "untergruppen" VALUES(2,1,'Spinning');
INSERT INTO "untergruppen" VALUES(3,2,'Waschmaschine');
INSERT INTO "untergruppen" VALUES(4,2,'Grundübung');
INSERT INTO "untergruppen" VALUES(5,1,'Trick');
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('jobs',42);
INSERT INTO "sqlite_sequence" VALUES('gruppen',2);
INSERT INTO "sqlite_sequence" VALUES('untergruppen',5);
COMMIT;
