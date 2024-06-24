BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "django_migrations" (
	"id"	integer NOT NULL,
	"app"	varchar(255) NOT NULL,
	"name"	varchar(255) NOT NULL,
	"applied"	datetime NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_group_permissions" (
	"id"	integer NOT NULL,
	"group_id"	integer NOT NULL,
	"permission_id"	integer NOT NULL,
	FOREIGN KEY("group_id") REFERENCES "auth_group"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("permission_id") REFERENCES "auth_permission"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_user_groups" (
	"id"	integer NOT NULL,
	"user_id"	integer NOT NULL,
	"group_id"	integer NOT NULL,
	FOREIGN KEY("group_id") REFERENCES "auth_group"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_user_user_permissions" (
	"id"	integer NOT NULL,
	"user_id"	integer NOT NULL,
	"permission_id"	integer NOT NULL,
	FOREIGN KEY("permission_id") REFERENCES "auth_permission"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "django_admin_log" (
	"id"	integer NOT NULL,
	"object_id"	text,
	"object_repr"	varchar(200) NOT NULL,
	"action_flag"	smallint unsigned NOT NULL CHECK("action_flag" >= 0),
	"change_message"	text NOT NULL,
	"content_type_id"	integer,
	"user_id"	integer NOT NULL,
	"action_time"	datetime NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("content_type_id") REFERENCES "django_content_type"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "django_content_type" (
	"id"	integer NOT NULL,
	"app_label"	varchar(100) NOT NULL,
	"model"	varchar(100) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_permission" (
	"id"	integer NOT NULL,
	"content_type_id"	integer NOT NULL,
	"codename"	varchar(100) NOT NULL,
	"name"	varchar(255) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("content_type_id") REFERENCES "django_content_type"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "auth_group" (
	"id"	integer NOT NULL,
	"name"	varchar(150) NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_user" (
	"id"	integer NOT NULL,
	"password"	varchar(128) NOT NULL,
	"last_login"	datetime,
	"is_superuser"	bool NOT NULL,
	"username"	varchar(150) NOT NULL UNIQUE,
	"last_name"	varchar(150) NOT NULL,
	"email"	varchar(254) NOT NULL,
	"is_staff"	bool NOT NULL,
	"is_active"	bool NOT NULL,
	"date_joined"	datetime NOT NULL,
	"first_name"	varchar(150) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "django_session" (
	"session_key"	varchar(40) NOT NULL,
	"session_data"	text NOT NULL,
	"expire_date"	datetime NOT NULL,
	PRIMARY KEY("session_key")
);
CREATE TABLE IF NOT EXISTS "employee_employee" (
	"employee_code"	integer NOT NULL UNIQUE,
	"id"	integer NOT NULL,
	"employee_name"	varchar(50) NOT NULL,
	"employee_national_id"	integer NOT NULL,
	"birth_date"	date NOT NULL,
	"employee_phone_1"	integer NOT NULL,
	"employee_phone_2"	integer,
	"governorate"	varchar(25) NOT NULL,
	"employee_email"	varchar(50) NOT NULL,
	"image"	varchar(100),
	"slug"	varchar(50),
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "ticket_new_ticket" (
	"id"	integer NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "ticket_it" (
	"id"	integer NOT NULL,
	"it_name"	varchar(25) NOT NULL,
	"it_id"	integer NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "ticket_ticket" (
	"ticket_code"	integer NOT NULL UNIQUE,
	"ticket_id"	integer NOT NULL,
	"title"	varchar(200) NOT NULL,
	"description"	text NOT NULL,
	"start_date"	datetime NOT NULL,
	"due_date"	datetime,
	"comment"	text,
	"status"	varchar(20) NOT NULL,
	"assigned_to_id"	bigint NOT NULL,
	"requested_by_id"	bigint NOT NULL,
	"slug"	varchar(50),
	PRIMARY KEY("ticket_id" AUTOINCREMENT),
	FOREIGN KEY("requested_by_id") REFERENCES "employee_employee"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("assigned_to_id") REFERENCES "ticket_it"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "device_device" (
	"device_code"	integer NOT NULL UNIQUE,
	"id"	integer NOT NULL,
	"device_type"	varchar(15) NOT NULL,
	"model_name"	varchar(50) NOT NULL,
	"motherboard"	varchar(50),
	"cpu"	varchar(50),
	"ram"	varchar(50),
	"hdd"	varchar(50),
	"date"	datetime NOT NULL,
	"status"	varchar(50) NOT NULL,
	"sites"	varchar(50) NOT NULL,
	"other"	text NOT NULL,
	"slug"	varchar(50),
	"price"	decimal NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
INSERT INTO "django_migrations" ("id","app","name","applied") VALUES (1,'contenttypes','0001_initial','2023-12-11 14:41:16.097527'),
 (2,'auth','0001_initial','2023-12-11 14:41:16.121785'),
 (3,'admin','0001_initial','2023-12-11 14:41:16.143230'),
 (4,'admin','0002_logentry_remove_auto_add','2023-12-11 14:41:16.167448'),
 (5,'admin','0003_logentry_add_action_flag_choices','2023-12-11 14:41:16.181955'),
 (6,'contenttypes','0002_remove_content_type_name','2023-12-11 14:41:16.211953'),
 (7,'auth','0002_alter_permission_name_max_length','2023-12-11 14:41:16.231947'),
 (8,'auth','0003_alter_user_email_max_length','2023-12-11 14:41:16.250732'),
 (9,'auth','0004_alter_user_username_opts','2023-12-11 14:41:16.268072'),
 (10,'auth','0005_alter_user_last_login_null','2023-12-11 14:41:16.287247'),
 (11,'auth','0006_require_contenttypes_0002','2023-12-11 14:41:16.296729'),
 (12,'auth','0007_alter_validators_add_error_messages','2023-12-11 14:41:16.311733'),
 (13,'auth','0008_alter_user_username_max_length','2023-12-11 14:41:16.331728'),
 (14,'auth','0009_alter_user_last_name_max_length','2023-12-11 14:41:16.351733'),
 (15,'auth','0010_alter_group_name_max_length','2023-12-11 14:41:16.366723'),
 (16,'auth','0011_update_proxy_permissions','2023-12-11 14:41:16.381721'),
 (17,'auth','0012_alter_user_first_name_max_length','2023-12-11 14:41:16.401913'),
 (18,'sessions','0001_initial','2023-12-11 14:41:16.417322'),
 (19,'device','0001_initial','2023-12-11 21:34:36.808794'),
 (20,'device','0002_alter_device_other','2023-12-11 21:39:43.040921'),
 (21,'device','0002_alter_device_device_code','2023-12-11 21:51:09.097954'),
 (22,'device','0003_alter_device_date_alter_device_price','2023-12-12 11:39:10.025227'),
 (23,'device','0004_alter_device_model_name','2023-12-12 11:44:05.869599'),
 (24,'device','0005_alter_device_price','2023-12-12 11:46:45.653040'),
 (25,'device','0006_alter_device_price','2023-12-12 11:48:41.236845'),
 (26,'device','0007_alter_device_price','2023-12-12 11:51:29.222111'),
 (27,'employee','0001_initial','2023-12-14 08:34:43.576527'),
 (28,'employee','0002_alter_employee_employee_national_id','2023-12-14 08:34:43.591529'),
 (29,'employee','0003_alter_employee_employee_phone_1_and_more','2023-12-14 08:34:43.613366'),
 (30,'employee','0004_employee_image','2023-12-14 08:44:33.368840'),
 (31,'employee','0005_alter_employee_employee_phone_2_alter_employee_image','2023-12-14 09:31:04.913929'),
 (32,'employee','0006_alter_employee_image','2023-12-14 09:40:27.815057'),
 (33,'employee','0007_alter_employee_employee_phone_2_alter_employee_image','2023-12-14 09:43:44.493781'),
 (34,'employee','0008_alter_employee_image','2023-12-14 09:44:55.706970'),
 (35,'employee','0009_alter_employee_image','2023-12-14 09:50:36.037335'),
 (36,'employee','0010_alter_employee_image','2023-12-14 10:22:20.893197'),
 (37,'device','0008_device_slug','2023-12-18 11:19:05.554369'),
 (38,'employee','0011_employee_slug','2023-12-18 12:07:20.155920'),
 (39,'ticket','0001_initial','2024-06-08 19:23:25.048870'),
 (40,'ticket','0002_ticket_requested_by','2024-06-08 19:31:39.991274'),
 (41,'ticket','0003_ticket_slug','2024-06-09 13:02:47.268154'),
 (42,'ticket','0004_ticket_ticket_code','2024-06-09 13:06:12.264750'),
 (43,'employee','0012_alter_employee_employee_code','2024-06-11 20:24:42.024683'),
 (44,'ticket','0005_new_ticket','2024-06-11 20:24:42.039680'),
 (45,'device','0009_alter_device_device_code','2024-06-11 20:26:28.449455'),
 (46,'ticket','0006_alter_it_it_id_alter_ticket_ticket_code','2024-06-11 20:26:28.479457'),
 (47,'device','0010_alter_device_cpu_alter_device_hdd_and_more','2024-06-12 07:32:09.435012'),
 (48,'device','0011_alter_device_price','2024-06-12 07:38:14.877762'),
 (49,'device','0012_alter_device_price','2024-06-12 07:41:43.341140'),
 (50,'device','0013_alter_device_price','2024-06-12 07:52:30.989540');
INSERT INTO "django_admin_log" ("id","object_id","object_repr","action_flag","change_message","content_type_id","user_id","action_time") VALUES (1,'1','admin',2,'[{"changed": {"fields": ["First name", "Last name"]}}]',4,1,'2023-12-11 14:46:05.642779'),
 (2,'1','HP Elit Book 85 8570p',1,'[{"added": {}}]',7,1,'2023-12-12 11:51:47.592414'),
 (3,'1','Ahmed Shafey',1,'[{"added": {}}]',8,1,'2023-12-14 08:35:08.162668'),
 (4,'2','Ahmed Mohamed',1,'[{"added": {}}]',8,1,'2023-12-14 09:40:39.233859'),
 (5,'1','Ahmed Shafey',2,'[{"changed": {"fields": ["Image"]}}]',8,1,'2023-12-14 09:49:07.607206'),
 (6,'2','Ahmed Mohamed',2,'[{"changed": {"fields": ["Image"]}}]',8,1,'2023-12-14 09:49:15.113839'),
 (7,'1','Ahmed Shafey',2,'[{"changed": {"fields": ["Image"]}}]',8,1,'2023-12-14 09:50:59.667976'),
 (8,'2','Ahmed Mohamed',2,'[{"changed": {"fields": ["Image"]}}]',8,1,'2023-12-14 09:51:06.490324'),
 (9,'1','Ahmed Shafey',2,'[{"changed": {"fields": ["Image"]}}]',8,1,'2023-12-14 10:22:39.586016'),
 (10,'1','Ahmed Shafey',2,'[{"changed": {"fields": ["Image"]}}]',8,1,'2023-12-14 10:23:20.132728'),
 (11,'2','Ahmed Mohamed',2,'[{"changed": {"fields": ["Image"]}}]',8,1,'2023-12-14 10:23:27.626783'),
 (12,'1','Ahmed Shafey',2,'[{"changed": {"fields": ["Governorate"]}}]',8,1,'2023-12-16 15:47:56.958286'),
 (13,'2','Dell Latitude E6530',1,'[{"added": {}}]',7,1,'2023-12-17 10:49:29.897237'),
 (14,'2','Dell Latitude E6530',2,'[]',7,1,'2023-12-18 11:28:36.205902'),
 (15,'1','HP Elit Book 85 8570p',2,'[]',7,1,'2023-12-18 11:28:45.735522'),
 (16,'2','Ahmed Mohamed',2,'[]',8,1,'2023-12-18 12:18:57.299699'),
 (17,'1','Ahmed Shafey',2,'[]',8,1,'2023-12-18 12:19:09.494547'),
 (18,'1','admin',2,'[]',4,2,'2024-06-04 10:53:31.368689'),
 (19,'1','Ahmed Shafey',2,'[]',8,1,'2024-06-09 12:41:54.225001'),
 (20,'1','Shafey',1,'[{"added": {}}]',10,1,'2024-06-09 12:44:19.777194'),
 (21,'1','Windows Error',1,'[{"added": {}}]',9,1,'2024-06-09 12:45:01.093504'),
 (22,'2','Mail Error',1,'[{"added": {}}]',9,1,'2024-06-09 12:48:44.538200'),
 (23,'2','Mail Error',2,'[{"changed": {"fields": ["Slug"]}}]',9,1,'2024-06-09 13:08:17.741306'),
 (24,'2','Mail Error',2,'[]',9,1,'2024-06-09 13:08:22.848707'),
 (25,'2','Mail Error',2,'[{"changed": {"fields": ["Ticket code", "Slug"]}}]',9,1,'2024-06-09 13:10:48.468510'),
 (26,'2','Mail Error',2,'[]',9,1,'2024-06-10 10:01:37.743086'),
 (27,'1','Windows Error',2,'[{"changed": {"fields": ["Ticket code"]}}]',9,1,'2024-06-10 10:01:46.751085'),
 (28,'3','Activation',1,'[{"added": {}}]',9,1,'2024-06-10 20:24:32.130705'),
 (29,'4','Internet Error',1,'[{"added": {}}]',9,1,'2024-06-10 20:25:20.227777'),
 (30,'5','app hang',1,'[{"added": {}}]',9,1,'2024-06-10 20:25:58.308863'),
 (31,'4','Internet Error',2,'[{"changed": {"fields": ["Ticket code"]}}]',9,1,'2024-06-10 20:26:20.876885'),
 (32,'6','share Error',1,'[{"added": {}}]',9,1,'2024-06-10 20:27:13.380415'),
 (33,'7','cameras not respond',1,'[{"added": {}}]',9,1,'2024-06-10 20:28:32.758513'),
 (34,'5','Ahmed Shafey 22',3,'',8,1,'2024-06-11 20:15:22.342748'),
 (35,'4','Ahmed Shafey 22',3,'',8,1,'2024-06-11 20:15:22.351888');
INSERT INTO "django_content_type" ("id","app_label","model") VALUES (1,'admin','logentry'),
 (2,'auth','permission'),
 (3,'auth','group'),
 (4,'auth','user'),
 (5,'contenttypes','contenttype'),
 (6,'sessions','session'),
 (7,'device','device'),
 (8,'employee','employee'),
 (9,'ticket','ticket'),
 (10,'ticket','it'),
 (11,'ticket','it_group'),
 (12,'ticket','new_ticket');
INSERT INTO "auth_permission" ("id","content_type_id","codename","name") VALUES (1,1,'add_logentry','Can add log entry'),
 (2,1,'change_logentry','Can change log entry'),
 (3,1,'delete_logentry','Can delete log entry'),
 (4,1,'view_logentry','Can view log entry'),
 (5,2,'add_permission','Can add permission'),
 (6,2,'change_permission','Can change permission'),
 (7,2,'delete_permission','Can delete permission'),
 (8,2,'view_permission','Can view permission'),
 (9,3,'add_group','Can add group'),
 (10,3,'change_group','Can change group'),
 (11,3,'delete_group','Can delete group'),
 (12,3,'view_group','Can view group'),
 (13,4,'add_user','Can add user'),
 (14,4,'change_user','Can change user'),
 (15,4,'delete_user','Can delete user'),
 (16,4,'view_user','Can view user'),
 (17,5,'add_contenttype','Can add content type'),
 (18,5,'change_contenttype','Can change content type'),
 (19,5,'delete_contenttype','Can delete content type'),
 (20,5,'view_contenttype','Can view content type'),
 (21,6,'add_session','Can add session'),
 (22,6,'change_session','Can change session'),
 (23,6,'delete_session','Can delete session'),
 (24,6,'view_session','Can view session'),
 (25,7,'add_device','Can add device'),
 (26,7,'change_device','Can change device'),
 (27,7,'delete_device','Can delete device'),
 (28,7,'view_device','Can view device'),
 (29,8,'add_employee','Can add employee'),
 (30,8,'change_employee','Can change employee'),
 (31,8,'delete_employee','Can delete employee'),
 (32,8,'view_employee','Can view employee'),
 (33,9,'add_ticket','Can add ticket'),
 (34,9,'change_ticket','Can change ticket'),
 (35,9,'delete_ticket','Can delete ticket'),
 (36,9,'view_ticket','Can view ticket'),
 (37,10,'add_it','Can add it'),
 (38,10,'change_it','Can change it'),
 (39,10,'delete_it','Can delete it'),
 (40,10,'view_it','Can view it'),
 (41,12,'add_new_ticket','Can add new_ ticket'),
 (42,12,'change_new_ticket','Can change new_ ticket'),
 (43,12,'delete_new_ticket','Can delete new_ ticket'),
 (44,12,'view_new_ticket','Can view new_ ticket');
INSERT INTO "auth_user" ("id","password","last_login","is_superuser","username","last_name","email","is_staff","is_active","date_joined","first_name") VALUES (1,'pbkdf2_sha256$720000$rVRGdRMbNnkiSDU8X94eFF$S4/oR0+De+aUfaHXF9iRrK8G/l0A20hH/+3ExRDZ5aE=','2024-06-11 19:30:18.645471',1,'admin','IT','admin@ecipegypt.com',1,1,'2023-12-11 14:44:16','Ahmed'),
 (2,'pbkdf2_sha256$720000$M0jbDJSwEVdpGOYzaTzAkT$ISWs8A0ps65EA+1XkJuNl3BfLzWrtV0IfoxaK6ehC+o=','2024-06-04 10:52:05.792189',1,'shafey','','shafeyvip@gmail.com',1,1,'2024-06-04 10:51:22.313142','');
INSERT INTO "django_session" ("session_key","session_data","expire_date") VALUES ('421nre4pqqthkadfsd7rzbd07ybf2nut','.eJxVjMsOwiAQRf-FtSEwPAou3fsNZBhAqgaS0q6M_65NutDtPefcFwu4rTVsIy9hTuzMJDv9bhHpkdsO0h3brXPqbV3myHeFH3Twa0_5eTncv4OKo37riUCCNMIToRPRWKmst4VQey1QJW11Lo6UnFSyETA5UQgKyGjAECj2_gDIrTda:1rChWS:axvg7KrpiHGDLdGvW1xzlnoZgDpIraFhBrr2yq557Hs','2023-12-25 14:44:40.434476'),
 ('ik43n99lh9jg4vddk28dbfrng8wrvn4g','.eJxVjMsOwiAQRf-FtSEwPAou3fsNZBhAqgaS0q6M_65NutDtPefcFwu4rTVsIy9hTuzMJDv9bhHpkdsO0h3brXPqbV3myHeFH3Twa0_5eTncv4OKo37riUCCNMIToRPRWKmst4VQey1QJW11Lo6UnFSyETA5UQgKyGjAECj2_gDIrTda:1rJJOz:5fsMGCHSy9Jb3br0tiFE4aSS-L7Q0D9gNKnJV994l8I','2024-01-12 20:24:17.596235'),
 ('3uw3p7l3666fsq14rmownnhe61kjkqg7','.eJxVjMsOwiAQRf-FtSEwPAou3fsNZBhAqgaS0q6M_65NutDtPefcFwu4rTVsIy9hTuzMJDv9bhHpkdsO0h3brXPqbV3myHeFH3Twa0_5eTncv4OKo37riUCCNMIToRPRWKmst4VQey1QJW11Lo6UnFSyETA5UQgKyGjAECj2_gDIrTda:1rJwhV:J_MEijNRZQbBgd6nVggMFfc52TLhtUo6yA_avHCMb58','2024-01-14 14:22:01.956276'),
 ('0topn2o9pf7en4flarjhljrzte56yqf9','.eJxVjMsOwiAQRf-FtSEwPAou3fsNZBhAqgaS0q6M_65NutDtPefcFwu4rTVsIy9hTuzMJDv9bhHpkdsO0h3brXPqbV3myHeFH3Twa0_5eTncv4OKo37riUCCNMIToRPRWKmst4VQey1QJW11Lo6UnFSyETA5UQgKyGjAECj2_gDIrTda:1sFpqv:TC0_PLGjQB0HTW9txex6rjJWV75qUfoPi3uKNJIN-5Q','2024-06-22 06:47:01.301836'),
 ('01g67l43oj8qswsdsbqim5kftgsu77de','.eJxVjMsOwiAQRf-FtSEwPAou3fsNZBhAqgaS0q6M_65NutDtPefcFwu4rTVsIy9hTuzMJDv9bhHpkdsO0h3brXPqbV3myHeFH3Twa0_5eTncv4OKo37riUCCNMIToRPRWKmst4VQey1QJW11Lo6UnFSyETA5UQgKyGjAECj2_gDIrTda:1sG1dl:XWTLr-pij7I1Yg1k3NGUdBVvCELUz_QJ8WJNI_gjR2c','2024-06-22 19:22:13.403791'),
 ('asv6n6s0naxwhbs9ovqrfz5x5zwvuc57','.eJxVjMsOwiAQRf-FtSEwPAou3fsNZBhAqgaS0q6M_65NutDtPefcFwu4rTVsIy9hTuzMJDv9bhHpkdsO0h3brXPqbV3myHeFH3Twa0_5eTncv4OKo37riUCCNMIToRPRWKmst4VQey1QJW11Lo6UnFSyETA5UQgKyGjAECj2_gDIrTda:1sGCiI:oDRFqyFOkOqYxUEq-dzbm3FUL4zMdt6FPXQcOFe3abc','2024-06-23 07:11:38.411354'),
 ('3ovo3b6lxmgq0qgk6xq1tg06xrm1aiwm','.eJxVjMsOwiAQRf-FtSEwPAou3fsNZBhAqgaS0q6M_65NutDtPefcFwu4rTVsIy9hTuzMJDv9bhHpkdsO0h3brXPqbV3myHeFH3Twa0_5eTncv4OKo37riUCCNMIToRPRWKmst4VQey1QJW11Lo6UnFSyETA5UQgKyGjAECj2_gDIrTda:1sH7CE:st8GCSX9f3BzA0aPBcVlg-w1iME6A6zt0zGBi2jzo68','2024-06-25 19:30:18.654465');
INSERT INTO "employee_employee" ("employee_code","id","employee_name","employee_national_id","birth_date","employee_phone_1","employee_phone_2","governorate","employee_email","image","slug") VALUES (1504,1,'Ahmed Shafey',27709080102691,'1979-09-08',1111947363,1015154355,'0000000000','ahmed.shafey@ecipegypt.com','employee/1504.png','1504'),
 (1200,2,'Ahmed Mohamed',221155448877,'1999-09-08',1551515,124578,'456','ahmed.mohamed@ecipegypt.com','employee/1200.png','1200'),
 (1009,3,'Ahmed Shafey 22',23165478921,'1979-09-08',1015984753,NULL,'0','ahmed.mohamed.2@ecipegypt.com','','1009'),
 (1010,4,'Ahmed Shafey 29',23165478922,'1979-09-08',1015984743,NULL,'0','ahmed.mohamed.20@ecipegypt.com','','1010');
INSERT INTO "ticket_it" ("id","it_name","it_id") VALUES (1,'Shafey',1504);
INSERT INTO "ticket_ticket" ("ticket_code","ticket_id","title","description","start_date","due_date","comment","status","assigned_to_id","requested_by_id","slug") VALUES (1002,1,'Windows Error','Windows Error','2024-06-02 11:40:01',NULL,'','new',1,1,'1002'),
 (1001,2,'Mail Error','Mail Error','2024-06-01 12:48:41',NULL,'','new',1,2,'1001'),
 (1003,3,'Activation','windows Activation','2024-06-04 20:23:51','2024-06-05 18:00:00','activated','closed',1,2,'1003'),
 (1004,4,'Internet Error','Internet Error','2024-06-05 18:00:00',NULL,'','new',1,1,'1004'),
 (1005,5,'app hang','app hang','2024-06-10 20:25:54',NULL,'','new',1,1,'1005'),
 (1007,6,'share Error','share Error','2024-06-10 20:27:09',NULL,'','new',1,1,'1007'),
 (1008,7,'cameras not respond','cameras not respond','2024-06-08 11:00:00',NULL,'','new',1,2,'1008'),
 (1011,8,'test_error','test_error','2024-06-08 11:00:00',NULL,'','new',1,2,'1011');
INSERT INTO "device_device" ("device_code","id","device_type","model_name","motherboard","cpu","ram","hdd","date","status","sites","other","slug","price") VALUES (7044060,1,'Laptop','HP Elit Book 85 8570p','test1','Core i5-3320M 2.60GHz','4G','320GB','2023-12-18 11:28:45.733523','Used','Head Office','ttttt','7044060',2000),
 (7044035,2,'Laptop','Dell Latitude E6530','Dell Inc.','Intel(R) Core(TM) i7-3520M CPU @ 2.90GHz','12G','512GB+750GB','2023-12-18 11:28:36.202900','Used','Head Office','NVIDIA NVS 5200M','7044035',5000),
 (7040020,3,'Printer','Canon IR-4025',NULL,NULL,NULL,NULL,'2024-06-12 07:45:56.089441','Used','Head Office','test','7040020',2000),
 (7048011,4,'Monitor','hp 1702',NULL,NULL,NULL,NULL,'2024-06-12 07:53:19.130732','Used','Head Office','0','7048011',20000);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" ON "auth_group_permissions" (
	"group_id",
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" (
	"group_id"
);
CREATE INDEX IF NOT EXISTS "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" (
	"permission_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_user_groups_user_id_group_id_94350c0c_uniq" ON "auth_user_groups" (
	"user_id",
	"group_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_groups_user_id_6a12ed8b" ON "auth_user_groups" (
	"user_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_groups_group_id_97559544" ON "auth_user_groups" (
	"group_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_user_user_permissions_user_id_permission_id_14a6b632_uniq" ON "auth_user_user_permissions" (
	"user_id",
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_user_permissions_user_id_a95ead1b" ON "auth_user_user_permissions" (
	"user_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_user_permissions_permission_id_1fbb5f2c" ON "auth_user_user_permissions" (
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" (
	"content_type_id"
);
CREATE INDEX IF NOT EXISTS "django_admin_log_user_id_c564eba6" ON "django_admin_log" (
	"user_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "django_content_type_app_label_model_76bd3d3b_uniq" ON "django_content_type" (
	"app_label",
	"model"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_permission_content_type_id_codename_01ab375a_uniq" ON "auth_permission" (
	"content_type_id",
	"codename"
);
CREATE INDEX IF NOT EXISTS "auth_permission_content_type_id_2f476e4b" ON "auth_permission" (
	"content_type_id"
);
CREATE INDEX IF NOT EXISTS "django_session_expire_date_a5c62663" ON "django_session" (
	"expire_date"
);
CREATE INDEX IF NOT EXISTS "employee_employee_slug_6061e06e" ON "employee_employee" (
	"slug"
);
CREATE INDEX IF NOT EXISTS "ticket_ticket_assigned_to_id_ccc590ff" ON "ticket_ticket" (
	"assigned_to_id"
);
CREATE INDEX IF NOT EXISTS "ticket_ticket_requested_by_id_f07a6ee8" ON "ticket_ticket" (
	"requested_by_id"
);
CREATE INDEX IF NOT EXISTS "ticket_ticket_slug_f9e99392" ON "ticket_ticket" (
	"slug"
);
CREATE INDEX IF NOT EXISTS "device_device_slug_20434b2c" ON "device_device" (
	"slug"
);
COMMIT;
