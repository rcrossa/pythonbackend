CREATE TABLE `movies` (
  `id_movie` int NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `director` varchar(150) DEFAULT NULL,
  `rating` varchar(200) DEFAULT NULL,
  `release_date` date DEFAULT NULL,
  `banner` varchar(255) DEFAULT NULL,
  `deleted` tinyint DEFAULT '0',
  PRIMARY KEY (`id_movie`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;