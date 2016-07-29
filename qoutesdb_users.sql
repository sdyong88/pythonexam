-- MySQL dump 10.13  Distrib 5.7.9, for osx10.9 (x86_64)
--
-- Host: 127.0.0.1    Database: qoutesdb
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
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `alias` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `birthdate` date DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Steven','Steven','sdyong@gmail.com','$2b$12$kB8i9un8.BoWo3804uPVQ.gaBrQ.3uhRpbceP6CQfU0rQazMCqDky','2001-12-11','2016-07-22 09:41:12'),(2,'admin','admin','admin@gmail.com','$2b$12$0G0p6ax1Y8TFg3.Qe1yZUOxmgSYsSNZskbxfsD17jGRif5E1Ya/pe','1111-11-11','2016-07-22 09:53:58'),(3,'mickey','mouse','mouse@gmail.com','$2b$12$T1wJ2uI.DIeHvYFq1U/Jde2KsfRAJy2y3WY4VTfhA9gyr5LhVARCS','1142-11-12','2016-07-22 13:36:29'),(4,'Daffy','Duck','daffy@gmail.com','$2b$12$vmWRdflFb2BS6Vodc1lI0u39qrwE3zRmkNQDjv93i2Mom9.o7FnKq','1212-12-12','2016-07-22 20:59:32'),(5,'Mini','Mouse','mini@gmail.com','$2b$12$7AKdy6uwMf21e6IT2n8QnO3k.ogdv3gNLq4lLBMd09D1kUPAmupBm','1212-04-14','2016-07-22 20:59:48'),(6,'Goofy','goofy','goofy@gmail.com','$2b$12$xfdl1dDASlCxZ36UkqaK6.UhMpdezYkV9PhCtU3wO92vruqsLrmvC','1212-12-12','2016-07-22 21:00:19');
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

-- Dump completed on 2016-07-26  7:47:35
