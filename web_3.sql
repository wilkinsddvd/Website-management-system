/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 80040
Source Host           : localhost:3306
Source Database       : web_3

Target Server Type    : MYSQL
Target Server Version : 80040
File Encoding         : 65001

Date: 2024-11-16 21:06:45
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for article_article
-- ----------------------------
DROP TABLE IF EXISTS `article_article`;
CREATE TABLE `article_article` (
  `id` char(32) COLLATE utf8mb4_bin NOT NULL,
  `title` varchar(200) COLLATE utf8mb4_bin NOT NULL,
  `content` longtext COLLATE utf8mb4_bin NOT NULL,
  `pub_time` datetime(6) NOT NULL,
  `readed_count` int NOT NULL,
  `admired_count` int NOT NULL,
  `liked_count` int NOT NULL,
  `collected_count` int NOT NULL,
  `commented_count` int NOT NULL,
  `up_time` datetime(6) NOT NULL,
  `status` varchar(10) COLLATE utf8mb4_bin NOT NULL,
  `author_id` char(32) COLLATE utf8mb4_bin NOT NULL,
  PRIMARY KEY (`id`),
  KEY `article_article_author_id_e6b479f8_fk_author_author_id` (`author_id`),
  CONSTRAINT `article_article_author_id_e6b479f8_fk_author_author_id` FOREIGN KEY (`author_id`) REFERENCES `author_author` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- ----------------------------
-- Records of article_article
-- ----------------------------
INSERT INTO `article_article` VALUES ('1da3d8c425d748189db7d836cde8c8db', '逻辑覆盖', 0xE4BA94E7A78DE980BBE8BE91E8A686E79B96E5928CE59FBAE69CACE8B7AFE5BE84E8A686E79B96E38082, '2024-11-16 06:19:31.217779', '1', '123', '123', '123', '123', '2024-11-16 06:19:31.217779', '0', '818ff1a6fec94b4abb74686a1e8cb06f');

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
INSERT INTO `author_author` VALUES ('1155580d9457411482492c76bf05f320', '1234', '1234', '1234', null, '0', null, null, null, '0', '2024-11-16 11:12:22.284475', '2024-11-16 11:12:22.284475', null, null, '2024-11-16 19:12:22.284475', null);
INSERT INTO `author_author` VALUES ('1c700fdad0f949ceac1ffcad46891fc3', 'Wang Xin', '123456', '王鑫', null, '0', null, null, null, '0', '2024-11-12 11:24:24.555587', '2024-11-12 11:24:24.555587', null, null, '2024-11-12 19:24:24.555587', null);
INSERT INTO `author_author` VALUES ('273ce47f16db4873bc1120a48899103e', 'admin123456', '123456', 'Shi Ruitong', null, '0', null, null, null, '0', '2024-11-12 07:00:01.374122', '2024-11-12 07:00:01.374122', null, null, '2024-11-12 15:00:01.374122', null);
INSERT INTO `author_author` VALUES ('47773d495cad4239ae8747760fd4f899', 'abc123', '123456', '123456', null, '0', null, null, null, '0', '2024-11-16 12:57:48.791500', '2024-11-16 12:57:48.791500', null, null, '2024-11-16 20:57:48.790495', null);
INSERT INTO `author_author` VALUES ('58e44e4ec5dd46969682de24a37a829d', 'abc', 'abc', 'abc', null, '0', null, null, null, '0', '2024-11-16 12:48:12.339545', '2024-11-16 12:48:12.339545', null, null, '2024-11-16 20:48:12.339545', null);
INSERT INTO `author_author` VALUES ('653ffdc4904a498997fc972f9a49f46a', 'Wang Lin', '123456', '王琳', null, '0', null, null, null, '0', '2024-11-12 08:18:26.690093', '2024-11-12 08:18:26.690093', null, null, '2024-11-12 16:18:26.689093', null);
INSERT INTO `author_author` VALUES ('818ff1a6fec94b4abb74686a1e8cb06f', 'admin', 'admin', '王林昊', 'wilkins', '21', '1', 'qingsdao_ddvd@163.com', '17888372051', '0', '2024-11-12 06:10:08.731884', '2024-11-12 06:10:08.731884', '', '', '2024-11-12 14:08:20.000000', null);
INSERT INTO `author_author` VALUES ('b8bcd1d8dfac46ba90ba2c57bced49dd', '12345', '12345', '12345', null, '0', null, null, null, '0', '2024-11-16 12:18:52.979111', '2024-11-16 12:18:52.979111', null, null, '2024-11-16 20:18:52.979111', null);
INSERT INTO `author_author` VALUES ('c75af1be78f84147920d2e1a44c555a6', '123', '123', '123', null, '0', null, null, null, '0', '2024-11-16 11:06:32.459269', '2024-11-16 11:06:32.459269', null, null, '2024-11-16 19:06:32.459269', null);
INSERT INTO `author_author` VALUES ('e024589be05d419a9f56944472c4c890', '123456', '123456', '123456', null, '0', null, null, null, '0', '2024-11-16 12:40:05.080267', '2024-11-16 12:40:05.080267', null, null, '2024-11-16 20:40:05.080267', null);
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
INSERT INTO `author_authorprofile` VALUES ('1f257c52bc6d4a21919989e9a37e4438', '0', '0', '0', '0', '0', '0', '0', 'e024589be05d419a9f56944472c4c890');
INSERT INTO `author_authorprofile` VALUES ('35e21629508d44a9a71a155dbdccf5f0', '0', '0', '0', '0', '0', '0', '0', 'c75af1be78f84147920d2e1a44c555a6');
INSERT INTO `author_authorprofile` VALUES ('7925fff97e174be58bf4cbadf81fd554', '0', '0', '0', '0', '0', '0', '0', '1155580d9457411482492c76bf05f320');
INSERT INTO `author_authorprofile` VALUES ('98abc8f9e3eb499ba5735c5df560352a', '0', '0', '0', '0', '0', '0', '0', '47773d495cad4239ae8747760fd4f899');
INSERT INTO `author_authorprofile` VALUES ('c02f915e8af4433c83f6d2c8dcfde227', '0', '0', '0', '0', '0', '0', '0', 'b8bcd1d8dfac46ba90ba2c57bced49dd');
INSERT INTO `author_authorprofile` VALUES ('d78f6a9851174a8193a14687aaadaff0', '0', '0', '0', '0', '0', '0', '0', '58e44e4ec5dd46969682de24a37a829d');

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
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

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
INSERT INTO `auth_permission` VALUES ('33', 'Can add article', '9', 'add_article');
INSERT INTO `auth_permission` VALUES ('34', 'Can change article', '9', 'change_article');
INSERT INTO `auth_permission` VALUES ('35', 'Can delete article', '9', 'delete_article');
INSERT INTO `auth_permission` VALUES ('36', 'Can view article', '9', 'view_article');

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
INSERT INTO `auth_user` VALUES ('1', 'pbkdf2_sha256$600000$kjqfMR2HDRb8S7xmGSiIeu$jjVBzqDGKfjpDTIeLnX2zDGwVayq7DRdKdFGyXhhdqY=', '2024-11-16 06:17:48.166585', '1', 'admin', '', '', 'qingsdao_ddvd@163.com', '1', '1', '2024-11-12 05:57:26.703278');

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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------
INSERT INTO `django_admin_log` VALUES ('1', '2024-11-12 06:10:08.733885', 0x38313866663161362D666563392D346234612D626237342D363836613165386362303666, '王林昊', '1', 0x5B7B226164646564223A207B7D7D5D, '7', '1');
INSERT INTO `django_admin_log` VALUES ('2', '2024-11-12 06:17:12.385421', 0x66616365663064362D626539622D343961352D396361322D386461336462643938313463, 'Wang Lin', '1', 0x5B7B226164646564223A207B7D7D5D, '7', '1');
INSERT INTO `django_admin_log` VALUES ('3', '2024-11-16 06:19:31.219778', 0x31646133643863342D323564372D343831382D396462372D643833366364653863386462, '文章标题: 逻辑覆盖,文章内容: 五种逻辑覆盖和基本路径覆盖。', '1', 0x5B7B226164646564223A207B7D7D5D, '9', '1');

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
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('9', 'article', 'article');
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
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

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
INSERT INTO `django_migrations` VALUES ('20', 'author', '0002_remove_author_authors_liked', '2024-11-16 05:57:26.998088');
INSERT INTO `django_migrations` VALUES ('21', 'article', '0001_initial', '2024-11-16 05:57:27.125861');

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
INSERT INTO `django_session` VALUES ('g63ok8cf41mc89j2vsvdj2habjn2u08y', 0x2E654A78645572474F3030415144516C78544D4A784234694769704A724C44732D323747753465416B684535634155704473397231726D4D54783436384E7079516B4B4467454767724D7677436E3047482D41682D674A614F6B6C6E374C6B71775A586C6D3973336274325F3258665F727232366E65643743666256446146306C704A61694A436B48646355426457756A786D6730467A6B7537504F584E4A3856566C546B565A6B7953304F73693156705053323479423565596E63334342497145314150504D59385164324154627A51643250663976306764466E675249486E68334559524F3434694D4C415A685368396F525363554474536377447A34325A4D775A6C614D36694248586E51676C6E316B4A764B314747464B42754E426D70383255617A544D42713430653436674E7A75454450414E3963495049696C5943456C4D4E475F58506D3351462D2D5F62646370356D735F676B2D7079426D724152557A7272414A31505535467869574A614A5149684E5A4D6462567A562D75362D55326E54343476615651767A53763466505062394D66785857766E792D4F6A763266665F377A34325A464D6D6471656E4335516563385A7536444D4A5A587964564879646145554E4E744335486979706E4371656E516D344B536A6A426C614C6B7173394D574370706B4F6C6B6D52613479686A31684C6E4B6F4E61685168585356496C5770436B325038663769435238504237394865794C673336505968735A5770363238303230716E3133534B586C555538354F4F666A2D696E397254635F7A55714637793952374A654A767473494830305A4779304F4A4B3146764F4D527132796A696831627270396C6254626A74486B71567A684B484E70336A48326D7441586F6C53706B574F4D7A36777870626A34304271367839655F7851323A31744349534C3A5865615A7953585A69506B494B6B51754930534E467A312D396D716F4D2D704159727A7658566F774F3077, '2024-11-30 13:03:17.757725');
