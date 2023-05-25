-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: sudoku
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `joueur`
--

DROP TABLE IF EXISTS `joueur`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `joueur` (
  `idJoueur` int NOT NULL AUTO_INCREMENT,
  `pseudo` varchar(45) NOT NULL,
  `mdp` text NOT NULL COMMENT 'Crypté',
  `date_inscription` datetime NOT NULL,
  PRIMARY KEY (`idJoueur`),
  UNIQUE KEY `idJoueur_UNIQUE` (`idJoueur`),
  UNIQUE KEY `pseudo_UNIQUE` (`pseudo`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `joueur`
--

LOCK TABLES `joueur` WRITE;
/*!40000 ALTER TABLE `joueur` DISABLE KEYS */;
INSERT INTO `joueur` VALUES (1,'simple1','mdp1','2023-05-11 09:04:00'),(2,'simple2','mdp2','2023-05-11 09:04:00'),(4,'simple3','mdp3','2023-05-11 09:04:00'),(5,'simple4','mdp4','2023-05-11 09:04:00'),(6,'simple5','mdp5','2023-05-11 09:04:00'),(12,'simple6','mdp6','2023-05-11 09:04:00'),(14,'Benoit','mdp','2023-05-16 18:37:21'),(15,'Bg','mdpbien','2023-05-16 18:48:00'),(17,'Bg2','mdpbien','2023-05-16 18:50:45'),(19,'Bg3','mdpbien','2023-05-16 18:52:06'),(20,'Bg4','mdpbien','2023-05-19 18:32:59'),(24,'Bg6','mdpbien','2023-05-19 18:39:14'),(25,'Bg7','mdpbien','2023-05-19 19:00:28'),(26,'Bg8','mdpbien','2023-05-19 19:43:34');
/*!40000 ALTER TABLE `joueur` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-25 21:10:20
