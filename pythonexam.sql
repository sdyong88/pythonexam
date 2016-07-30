CREATE DATABASE  IF NOT EXISTS `pythonbeltdb` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `pythonbeltdb`;
-- MySQL dump 10.13  Distrib 5.7.9, for osx10.9 (x86_64)
--
-- Host: 127.0.0.1    Database: pythonbeltdb
-- ------------------------------------------------------
-- Server version	5.5.42

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `planned`
--

DROP TABLE IF EXISTS `planned`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `planned` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `trip_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_favorites_users_idx` (`user_id`),
  KEY `fk_planned_trips1_idx` (`trip_id`),
  CONSTRAINT `fk_favorites_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_planned_trips1` FOREIGN KEY (`trip_id`) REFERENCES `trips` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `planned`
--

LOCK TABLES `planned` WRITE;
/*!40000 ALTER TABLE `planned` DISABLE KEYS */;
INSERT INTO `planned` VALUES (1,1,7),(2,3,7),(3,3,3),(4,4,2),(5,4,6),(6,4,3),(7,4,7),(8,4,8);
/*!40000 ALTER TABLE `planned` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trips`
--

DROP TABLE IF EXISTS `trips`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `trips` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `destination` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `start` date DEFAULT NULL,
  `finish` date DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_trips_users1_idx` (`user_id`),
  CONSTRAINT `fk_trips_users1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trips`
--

LOCK TABLES `trips` WRITE;
/*!40000 ALTER TABLE `trips` DISABLE KEYS */;
INSERT INTO `trips` VALUES (2,'apan','eatfood','0000-00-00','0000-00-00','2016-07-30 12:31:53','2016-07-30 12:31:53',1),(3,'china','eatfood','0000-00-00','0000-00-00','0000-00-00 00:00:00','0000-00-00 00:00:00',2),(6,'sweeden','eat other food','0000-00-00','0000-00-00','0000-00-00 00:00:00','0000-00-00 00:00:00',1),(7,'Korea','Koreanfood',NULL,NULL,'0000-00-00 00:00:00','0000-00-00 00:00:00',3),(8,'Canada','Play some Hockey','2016-07-01','2016-07-31','2016-07-30 14:37:17','2016-07-30 14:37:17',3);
/*!40000 ALTER TABLE `trips` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `username` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Steven','Steven','steven@gmail.com','$2b$12$tT6i2fZOGuNEXzxGpNjWMODxLt5DQ/eOpsANNMqCZEkvr.fFXXfqa','2016-07-30 11:35:17','2016-07-30 11:35:17'),(2,'Steven','Steven','steven@gmail.com','$2b$12$Q20YW9B2jomCKQnDCXwvUeT8g7JbVmRCEGTqhxQqltn5ZNjErSDbS','2016-07-30 11:35:28','2016-07-30 11:35:28'),(3,'Melissa','Melissa','melissa@gmail.com','$2b$12$HTucSf2F8VqKKHp1dVsRPuY1FzAS4LLBeKnk/1oyWYyTvi7grrj8W','2016-07-30 13:02:17','2016-07-30 13:02:17'),(4,'Kevin','Kevin','kevin@gmail.com','$2b$12$Z6ctrktXmupcXgn1JKCcG.Lctj2l6WEF2LJ3j/f5Pf0zXlM5zjRm2','2016-07-30 14:37:41','2016-07-30 14:37:41');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-07-30 15:20:47
