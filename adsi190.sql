-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 17-02-2022 a las 23:37:23
-- Versión del servidor: 10.4.18-MariaDB
-- Versión de PHP: 7.3.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

--
-- Base de datos: `adsi190`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add marca', 7, 'add_marca'),
(26, 'Can change marca', 7, 'change_marca'),
(27, 'Can delete marca', 7, 'delete_marca'),
(28, 'Can view marca', 7, 'view_marca'),
(29, 'Can add producto', 8, 'add_producto'),
(30, 'Can change producto', 8, 'change_producto'),
(31, 'Can delete producto', 8, 'delete_producto'),
(32, 'Can view producto', 8, 'view_producto');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$260000$8hWLjriBst6uzsHCSle9f1$gTBrihVU0zekpi4+kHDZL500qdmGQTMBRBjOQk+UeOk=', '2022-02-17 22:05:12.136701', 1, 'johnwmartinez', '', '', 'info@johnwmartinez.com', 1, 1, '2021-12-08 00:38:07.844741');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2021-12-08 00:40:43.170586', '1', 'Sin Marca', 1, '[{\"added\": {}}]', 7, 1),
(2, '2021-12-08 00:40:48.394210', '2', 'Teclados', 1, '[{\"added\": {}}]', 7, 1),
(3, '2021-12-08 00:41:14.982269', '1', 'Logitech Mk235, Combo Inalámbrico Teclado Multimedia Y Mouse', 1, '[{\"added\": {}}]', 8, 1),
(4, '2021-12-08 00:42:09.232230', '2', 'Teclado gamer Redragon Kumara K552 QWERTY Outemu Blue español latinoamérica color negro con luz roja', 1, '[{\"added\": {}}]', 8, 1),
(5, '2021-12-08 00:42:35.503292', '3', 'Combo Gamer Teclado Usb Con Ñ + Mouse Óptico Usb Con Luces', 1, '[{\"added\": {}}]', 8, 1),
(6, '2021-12-08 00:43:09.548488', '3', 'Monitor', 1, '[{\"added\": {}}]', 7, 1),
(7, '2021-12-08 00:43:10.895227', '4', 'Monitor gamer Samsung F24T35 led 24 \" azul y gris oscuro 100V/240V', 1, '[{\"added\": {}}]', 8, 1),
(8, '2021-12-08 00:43:31.053905', '5', 'Monitor gamer curvo Samsung C27R500FHL led 27 \" dark blue gray 100V/240V', 1, '[{\"added\": {}}]', 8, 1),
(9, '2022-02-17 22:05:32.503541', '1', '__Logitech Mk235, Combo Inalámbrico Teclado Multimedia Y Mouse', 2, '[{\"changed\": {\"fields\": [\"Nombre\"]}}]', 8, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(7, 'tienda', 'marca'),
(8, 'tienda', 'producto');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2021-12-08 00:35:51.037136'),
(2, 'auth', '0001_initial', '2021-12-08 00:35:51.525998'),
(3, 'admin', '0001_initial', '2021-12-08 00:35:51.639216'),
(4, 'admin', '0002_logentry_remove_auto_add', '2021-12-08 00:35:51.646863'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2021-12-08 00:35:51.656587'),
(6, 'contenttypes', '0002_remove_content_type_name', '2021-12-08 00:35:51.713650'),
(7, 'auth', '0002_alter_permission_name_max_length', '2021-12-08 00:35:51.757752'),
(8, 'auth', '0003_alter_user_email_max_length', '2021-12-08 00:35:51.782248'),
(9, 'auth', '0004_alter_user_username_opts', '2021-12-08 00:35:51.790909'),
(10, 'auth', '0005_alter_user_last_login_null', '2021-12-08 00:35:51.816325'),
(11, 'auth', '0006_require_contenttypes_0002', '2021-12-08 00:35:51.818726'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2021-12-08 00:35:51.826292'),
(13, 'auth', '0008_alter_user_username_max_length', '2021-12-08 00:35:51.853132'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2021-12-08 00:35:51.879656'),
(15, 'auth', '0010_alter_group_name_max_length', '2021-12-08 00:35:51.906499'),
(16, 'auth', '0011_update_proxy_permissions', '2021-12-08 00:35:51.915975'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2021-12-08 00:35:51.946104'),
(18, 'sessions', '0001_initial', '2021-12-08 00:35:51.989747'),
(19, 'tienda', '0001_initial', '2021-12-08 00:40:07.212568');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('6d0sc51hlfrwl1xpge3renvvcajonv0l', '.eJxVjEEOwiAQRe_C2pAOA8i4dO8ZyACjVA1NSrsy3l2bdKHb_977LxV5XWpcu8xxLOqkQB1-t8T5IW0D5c7tNuk8tWUek94UvdOuL1OR53l3_w4q9_qtM8lAJSWPGDx5A0AADu2VgxMxoSCSZaEU0Bv0HET4mEEGZzN5Mer9AcnlN1U:1mukyV:7NqtBdEqU9cCB_C3IUVDZNcXEM2OzmVH3zgDDhk1CFo', '2021-12-22 00:38:23.474126'),
('cbi2dd8lsf5kfcy5vd3salsxd6ja2lx3', '.eJxVjEEOwiAQRe_C2pAOA8i4dO8ZyACjVA1NSrsy3l2bdKHb_977LxV5XWpcu8xxLOqkQB1-t8T5IW0D5c7tNuk8tWUek94UvdOuL1OR53l3_w4q9_qtM8lAJSWPGDx5A0AADu2VgxMxoSCSZaEU0Bv0HET4mEEGZzN5Mer9AcnlN1U:1nKotk:arng3ERJBEzQ7V0eYR5PMyrO5ujRIK0-vF3zvpMTqMc', '2022-03-03 22:05:12.138323');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tienda_marca`
--

CREATE TABLE `tienda_marca` (
  `id` bigint(20) NOT NULL,
  `marca` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tienda_marca`
--

INSERT INTO `tienda_marca` (`id`, `marca`) VALUES
(1, 'Sin Marca'),
(2, 'Teclados'),
(3, 'Monitor');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tienda_producto`
--

CREATE TABLE `tienda_producto` (
  `id` bigint(20) NOT NULL,
  `nombre` varchar(150) NOT NULL,
  `descripcion` longtext NOT NULL,
  `cantidad` bigint(20) UNSIGNED NOT NULL CHECK (`cantidad` >= 0),
  `precio` double NOT NULL,
  `imagen` varchar(100) NOT NULL,
  `id_marca_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tienda_producto`
--

INSERT INTO `tienda_producto` (`id`, `nombre`, `descripcion`, `cantidad`, `precio`, `imagen`, `id_marca_id`) VALUES
(1, '__Logitech Mk235, Combo Inalámbrico Teclado Multimedia Y Mouse', 'Logitech Mk235, Combo Inalámbrico Teclado Multimedia Y Mouse', 10, 99900, 'static/img/productos/teclado1_gT0zGbn.jpg', 2),
(2, 'Teclado gamer Redragon Kumara K552 QWERTY Outemu Blue español latinoamérica color negro con luz roja', 'Teclado gamer Redragon Kumara K552 QWERTY Outemu Blue español latinoamérica color negro con luz roja', 90, 159900, 'static/img/productos/teclado2_JeF4lc2.jpg', 2),
(3, 'Combo Gamer Teclado Usb Con Ñ + Mouse Óptico Usb Con Luces', 'Combo Gamer Teclado Usb Con Ñ + Mouse Óptico Usb Con Luces', 6, 199900, 'static/img/productos/teclado3_Nwia3rZ.jpg', 2),
(4, 'Monitor gamer Samsung F24T35 led 24 \" azul y gris oscuro 100V/240V', 'Monitor gamer Samsung F24T35 led 24 \" azul y gris oscuro 100V/240V', 5, 739900, 'static/img/productos/monitor1_1zHkhJ8.jpg', 3),
(5, 'Monitor gamer curvo Samsung C27R500FHL led 27 \" dark blue gray 100V/240V', 'Monitor gamer curvo Samsung C27R500FHL led 27 \" dark blue gray 100V/240V', 5, 953900, 'static/img/productos/monitor2_UMhXfIm.jpg', 3);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indices de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indices de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indices de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indices de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indices de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indices de la tabla `tienda_marca`
--
ALTER TABLE `tienda_marca`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `tienda_producto`
--
ALTER TABLE `tienda_producto`
  ADD PRIMARY KEY (`id`),
  ADD KEY `tienda_producto_id_marca_id_83167c81_fk_tienda_marca_id` (`id_marca_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT de la tabla `tienda_marca`
--
ALTER TABLE `tienda_marca`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `tienda_producto`
--
ALTER TABLE `tienda_producto`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `tienda_producto`
--
ALTER TABLE `tienda_producto`
  ADD CONSTRAINT `tienda_producto_id_marca_id_83167c81_fk_tienda_marca_id` FOREIGN KEY (`id_marca_id`) REFERENCES `tienda_marca` (`id`);
COMMIT;
