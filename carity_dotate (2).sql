-- phpMyAdmin SQL Dump
-- version 4.2.7.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Nov 22, 2021 at 05:03 AM
-- Server version: 5.6.20
-- PHP Version: 5.5.15

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `carity_dotate`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE IF NOT EXISTS `auth_group` (
`id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
`id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE IF NOT EXISTS `auth_permission` (
`id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=65 ;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add beneficiary', 1, 'add_beneficiary'),
(2, 'Can change beneficiary', 1, 'change_beneficiary'),
(3, 'Can delete beneficiary', 1, 'delete_beneficiary'),
(4, 'Can view beneficiary', 1, 'view_beneficiary'),
(5, 'Can add location', 2, 'add_location'),
(6, 'Can change location', 2, 'change_location'),
(7, 'Can delete location', 2, 'delete_location'),
(8, 'Can view location', 2, 'view_location'),
(9, 'Can add volunteer_reg', 3, 'add_volunteer_reg'),
(10, 'Can change volunteer_reg', 3, 'change_volunteer_reg'),
(11, 'Can delete volunteer_reg', 3, 'delete_volunteer_reg'),
(12, 'Can view volunteer_reg', 3, 'view_volunteer_reg'),
(13, 'Can add user type', 4, 'add_usertype'),
(14, 'Can change user type', 4, 'change_usertype'),
(15, 'Can delete user type', 4, 'delete_usertype'),
(16, 'Can view user type', 4, 'view_usertype'),
(17, 'Can add request_ need', 5, 'add_request_need'),
(18, 'Can change request_ need', 5, 'change_request_need'),
(19, 'Can delete request_ need', 5, 'delete_request_need'),
(20, 'Can view request_ need', 5, 'view_request_need'),
(21, 'Can add beneficiary_ report', 6, 'add_beneficiary_report'),
(22, 'Can change beneficiary_ report', 6, 'change_beneficiary_report'),
(23, 'Can delete beneficiary_ report', 6, 'delete_beneficiary_report'),
(24, 'Can view beneficiary_ report', 6, 'view_beneficiary_report'),
(25, 'Can add benefactorr', 7, 'add_benefactorr'),
(26, 'Can change benefactorr', 7, 'change_benefactorr'),
(27, 'Can delete benefactorr', 7, 'delete_benefactorr'),
(28, 'Can view benefactorr', 7, 'view_benefactorr'),
(29, 'Can add benefactor_ report', 8, 'add_benefactor_report'),
(30, 'Can change benefactor_ report', 8, 'change_benefactor_report'),
(31, 'Can delete benefactor_ report', 8, 'delete_benefactor_report'),
(32, 'Can view benefactor_ report', 8, 'view_benefactor_report'),
(33, 'Can add log entry', 9, 'add_logentry'),
(34, 'Can change log entry', 9, 'change_logentry'),
(35, 'Can delete log entry', 9, 'delete_logentry'),
(36, 'Can view log entry', 9, 'view_logentry'),
(37, 'Can add permission', 10, 'add_permission'),
(38, 'Can change permission', 10, 'change_permission'),
(39, 'Can delete permission', 10, 'delete_permission'),
(40, 'Can view permission', 10, 'view_permission'),
(41, 'Can add group', 11, 'add_group'),
(42, 'Can change group', 11, 'change_group'),
(43, 'Can delete group', 11, 'delete_group'),
(44, 'Can view group', 11, 'view_group'),
(45, 'Can add user', 12, 'add_user'),
(46, 'Can change user', 12, 'change_user'),
(47, 'Can delete user', 12, 'delete_user'),
(48, 'Can view user', 12, 'view_user'),
(49, 'Can add content type', 13, 'add_contenttype'),
(50, 'Can change content type', 13, 'change_contenttype'),
(51, 'Can delete content type', 13, 'delete_contenttype'),
(52, 'Can view content type', 13, 'view_contenttype'),
(53, 'Can add session', 14, 'add_session'),
(54, 'Can change session', 14, 'change_session'),
(55, 'Can delete session', 14, 'delete_session'),
(56, 'Can view session', 14, 'view_session'),
(57, 'Can add product_add', 15, 'add_product_add'),
(58, 'Can change product_add', 15, 'change_product_add'),
(59, 'Can delete product_add', 15, 'delete_product_add'),
(60, 'Can view product_add', 15, 'view_product_add'),
(61, 'Can add feedback', 16, 'add_feedback'),
(62, 'Can change feedback', 16, 'change_feedback'),
(63, 'Can delete feedback', 16, 'delete_feedback'),
(64, 'Can view feedback', 16, 'view_feedback');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE IF NOT EXISTS `auth_user` (
`id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=50 ;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(18, 'pbkdf2_sha256$180000$76EBvHuqHcGk$xdGhCKrY7i24UunmkXkh81TT/GmidHqHqZpByvc5ZXc=', '2021-11-21 05:54:52.484861', 1, 'admin', '', '1', 'admin@gmail.com', 1, 1, '2021-11-10 20:52:40.871103'),
(28, 'pbkdf2_sha256$180000$A1UDHmvUg9IZ$kH0csj/u8cH7UjyeaL/6tGna77iOstTK4cUhZQfM4rE=', '2021-11-21 07:06:30.273203', 0, 'athirathanikunnel@gmail.com', 'athira', '1', 'athirathanikunnel@gmail.com', 0, 1, '2021-11-13 18:24:26.637777'),
(29, 'pbkdf2_sha256$180000$pnZxCepcMP5s$fa8faB70bFe61Qi6lHVkSaifX7sbcFaLQXfMZ67tmzI=', '2021-11-21 07:02:48.330979', 0, 'subin@gmail.com', 'subin', '1', 'arunkumarthanikkunel@gmail.com', 0, 1, '2021-11-13 18:26:15.345383'),
(30, 'pbkdf2_sha256$180000$YPCtEzqiLK3r$+Yw52+0/PGVJg/2IkA1wn7hf2PxHkEjEUbrGW4/OD04=', NULL, 0, 'mayaa@gmai.com', 'maya', '1', 'mayaa@gmai.com', 0, 1, '2021-11-14 07:43:36.946551'),
(34, 'pbkdf2_sha256$180000$aizZf42vghTd$4K3NI+0hKOsZqSIcY/7RpA2QUVTlvfk7KPYjkGzgM2A=', '2021-11-21 07:12:19.547529', 0, 'arunkumarthanikkunel@gmail.com', 'Arunkumar', '1', 'arunkumarthanikkunel@gmail.com', 0, 1, '2021-11-15 14:41:58.737654');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE IF NOT EXISTS `auth_user_groups` (
`id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
`id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `charity_benefactorr`
--

CREATE TABLE IF NOT EXISTS `charity_benefactorr` (
`id` int(11) NOT NULL,
  `location` varchar(50) NOT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `type1` varchar(50) NOT NULL,
  `status` varchar(100) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `City_Address` varchar(50) DEFAULT NULL,
  `Home_Address` varchar(50) DEFAULT NULL,
  `Street_Address` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=19 ;

--
-- Dumping data for table `charity_benefactorr`
--

INSERT INTO `charity_benefactorr` (`id`, `location`, `phone`, `type1`, `status`, `user_id`, `City_Address`, `Home_Address`, `Street_Address`, `password`) VALUES
(9, 'malappuram', '2147483647', 'long_term', '1', 30, 'malappuram', 'melottuparamb', 'Vazhikadavu', 'maya12345678'),
(12, 'malappuram', '2147483647', 'long_term', '1', 34, 'malappuram', 'melottuparamb', 'Vazhikadavu', 'arunkumar');

-- --------------------------------------------------------

--
-- Table structure for table `charity_benefactor_report`
--

CREATE TABLE IF NOT EXISTS `charity_benefactor_report` (
`id` int(11) NOT NULL,
  `location` varchar(50) DEFAULT NULL,
  `reply` varchar(50) NOT NULL,
  `status` varchar(100) NOT NULL,
  `benefactor_id_id` int(11) DEFAULT NULL
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=10 ;

--
-- Dumping data for table `charity_benefactor_report`
--

INSERT INTO `charity_benefactor_report` (`id`, `location`, `reply`, `status`, `benefactor_id_id`) VALUES
(7, 'muvatupuzha', 'Accept', '1', 9),
(9, 'muvatupuzha', 'Accept', '1', 12);

-- --------------------------------------------------------

--
-- Table structure for table `charity_beneficiary`
--

CREATE TABLE IF NOT EXISTS `charity_beneficiary` (
`id` int(11) NOT NULL,
  `location` varchar(50) NOT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `type1` varchar(50) NOT NULL,
  `status` varchar(100) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `city_Address` varchar(50) DEFAULT NULL,
  `home_Address` varchar(50) DEFAULT NULL,
  `street_Address` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=8 ;

--
-- Dumping data for table `charity_beneficiary`
--

INSERT INTO `charity_beneficiary` (`id`, `location`, `phone`, `type1`, `status`, `user_id`, `city_Address`, `home_Address`, `street_Address`, `password`) VALUES
(7, 'malappuram', '2147483647', 'long_term', '1', 28, 'kottarakara', 'melottuparam', 'kottayam', 'athira12345678');

-- --------------------------------------------------------

--
-- Table structure for table `charity_beneficiary_report`
--

CREATE TABLE IF NOT EXISTS `charity_beneficiary_report` (
`id` int(11) NOT NULL,
  `location` varchar(50) DEFAULT NULL,
  `reply` varchar(50) NOT NULL,
  `status` varchar(100) NOT NULL,
  `beneficiary_id_id` int(11) DEFAULT NULL
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `charity_beneficiary_report`
--

INSERT INTO `charity_beneficiary_report` (`id`, `location`, `reply`, `status`, `beneficiary_id_id`) VALUES
(4, 'muvatupuzha', 'Accept', '1', 7);

-- --------------------------------------------------------

--
-- Table structure for table `charity_feedback`
--

CREATE TABLE IF NOT EXISTS `charity_feedback` (
`id` int(11) NOT NULL,
  `feedback` varchar(300) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=7 ;

--
-- Dumping data for table `charity_feedback`
--

INSERT INTO `charity_feedback` (`id`, `feedback`, `user_id`) VALUES
(1, 'good', 29),
(2, 'good', 28);

-- --------------------------------------------------------

--
-- Table structure for table `charity_location`
--

CREATE TABLE IF NOT EXISTS `charity_location` (
`id` int(11) NOT NULL,
  `location` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Dumping data for table `charity_location`
--

INSERT INTO `charity_location` (`id`, `location`, `status`) VALUES
(3, 'malappuram', '1'),
(4, 'muvatupuzha', '1');

-- --------------------------------------------------------

--
-- Table structure for table `charity_product_add`
--

CREATE TABLE IF NOT EXISTS `charity_product_add` (
`id` int(11) NOT NULL,
  `products` varchar(300) DEFAULT NULL,
  `expiry_date` date DEFAULT NULL,
  `members` int(11) DEFAULT NULL,
  `status` varchar(100) NOT NULL,
  `benefactor_id` int(11) DEFAULT NULL,
  `location` varchar(300) DEFAULT NULL,
  `collected_date` date DEFAULT NULL,
  `volunteer_id` int(11) DEFAULT NULL,
  `status1` varchar(100) NOT NULL
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=16 ;

--
-- Dumping data for table `charity_product_add`
--

INSERT INTO `charity_product_add` (`id`, `products`, `expiry_date`, `members`, `status`, `benefactor_id`, `location`, `collected_date`, `volunteer_id`, `status1`) VALUES
(13, '[''Food'', ''Dress'', ''Book'']', '2021-11-16', 5, 'accepted', 12, 'malappuram', '2021-11-14', 7, '1'),
(15, '[''Food'', ''Dress'']', '2021-11-25', 7, '0', 12, 'malappuram', NULL, NULL, '0');

-- --------------------------------------------------------

--
-- Table structure for table `charity_request_need`
--

CREATE TABLE IF NOT EXISTS `charity_request_need` (
`id` int(11) NOT NULL,
  `location` varchar(50) DEFAULT NULL,
  `members` varchar(50) DEFAULT NULL,
  `product_need` varchar(300) DEFAULT NULL,
  `benfi_id_id` int(11) DEFAULT NULL,
  `status` varchar(100) NOT NULL,
  `need_status` varchar(100) NOT NULL,
  `status1` varchar(100) NOT NULL,
  `volunteer_id` int(11) DEFAULT NULL
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=9 ;

--
-- Dumping data for table `charity_request_need`
--

INSERT INTO `charity_request_need` (`id`, `location`, `members`, `product_need`, `benfi_id_id`, `status`, `need_status`, `status1`, `volunteer_id`) VALUES
(7, 'malappuram', '5', '[''Food'', ''Dress'', ''Book'']', 7, '0', 'Accept', '0', 7),
(8, 'muvatupuzha', '4', '[''Food'', ''Dress'', ''Book'']', 7, '0', 'apply', '0', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `charity_usertype`
--

CREATE TABLE IF NOT EXISTS `charity_usertype` (
`id` int(11) NOT NULL,
  `type` varchar(50) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=29 ;

--
-- Dumping data for table `charity_usertype`
--

INSERT INTO `charity_usertype` (`id`, `type`, `user_id`) VALUES
(21, 'beneficiary', 28),
(22, 'volunteer', 29),
(23, 'benefactor', 30),
(26, 'benefactor', 34);

-- --------------------------------------------------------

--
-- Table structure for table `charity_volunteer_reg`
--

CREATE TABLE IF NOT EXISTS `charity_volunteer_reg` (
`id` int(11) NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `proof` varchar(100) DEFAULT NULL,
  `qualification` varchar(50) NOT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `location` varchar(50) NOT NULL,
  `status` varchar(100) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `City_Address` varchar(50) DEFAULT NULL,
  `Home_Address` varchar(50) DEFAULT NULL,
  `Street_Address` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=8 ;

--
-- Dumping data for table `charity_volunteer_reg`
--

INSERT INTO `charity_volunteer_reg` (`id`, `image`, `proof`, `qualification`, `phone`, `location`, `status`, `user_id`, `City_Address`, `Home_Address`, `Street_Address`, `password`) VALUES
(7, 'wallpaperflare.com_wallpaper_4mPrz6J.jpg', 'GIVE FOR GOOD- reference doc_s4LYP7U.docx', 'b.tech', '2147483647', 'malappuram', NULL, 29, 'edukki', 'thottuvalli', 'thonikkadavu', 'subin12345678');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE IF NOT EXISTS `django_admin_log` (
`id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE IF NOT EXISTS `django_content_type` (
`id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=17 ;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(9, 'admin', 'logentry'),
(11, 'auth', 'group'),
(10, 'auth', 'permission'),
(12, 'auth', 'user'),
(7, 'charity', 'benefactorr'),
(8, 'charity', 'benefactor_report'),
(1, 'charity', 'beneficiary'),
(6, 'charity', 'beneficiary_report'),
(16, 'charity', 'feedback'),
(2, 'charity', 'location'),
(15, 'charity', 'product_add'),
(5, 'charity', 'request_need'),
(4, 'charity', 'usertype'),
(3, 'charity', 'volunteer_reg'),
(13, 'contenttypes', 'contenttype'),
(14, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE IF NOT EXISTS `django_migrations` (
`id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=37 ;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2021-11-05 20:26:46.022578'),
(2, 'auth', '0001_initial', '2021-11-05 20:26:46.440607'),
(3, 'admin', '0001_initial', '2021-11-05 20:26:46.949646'),
(4, 'admin', '0002_logentry_remove_auto_add', '2021-11-05 20:26:47.052654'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2021-11-05 20:26:47.066655'),
(6, 'contenttypes', '0002_remove_content_type_name', '2021-11-05 20:26:47.197665'),
(7, 'auth', '0002_alter_permission_name_max_length', '2021-11-05 20:26:47.251668'),
(8, 'auth', '0003_alter_user_email_max_length', '2021-11-05 20:26:47.307673'),
(9, 'auth', '0004_alter_user_username_opts', '2021-11-05 20:26:47.320675'),
(10, 'auth', '0005_alter_user_last_login_null', '2021-11-05 20:26:47.380679'),
(11, 'auth', '0006_require_contenttypes_0002', '2021-11-05 20:26:47.385680'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2021-11-05 20:26:47.397683'),
(13, 'auth', '0008_alter_user_username_max_length', '2021-11-05 20:26:47.455685'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2021-11-05 20:26:47.513688'),
(15, 'auth', '0010_alter_group_name_max_length', '2021-11-05 20:26:47.571694'),
(16, 'auth', '0011_update_proxy_permissions', '2021-11-05 20:26:47.583694'),
(17, 'charity', '0001_initial', '2021-11-05 20:26:48.292748'),
(18, 'sessions', '0001_initial', '2021-11-05 20:26:48.692779'),
(19, 'charity', '0002_request_need_status', '2021-11-05 22:12:44.700359'),
(20, 'charity', '0003_product_add', '2021-11-06 03:35:09.018424'),
(21, 'charity', '0004_remove_product_add_quantity', '2021-11-06 03:45:10.188446'),
(22, 'charity', '0005_product_add_volunteer', '2021-11-06 04:19:41.850428'),
(23, 'charity', '0006_auto_20211106_1035', '2021-11-06 05:05:22.397365'),
(24, 'charity', '0007_auto_20211110_0008', '2021-11-09 18:38:11.714098'),
(25, 'charity', '0008_remove_benefactorr_h_name', '2021-11-09 18:40:25.166601'),
(26, 'charity', '0009_remove_benefactorr_city', '2021-11-09 18:44:49.967097'),
(27, 'charity', '0010_auto_20211110_0027', '2021-11-09 18:57:36.089796'),
(28, 'charity', '0011_auto_20211111_0051', '2021-11-11 14:20:38.736021'),
(29, 'charity', '0012_auto_20211111_0052', '2021-11-11 14:20:38.828026'),
(30, 'charity', '0013_auto_20211111_1950', '2021-11-11 14:20:39.247425'),
(31, 'charity', '0014_auto_20211116_0718', '2021-11-16 01:48:37.071763'),
(32, 'charity', '0015_feedback', '2021-11-17 16:48:46.323340'),
(33, 'charity', '0016_auto_20211120_1655', '2021-11-20 11:25:30.755828'),
(34, 'charity', '0017_product_add_status1', '2021-11-20 17:52:49.911325'),
(35, 'charity', '0018_auto_20211121_1217', '2021-11-21 06:47:25.656394'),
(36, 'charity', '0019_auto_20211121_1219', '2021-11-21 06:49:38.446930');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('04rmdnlo2cu5lorhcsi59y3ezkcew3x9', 'OTkyM2E4YmM2NjJkZjMwOGY0YTMyNjBhM2FlMjE3Nzc3MDMyMWZlYzp7Il9hdXRoX3VzZXJfaWQiOiIzNCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMDg5MzUyM2Q2OGMyOGIzYjhhMzA3YWI0ZDI2ZjQ4MzY0OTg2NmJkNyJ9', '2021-12-05 07:12:19.566542'),
('ov2d1vbbwl456noauf6ij7p13e658w03', 'M2JmYzI5OTM4MWRhMjE2ODg0Y2I5YzkwNDFiMzFiZjFiN2JmNzBmNDp7fQ==', '2021-11-24 20:41:42.819605');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
 ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
 ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`), ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
 ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
 ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
 ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`), ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
 ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`), ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `charity_benefactorr`
--
ALTER TABLE `charity_benefactorr`
 ADD PRIMARY KEY (`id`), ADD KEY `charity_benefactorr_user_id_a09bd55d_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `charity_benefactor_report`
--
ALTER TABLE `charity_benefactor_report`
 ADD PRIMARY KEY (`id`), ADD KEY `charity_benefactor_r_benefactor_id_id_98b7e36b_fk_charity_b` (`benefactor_id_id`);

--
-- Indexes for table `charity_beneficiary`
--
ALTER TABLE `charity_beneficiary`
 ADD PRIMARY KEY (`id`), ADD KEY `charity_beneficiary_user_id_d8446cd7_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `charity_beneficiary_report`
--
ALTER TABLE `charity_beneficiary_report`
 ADD PRIMARY KEY (`id`), ADD KEY `charity_beneficiary__beneficiary_id_id_76e1a028_fk_charity_b` (`beneficiary_id_id`);

--
-- Indexes for table `charity_feedback`
--
ALTER TABLE `charity_feedback`
 ADD PRIMARY KEY (`id`), ADD KEY `charity_feedback_user_id_31038a71_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `charity_location`
--
ALTER TABLE `charity_location`
 ADD PRIMARY KEY (`id`);

--
-- Indexes for table `charity_product_add`
--
ALTER TABLE `charity_product_add`
 ADD PRIMARY KEY (`id`), ADD KEY `charity_product_add_benefactor_id_8c9851d8_fk_charity_b` (`benefactor_id`), ADD KEY `charity_product_add_volunteer_id_95ea85b9_fk_charity_v` (`volunteer_id`);

--
-- Indexes for table `charity_request_need`
--
ALTER TABLE `charity_request_need`
 ADD PRIMARY KEY (`id`), ADD KEY `charity_request_need_benfi_id_id_9ae2e3fe_fk_charity_b` (`benfi_id_id`), ADD KEY `charity_request_need_volunteer_id_f86708a5_fk_charity_v` (`volunteer_id`);

--
-- Indexes for table `charity_usertype`
--
ALTER TABLE `charity_usertype`
 ADD PRIMARY KEY (`id`), ADD KEY `charity_usertype_user_id_f2d1b3a7_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `charity_volunteer_reg`
--
ALTER TABLE `charity_volunteer_reg`
 ADD PRIMARY KEY (`id`), ADD KEY `charity_volunteer_reg_user_id_a475de56_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
 ADD PRIMARY KEY (`id`), ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`), ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
 ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
 ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
 ADD PRIMARY KEY (`session_key`), ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=65;
--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=50;
--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `charity_benefactorr`
--
ALTER TABLE `charity_benefactorr`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=19;
--
-- AUTO_INCREMENT for table `charity_benefactor_report`
--
ALTER TABLE `charity_benefactor_report`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=10;
--
-- AUTO_INCREMENT for table `charity_beneficiary`
--
ALTER TABLE `charity_beneficiary`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=8;
--
-- AUTO_INCREMENT for table `charity_beneficiary_report`
--
ALTER TABLE `charity_beneficiary_report`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `charity_feedback`
--
ALTER TABLE `charity_feedback`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=7;
--
-- AUTO_INCREMENT for table `charity_location`
--
ALTER TABLE `charity_location`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=6;
--
-- AUTO_INCREMENT for table `charity_product_add`
--
ALTER TABLE `charity_product_add`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=16;
--
-- AUTO_INCREMENT for table `charity_request_need`
--
ALTER TABLE `charity_request_need`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=9;
--
-- AUTO_INCREMENT for table `charity_usertype`
--
ALTER TABLE `charity_usertype`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=29;
--
-- AUTO_INCREMENT for table `charity_volunteer_reg`
--
ALTER TABLE `charity_volunteer_reg`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=8;
--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=17;
--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=37;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `charity_benefactorr`
--
ALTER TABLE `charity_benefactorr`
ADD CONSTRAINT `charity_benefactorr_user_id_a09bd55d_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `charity_benefactor_report`
--
ALTER TABLE `charity_benefactor_report`
ADD CONSTRAINT `charity_benefactor_r_benefactor_id_id_98b7e36b_fk_charity_b` FOREIGN KEY (`benefactor_id_id`) REFERENCES `charity_benefactorr` (`id`);

--
-- Constraints for table `charity_beneficiary`
--
ALTER TABLE `charity_beneficiary`
ADD CONSTRAINT `charity_beneficiary_user_id_d8446cd7_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `charity_beneficiary_report`
--
ALTER TABLE `charity_beneficiary_report`
ADD CONSTRAINT `charity_beneficiary__beneficiary_id_id_76e1a028_fk_charity_b` FOREIGN KEY (`beneficiary_id_id`) REFERENCES `charity_beneficiary` (`id`);

--
-- Constraints for table `charity_feedback`
--
ALTER TABLE `charity_feedback`
ADD CONSTRAINT `charity_feedback_user_id_31038a71_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `charity_product_add`
--
ALTER TABLE `charity_product_add`
ADD CONSTRAINT `charity_product_add_benefactor_id_8c9851d8_fk_charity_b` FOREIGN KEY (`benefactor_id`) REFERENCES `charity_benefactorr` (`id`),
ADD CONSTRAINT `charity_product_add_volunteer_id_95ea85b9_fk_charity_v` FOREIGN KEY (`volunteer_id`) REFERENCES `charity_volunteer_reg` (`id`);

--
-- Constraints for table `charity_request_need`
--
ALTER TABLE `charity_request_need`
ADD CONSTRAINT `charity_request_need_benfi_id_id_9ae2e3fe_fk_charity_b` FOREIGN KEY (`benfi_id_id`) REFERENCES `charity_beneficiary` (`id`),
ADD CONSTRAINT `charity_request_need_volunteer_id_f86708a5_fk_charity_v` FOREIGN KEY (`volunteer_id`) REFERENCES `charity_volunteer_reg` (`id`);

--
-- Constraints for table `charity_usertype`
--
ALTER TABLE `charity_usertype`
ADD CONSTRAINT `charity_usertype_user_id_f2d1b3a7_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `charity_volunteer_reg`
--
ALTER TABLE `charity_volunteer_reg`
ADD CONSTRAINT `charity_volunteer_reg_user_id_a475de56_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
