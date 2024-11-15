/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 80040
Source Host           : localhost:3306
Source Database       : web_3

Target Server Type    : MYSQL
Target Server Version : 80040
File Encoding         : 65001

Date: 2024-11-15 21:30:53
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for author_author
-- ----------------------------
DROP TABLE IF EXISTS `author_author`;
CREATE TABLE `author_author` (
  `id` char(32) COLLATE utf8mb4_bin NOT NULL,
  `username` varchar(50) COLLATE utf8mb4_bin NOT NULL,
  `password` varchar(50) COLLATE utf8mb4_bin NOT NULL,
  `realname` varchar(20) COLLATE utf8mb4_bin DEFAULT NULL,
  `nickname` varchar(20) COLLATE utf8mb4_bin DEFAULT NULL,
  `age` int NOT NULL,
  `gender` varchar(1) COLLATE utf8mb4_bin DEFAULT NULL,
  `email` varchar(254) COLLATE utf8mb4_bin DEFAULT NULL,
  `phone` varchar(20) COLLATE utf8mb4_bin DEFAULT NULL,
  `status` varchar(5) COLLATE utf8mb4_bin NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `intro` longtext COLLATE utf8mb4_bin,
  `remark` longtext COLLATE utf8mb4_bin,
  `created_at` datetime(6) NOT NULL,
  `author_liked_id` char(32) COLLATE utf8mb4_bin DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `nickname` (`nickname`),
  UNIQUE KEY `author_liked_id` (`author_liked_id`),
  KEY `author_author_realname_1386c622` (`realname`),
  KEY `author_author_email_a3ebd156` (`email`),
  KEY `author_author_phone_5383ce06` (`phone`),
  CONSTRAINT `author_author_author_liked_id_ab8b712e_fk_author_author_id` FOREIGN KEY (`author_liked_id`) REFERENCES `author_author` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- ----------------------------
-- Records of author_author
-- ----------------------------
INSERT INTO `author_author` VALUES ('1c700fdad0f949ceac1ffcad46891fc3', 'Wang Xin', '123456', '王鑫', null, '0', null, null, null, '0', '2024-11-12 11:24:24.555587', '2024-11-12 11:24:24.555587', null, null, '2024-11-12 19:24:24.555587', null);
INSERT INTO `author_author` VALUES ('273ce47f16db4873bc1120a48899103e', 'admin123456', '123456', 'Shi Ruitong', null, '0', null, null, null, '0', '2024-11-12 07:00:01.374122', '2024-11-12 07:00:01.374122', null, null, '2024-11-12 15:00:01.374122', null);
INSERT INTO `author_author` VALUES ('653ffdc4904a498997fc972f9a49f46a', 'Wang Lin', '123456', '王琳', null, '0', null, null, null, '0', '2024-11-12 08:18:26.690093', '2024-11-12 08:18:26.690093', null, null, '2024-11-12 16:18:26.689093', null);
INSERT INTO `author_author` VALUES ('818ff1a6fec94b4abb74686a1e8cb06f', 'admin', 'admin', '王林昊', 'wilkins', '21', '1', 'qingsdao_ddvd@163.com', '17888372051', '0', '2024-11-12 06:10:08.731884', '2024-11-12 06:10:08.731884', '', '', '2024-11-12 14:08:20.000000', null);
INSERT INTO `author_author` VALUES ('facef0d6be9b49a59ca28da3dbd9814c', 'admin123', 'admin123', 'Wang Lin', 'ddvd', '21', '0', 'qingsdao_ddvd@163.com', '17888372051', '0', '2024-11-12 06:17:12.384421', '2024-11-12 06:17:12.384421', '', '', '2024-11-12 14:16:39.000000', null);

-- ----------------------------
-- Table structure for author_authorprofile
-- ----------------------------
DROP TABLE IF EXISTS `author_authorprofile`;
CREATE TABLE `author_authorprofile` (
  `id` char(32) COLLATE utf8mb4_bin NOT NULL,
  `fans_count` int NOT NULL,
  `visited_count` int NOT NULL,
  `word_count` int NOT NULL,
  `aricle_count` int NOT NULL,
  `collected_count` int NOT NULL,
  `liked_count` int NOT NULL,
  `admired_count` int NOT NULL,
  `author_id` char(32) COLLATE utf8mb4_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `author_id` (`author_id`),
  CONSTRAINT `author_authorprofile_author_id_0a32c9e3_fk_author_author_id` FOREIGN KEY (`author_id`) REFERENCES `author_author` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- ----------------------------
-- Records of author_authorprofile
-- ----------------------------

-- ----------------------------
-- Table structure for author_author_authors_liked
-- ----------------------------
DROP TABLE IF EXISTS `author_author_authors_liked`;
CREATE TABLE `author_author_authors_liked` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `from_author_id` char(32) COLLATE utf8mb4_bin NOT NULL,
  `to_author_id` char(32) COLLATE utf8mb4_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `author_author_authors_li_from_author_id_to_author_76fd0d72_uniq` (`from_author_id`,`to_author_id`),
  KEY `author_author_author_to_author_id_74e7624b_fk_author_au` (`to_author_id`),
  CONSTRAINT `author_author_author_from_author_id_723e40c2_fk_author_au` FOREIGN KEY (`from_author_id`) REFERENCES `author_author` (`id`),
  CONSTRAINT `author_author_author_to_author_id_74e7624b_fk_author_au` FOREIGN KEY (`to_author_id`) REFERENCES `author_author` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- ----------------------------
-- Records of author_author_authors_liked
-- ----------------------------

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8mb4_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_bin NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('2', 'Can change log entry', '1', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete log entry', '1', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('4', 'Can view log entry', '1', 'view_logentry');
INSERT INTO `auth_permission` VALUES ('5', 'Can add permission', '2', 'add_permission');
INSERT INTO `auth_permission` VALUES ('6', 'Can change permission', '2', 'change_permission');
INSERT INTO `auth_permission` VALUES ('7', 'Can delete permission', '2', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('8', 'Can view permission', '2', 'view_permission');
INSERT INTO `auth_permission` VALUES ('9', 'Can add group', '3', 'add_group');
INSERT INTO `auth_permission` VALUES ('10', 'Can change group', '3', 'change_group');
INSERT INTO `auth_permission` VALUES ('11', 'Can delete group', '3', 'delete_group');
INSERT INTO `auth_permission` VALUES ('12', 'Can view group', '3', 'view_group');
INSERT INTO `auth_permission` VALUES ('13', 'Can add user', '4', 'add_user');
INSERT INTO `auth_permission` VALUES ('14', 'Can change user', '4', 'change_user');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete user', '4', 'delete_user');
INSERT INTO `auth_permission` VALUES ('16', 'Can view user', '4', 'view_user');
INSERT INTO `auth_permission` VALUES ('17', 'Can add content type', '5', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('18', 'Can change content type', '5', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('19', 'Can delete content type', '5', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('20', 'Can view content type', '5', 'view_contenttype');
INSERT INTO `auth_permission` VALUES ('21', 'Can add session', '6', 'add_session');
INSERT INTO `auth_permission` VALUES ('22', 'Can change session', '6', 'change_session');
INSERT INTO `auth_permission` VALUES ('23', 'Can delete session', '6', 'delete_session');
INSERT INTO `auth_permission` VALUES ('24', 'Can view session', '6', 'view_session');
INSERT INTO `auth_permission` VALUES ('25', 'Can add author', '7', 'add_author');
INSERT INTO `auth_permission` VALUES ('26', 'Can change author', '7', 'change_author');
INSERT INTO `auth_permission` VALUES ('27', 'Can delete author', '7', 'delete_author');
INSERT INTO `auth_permission` VALUES ('28', 'Can view author', '7', 'view_author');
INSERT INTO `auth_permission` VALUES ('29', 'Can add author profile', '8', 'add_authorprofile');
INSERT INTO `auth_permission` VALUES ('30', 'Can change author profile', '8', 'change_authorprofile');
INSERT INTO `auth_permission` VALUES ('31', 'Can delete author profile', '8', 'delete_authorprofile');
INSERT INTO `auth_permission` VALUES ('32', 'Can view author profile', '8', 'view_authorprofile');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8mb4_bin NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8mb4_bin NOT NULL,
  `first_name` varchar(150) COLLATE utf8mb4_bin NOT NULL,
  `last_name` varchar(150) COLLATE utf8mb4_bin NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_bin NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- ----------------------------
-- Records of auth_user
-- ----------------------------
INSERT INTO `auth_user` VALUES ('1', 'pbkdf2_sha256$600000$kjqfMR2HDRb8S7xmGSiIeu$jjVBzqDGKfjpDTIeLnX2zDGwVayq7DRdKdFGyXhhdqY=', '2024-11-12 06:08:17.906918', '1', 'admin', '', '', 'qingsdao_ddvd@163.com', '1', '1', '2024-11-12 05:57:26.703278');

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8mb4_bin,
  `object_repr` varchar(200) COLLATE utf8mb4_bin NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext COLLATE utf8mb4_bin NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------
INSERT INTO `django_admin_log` VALUES ('1', '2024-11-12 06:10:08.733885', 0x38313866663161362D666563392D346234612D626237342D363836613165386362303666, '王林昊', '1', 0x5B7B226164646564223A207B7D7D5D, '7', '1');
INSERT INTO `django_admin_log` VALUES ('2', '2024-11-12 06:17:12.385421', 0x66616365663064362D626539622D343961352D396361322D386461336462643938313463, 'Wang Lin', '1', 0x5B7B226164646564223A207B7D7D5D, '7', '1');

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  `model` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('4', 'auth', 'user');
INSERT INTO `django_content_type` VALUES ('7', 'author', 'author');
INSERT INTO `django_content_type` VALUES ('8', 'author', 'authorprofile');
INSERT INTO `django_content_type` VALUES ('5', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('6', 'sessions', 'session');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8mb4_bin NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_bin NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2024-11-12 05:43:39.048363');
INSERT INTO `django_migrations` VALUES ('2', 'auth', '0001_initial', '2024-11-12 05:43:39.573667');
INSERT INTO `django_migrations` VALUES ('3', 'admin', '0001_initial', '2024-11-12 05:43:39.788874');
INSERT INTO `django_migrations` VALUES ('4', 'admin', '0002_logentry_remove_auto_add', '2024-11-12 05:43:39.796457');
INSERT INTO `django_migrations` VALUES ('5', 'admin', '0003_logentry_add_action_flag_choices', '2024-11-12 05:43:39.804885');
INSERT INTO `django_migrations` VALUES ('6', 'contenttypes', '0002_remove_content_type_name', '2024-11-12 05:43:39.874677');
INSERT INTO `django_migrations` VALUES ('7', 'auth', '0002_alter_permission_name_max_length', '2024-11-12 05:43:39.933307');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0003_alter_user_email_max_length', '2024-11-12 05:43:39.953400');
INSERT INTO `django_migrations` VALUES ('9', 'auth', '0004_alter_user_username_opts', '2024-11-12 05:43:39.960395');
INSERT INTO `django_migrations` VALUES ('10', 'auth', '0005_alter_user_last_login_null', '2024-11-12 05:43:40.007557');
INSERT INTO `django_migrations` VALUES ('11', 'auth', '0006_require_contenttypes_0002', '2024-11-12 05:43:40.010562');
INSERT INTO `django_migrations` VALUES ('12', 'auth', '0007_alter_validators_add_error_messages', '2024-11-12 05:43:40.018558');
INSERT INTO `django_migrations` VALUES ('13', 'auth', '0008_alter_user_username_max_length', '2024-11-12 05:43:40.075012');
INSERT INTO `django_migrations` VALUES ('14', 'auth', '0009_alter_user_last_name_max_length', '2024-11-12 05:43:40.133193');
INSERT INTO `django_migrations` VALUES ('15', 'auth', '0010_alter_group_name_max_length', '2024-11-12 05:43:40.150270');
INSERT INTO `django_migrations` VALUES ('16', 'auth', '0011_update_proxy_permissions', '2024-11-12 05:43:40.157511');
INSERT INTO `django_migrations` VALUES ('17', 'auth', '0012_alter_user_first_name_max_length', '2024-11-12 05:43:40.216672');
INSERT INTO `django_migrations` VALUES ('18', 'author', '0001_initial', '2024-11-12 05:43:40.539045');
INSERT INTO `django_migrations` VALUES ('19', 'sessions', '0001_initial', '2024-11-12 05:43:40.572045');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8mb4_bin NOT NULL,
  `session_data` longtext COLLATE utf8mb4_bin NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('9px0mqd9z8lllnqedfe9ic2dpb1o0fae', 0x2E654A784E6A45734B776A415552585867554152586F5A4F514E4361766D596C7A313144657938653253677639444155586B474663683175306F6B4C76384A7A4466617965723856333937534C36774C486F537A47336E644635564A63696853334D305A6F7237365A784E3756324678615A74746D364370696E345439624D5F4F72664F3330375F647A41354B374D73556A347049655A524175544A614273323142694D4A6841576C545442675A516257414365635570346A2D675079504468514D70444930736A653532305F47673A3174416A75623A4367497957766654587239757744494C4D794C653776393863696E2D327A42793152646F35764E39726355, '2024-11-26 05:58:01.918093');
INSERT INTO `django_session` VALUES ('kxmqczensayuf80v8j37bobt6iapokn1', 0x2E654A7864556B3176303041515456506975456C70426149634F564D4F6C68335848376D673869456B694F414136746C61653966784E6F366465753157516B4B6942346F6F4B7A686B454A77346375624F4C2D4350464135632D414F495762757041725973373879386E586E7A5A6C3532506C786662645850433767704C77656B4B704F67457177494F415735596F47387575514C53545268475161323654374A78726B5235566C5A384E4251454F4D384B6F7A484F5758703351563263796C42516B51436374634A51346352327774395A2D6A6173577536726A653051382D4B504D6364786B4D76736764654E50544D6B43445539416C684F385430592D6F35646878614135436179706B58494C664F6D6444516D4B7179416D6B49426E4B6A746F49716D5F466F6B6A4B594C393352376A53484533674654304531726757694A435744524A65396D76327A32707A44396E45544A355479624178765A4A7547494C75557861524B533544724D576370465546456F6F51687441706C57796C337161727133393765775F754C4E484B565A79576358736D5F7968763753666E7430656A376E792D5F33782D33524368314A55394770736938512D69555A794431475248694B435F6F6B7174674A473151617A5F65765433375F50487330796D364D2D797863586550654472686D6342695A4D7867744357314D553642465A43305A59644E43553952737750735256435342355165306C334C745847515579777A535F494D6B5F51747A5F64393278755944693641707153704D4F4F4B696145494B5A51734B4C6D71706C4D385F332D63773731653932645F586576705F56755F494C476C72767A50566571354D74655569527158424F3152533732766351357146696634795834316F78633145756666624C6472534165564C484B514C61525859466646424A4948737465516F7745704C2D3574364E6477755266334E7073564346492D5152684F36416D755A374E4277534572424D39525A5733484742695769374F736A4C386631535F483A3174427675533A483168763951444E442D6572395A574B6F645A3169524957566A796C5431747662726F61766475524C5459, '2024-11-29 12:58:48.061837');
