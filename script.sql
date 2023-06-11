-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: sudoku
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `sudoku`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `sudoku` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `sudoku`;

--
-- Table structure for table `grille`
--

DROP TABLE IF EXISTS `grille`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `grille` (
  `idgrille` int NOT NULL,
  `board` text NOT NULL,
  `solution` text,
  `difficulté` int DEFAULT NULL,
  PRIMARY KEY (`idgrille`),
  UNIQUE KEY `idgrille_UNIQUE` (`idgrille`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `grille`
--

LOCK TABLES `grille` WRITE;
/*!40000 ALTER TABLE `grille` DISABLE KEYS */;
INSERT INTO `grille` VALUES (0,'([None, None, 9, None, None, None, None, 1, 4], [1, None, 4, None, None, None, 6, 5, 2], [None, 3, 5, None, 2, None, None, None, 8], [None, 5, 7, None, 3, 1, 2, 6, 9], [None, 6, None, None, None, None, None, 3, None], [3, None, None, None, None, 2, None, 8, None], [None, None, 8, None, 9, None, None, 2, 1], [9, None, None, 7, None, None, 8, None, None], [None, 1, None, None, None, 8, None, None, None])','NULL',0);
/*!40000 ALTER TABLE `grille` ENABLE KEYS */;
UNLOCK TABLES;

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
) ENGINE=InnoDB AUTO_INCREMENT=50 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `joueur`
--

LOCK TABLES `joueur` WRITE;
/*!40000 ALTER TABLE `joueur` DISABLE KEYS */;
INSERT INTO `joueur` VALUES (1,'simple1','mdp1','2023-05-11 09:04:00'),(2,'simple2','mdp2','2023-05-11 09:04:00'),(4,'simple3','mdp3','2023-05-11 09:04:00'),(5,'simple4','mdp4','2023-05-11 09:04:00'),(6,'simple5','mdp5','2023-05-11 09:04:00'),(12,'simple6','mdp6','2023-05-11 09:04:00'),(14,'Benoit','mdp','2023-05-16 18:37:21'),(15,'Bg','mdpbien','2023-05-16 18:48:00'),(17,'Bg2','mdpbien','2023-05-16 18:50:45'),(19,'Bg3','mdpbien','2023-05-16 18:52:06'),(20,'Bg4','mdpbien','2023-05-19 18:32:59'),(24,'Bg6','mdpbien','2023-05-19 18:39:14'),(25,'Bg7','mdpbien','2023-05-19 19:00:28'),(26,'Bg8','mdpbien','2023-05-19 19:43:34'),(28,'test','test','2023-06-05 10:26:18'),(37,'coucou','coucou','2023-06-08 19:23:53'),(38,'nouveau','nouveau','2023-06-10 00:06:50'),(39,'testn','testn','2023-06-10 00:09:58'),(40,'crypte','crypte','2023-06-10 00:13:15'),(41,'crypter','crypter','2023-06-10 00:15:44'),(42,'nv','nv','2023-06-10 00:16:27'),(43,'cry','cry','2023-06-10 11:17:22'),(44,'user0','user0','2023-06-10 11:20:00'),(45,'user01','user01','2023-06-10 11:22:55'),(46,'user1','user1','2023-06-10 11:28:13'),(48,'gtg','gfeg','2023-06-11 11:32:06'),(49,'admin','admin','2023-06-11 11:45:17');
/*!40000 ALTER TABLE `joueur` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `parties`
--

DROP TABLE IF EXISTS `parties`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `parties` (
  `idparties` int NOT NULL,
  `date` datetime DEFAULT NULL,
  `durée_sec` int NOT NULL,
  `idjoueurgagne` int NOT NULL,
  `grille` int DEFAULT NULL,
  PRIMARY KEY (`idparties`),
  UNIQUE KEY `idparties_UNIQUE` (`idparties`),
  UNIQUE KEY `idjoueurgagne_UNIQUE` (`idjoueurgagne`),
  KEY `grille_idx` (`grille`),
  CONSTRAINT `grille` FOREIGN KEY (`grille`) REFERENCES `grille` (`idgrille`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `parties`
--

LOCK TABLES `parties` WRITE;
/*!40000 ALTER TABLE `parties` DISABLE KEYS */;
/*!40000 ALTER TABLE `parties` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `statistiques`
--

DROP TABLE IF EXISTS `statistiques`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `statistiques` (
  `idJoueur` int NOT NULL,
  `nbparties` int DEFAULT NULL,
  `victoires` int DEFAULT NULL,
  `défaites` int DEFAULT NULL,
  `ratiovd` float DEFAULT NULL,
  `classement` int DEFAULT NULL,
  `points` int NOT NULL,
  PRIMARY KEY (`idJoueur`),
  UNIQUE KEY `stat_id_UNIQUE` (`idJoueur`),
  CONSTRAINT `joueur` FOREIGN KEY (`idJoueur`) REFERENCES `joueur` (`idJoueur`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `statistiques`
--

LOCK TABLES `statistiques` WRITE;
/*!40000 ALTER TABLE `statistiques` DISABLE KEYS */;
INSERT INTO `statistiques` VALUES (1,0,0,4,NULL,1,0),(2,0,0,4,NULL,2,0),(6,0,0,4,0,3,0),(24,0,0,4,0,4,0),(25,11,23,21,1.09524,18,-37),(26,0,0,4,0,5,0),(37,0,0,6,0,6,0),(38,0,0,0,0,7,0),(39,0,0,0,0,8,0),(40,0,0,0,0,9,0),(41,0,0,0,0,10,0),(42,0,0,0,0,11,0),(43,0,0,0,0,12,0),(44,0,0,0,0,13,0),(45,0,0,0,0,14,0),(46,0,0,0,0,15,0),(48,0,0,0,0,16,0),(49,6,1,5,0.2,17,-11);
/*!40000 ALTER TABLE `statistiques` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-11 12:53:09
