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
  `nuls` int DEFAULT NULL,
  `ratiovd` float DEFAULT NULL,
  `classement` int DEFAULT NULL,
  `points` int NOT NULL,
  PRIMARY KEY (`idJoueur`),
  UNIQUE KEY `stat_id_UNIQUE` (`idJoueur`),
  UNIQUE KEY `classement_UNIQUE` (`classement`),
  CONSTRAINT `joueur` FOREIGN KEY (`idJoueur`) REFERENCES `joueur` (`idJoueur`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `statistiques`
--

LOCK TABLES `statistiques` WRITE;
/*!40000 ALTER TABLE `statistiques` DISABLE KEYS */;
INSERT INTO `statistiques` VALUES (1,0,0,0,0,NULL,NULL,0),(2,0,0,0,0,NULL,NULL,0),(6,0,0,0,0,0,NULL,0),(24,0,0,0,0,0,NULL,0),(25,0,0,0,0,0,NULL,0),(26,0,0,0,0,0,NULL,0);
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

-- Dump completed on 2023-05-25 21:10:20
