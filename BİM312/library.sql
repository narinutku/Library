-- MySQL dump 10.13  Distrib 8.0.20, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: library
-- ------------------------------------------------------
-- Server version	8.0.20

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
-- Table structure for table `barrowed`
--

DROP TABLE IF EXISTS `barrowed`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `barrowed` (
  `userid` int NOT NULL,
  `bookid` int NOT NULL,
  `issuedate` date NOT NULL,
  `returndate` date NOT NULL,
  PRIMARY KEY (`userid`,`bookid`),
  KEY `barrowed_ibfk_1` (`bookid`),
  CONSTRAINT `barrowed_ibfk_1` FOREIGN KEY (`bookid`) REFERENCES `book` (`id`),
  CONSTRAINT `barrowed_ibfk_2` FOREIGN KEY (`userid`) REFERENCES `member` (`idMember`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `barrowed`
--

LOCK TABLES `barrowed` WRITE;
/*!40000 ALTER TABLE `barrowed` DISABLE KEYS */;
INSERT INTO `barrowed` VALUES (1,2,'2020-06-01','2020-06-16'),(1,54,'2020-06-01','2020-06-16'),(8,53,'2020-06-01','2020-06-16'),(8,56,'2020-06-01','2020-06-16'),(9,55,'2020-06-01','2020-06-16'),(9,73,'2020-06-01','2020-06-16');
/*!40000 ALTER TABLE `barrowed` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `book`
--

DROP TABLE IF EXISTS `book`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `book` (
  `id` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(45) NOT NULL,
  `Author` varchar(45) NOT NULL,
  `Genre` varchar(45) NOT NULL,
  `PublishingHouse` varchar(45) NOT NULL,
  `PublicationDate` date NOT NULL,
  `Language` varchar(45) NOT NULL,
  `NumberofCopies` int NOT NULL DEFAULT '1',
  `Availabity` varchar(45) NOT NULL DEFAULT 'Yes',
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=74 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book`
--

LOCK TABLES `book` WRITE;
/*!40000 ALTER TABLE `book` DISABLE KEYS */;
INSERT INTO `book` VALUES (1,'Lord of The Ring:The Fellowship of the Ring','Tolkien','Fantasy','YKY','0000-00-00','English',1,'Yes'),(2,'yabancı','albertcamus','classic','canyayınları','1982-10-10','turkish',1,'No'),(34,'Suc ve Ceza','Dostoyevski','Classic','İs Bankası','0000-00-00','English',1,'Yes'),(35,'Bir İdam Mahkumunun Son Günü','Victor Hugo','Classic','İs Bankası','0000-00-00','Turkish',2,'Yes'),(36,'Beyaz Geceler','Dostoyevski','Classic','İs Bankası','0000-00-00','French',1,'Yes'),(38,'İstanbul Seyahatnamesi','İlber Ortaylı','Gezi','Kronik Kitap','0000-00-00','Turkish',2,'Yes'),(39,'Yüzyıllık Yalnızlık','Marquez','Dram','Can yayınları','0000-00-00','Turkish',1,'Yes'),(40,'yabancı','albertcamus','classic','canyayınları','1982-10-10','turkish',1,'Yes'),(44,'Yeraltından Notlar','Dostoyevski','Classic','İs Bankası','2015-07-06','turkish',1,'Yes'),(45,'Dünyanın merkezine yolculuk','Victor Hugo','Classic','İs Bankası','2010-02-02','turkish',1,'Yes'),(46,'Karamazov Kardeşler','Dostoyevski','Classic','İs Bankası','2019-01-03','tukrish',2,'Yes'),(47,'Great Gatsby','F. Scott Fitzgerald','American Classic','İs Bankası','2015-05-22','english',1,'Yes'),(48,'Cumhuriyetin 100 yılı','İlber Ortaylı','tarih','Kronik Kitap','2012-03-03','turkish',2,'Yes'),(49,'Kırmızı Pazartesi','Marquez','Dram','Can yayınları','2015-08-09','turkish',1,'Yes'),(50,'yabancı','albertcamus','classic','YKY','1982-10-10','turkish',1,'Yes'),(51,'Şu Çılgın Türkler','Turgut Özakman','Tarih','Bilgi Yayınevi','2005-07-06','Turkish',1,'Yes'),(52,'Denizlar Altında 20000 Fersah','Jules Verne','Classic','İs Bankası','2000-02-02','turkish',1,'Yes'),(53,'İnce Mehmed','Yaşar Kemal','Türk Klasikleri','YKY','2019-01-03','turkish',1,'No'),(54,'Ağrı Dağı Efsanesi','Yaşar Kemal','Türk Klasikleri','YKY','2012-01-03','turkish',1,'No'),(55,'İnce Mehmed 2','Yaşar Kemal','Türk Klasikleri','YKY','2013-01-03','turkish',1,'No'),(56,'İnce Mehmed 3','Yaşar Kemal','Türk Klasikleri','YKY','2014-01-03','turkish',1,'No'),(57,'İnce Mehmed 4','Yaşar Kemal','Türk Klasikleri','YKY','2015-01-03','turkish',1,'Yes'),(58,'Felatun Bey ile Rakım Efendi','Ahmet Mithad','Türk Klasikleri','İş Bankası','2019-01-03','turkish',1,'Yes'),(59,'Efsuncu Baba','Hüseyin Rahmi Gürpınar','Türk Klasikleri','İş Bankası','2019-01-03','turkish',1,'Yes'),(60,'Sefiller','Victor Hugo','Classic','İs Bankası','2000-02-02','turkish',1,'Yes'),(61,'Notre Dame\'ın Kamburu','Victor Hugo','Classic','İs Bankası','2000-02-02','turkish',1,'Yes'),(62,'1984','George Orwell','Classic','Can Yayınları','2010-02-02','turkish',1,'Yes'),(63,'Nineteen Eighty-four','George Orwell','Classic','Can Yayınları','2010-02-02','english',1,'Yes'),(64,'Hayvan Çiftliği','George Orwell','Classic','Can Yayınları','2010-02-02','turkish',1,'Yes'),(65,'Paris ve Lonra\'da Beş Parasız','George Orwell','Classic','Can Yayınları','2010-02-02','turkish',1,'Yes'),(66,'Benjamin Button\'ın Tuhaf Hikayesi','F. Scott Fitzgerald','American Classic','İs Bankası','2018-05-22','english',1,'Yes'),(67,'Bir Ömür Nasıl Yaşanır ','İlber Ortaylı','Tarih','Kronik Kitap','2020-03-03','turkish',1,'Yes'),(68,'Türklerin Tarihi ','İlber Ortaylı','Tarih','Kronik Kitap','2017-03-03','turkish',1,'Yes'),(69,'Türklerin Tarihi 2','İlber Ortaylı','Tarih','Kronik Kitap','2018-03-03','turkish',1,'Yes'),(70,'Türklerin Altın Çağı ','İlber Ortaylı','Tarih','Kronik Kitap','2019-03-03','turkish',1,'Yes'),(71,'İmparatorluğun En Uzun Yüzyılı','İlber Ortaylı','Tarih','Kronik Kitap','2014-03-03','turkish',1,'Yes'),(72,'Kolera Günlerinde Aşk','Gabriel García Márquez','Dram','Can yayınları','2015-08-09','turkish',1,'Yes'),(73,'Dava','albertcamus','classic','YKY','1982-10-10','turkish',1,'No');
/*!40000 ALTER TABLE `book` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `keeps`
--

DROP TABLE IF EXISTS `keeps`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `keeps` (
  `reportno` int NOT NULL,
  `librarianno` int NOT NULL,
  PRIMARY KEY (`librarianno`,`reportno`),
  KEY `reportno` (`reportno`),
  CONSTRAINT `keeps_ibfk_1` FOREIGN KEY (`reportno`) REFERENCES `reports` (`idReports`),
  CONSTRAINT `keeps_ibfk_2` FOREIGN KEY (`librarianno`) REFERENCES `librarian` (`idLibrarian`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `keeps`
--

LOCK TABLES `keeps` WRITE;
/*!40000 ALTER TABLE `keeps` DISABLE KEYS */;
INSERT INTO `keeps` VALUES (1,1),(1,2),(2,2);
/*!40000 ALTER TABLE `keeps` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `librarian`
--

DROP TABLE IF EXISTS `librarian`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `librarian` (
  `idLibrarian` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(45) NOT NULL,
  `Phone Number` varchar(12) NOT NULL,
  PRIMARY KEY (`idLibrarian`),
  UNIQUE KEY `idLibrarian_UNIQUE` (`idLibrarian`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `librarian`
--

LOCK TABLES `librarian` WRITE;
/*!40000 ALTER TABLE `librarian` DISABLE KEYS */;
INSERT INTO `librarian` VALUES (1,'Utku','12345'),(2,'Batuhan','58562');
/*!40000 ALTER TABLE `librarian` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `maintains`
--

DROP TABLE IF EXISTS `maintains`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `maintains` (
  `librarianid` int NOT NULL,
  `bookid` int NOT NULL,
  PRIMARY KEY (`librarianid`,`bookid`),
  KEY `bookid` (`bookid`),
  CONSTRAINT `maintains_ibfk_1` FOREIGN KEY (`librarianid`) REFERENCES `librarian` (`idLibrarian`),
  CONSTRAINT `maintains_ibfk_2` FOREIGN KEY (`bookid`) REFERENCES `book` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `maintains`
--

LOCK TABLES `maintains` WRITE;
/*!40000 ALTER TABLE `maintains` DISABLE KEYS */;
INSERT INTO `maintains` VALUES (1,1),(1,2),(1,35),(1,54),(2,55),(1,58),(2,59),(1,61),(1,62),(2,66);
/*!40000 ALTER TABLE `maintains` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `member`
--

DROP TABLE IF EXISTS `member`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `member` (
  `idMember` int NOT NULL AUTO_INCREMENT,
  `FullName` varchar(45) NOT NULL,
  `Address` varchar(120) NOT NULL,
  `PhoneNumber` varchar(12) NOT NULL,
  `EMail` varchar(45) NOT NULL,
  `DateofBirth` date NOT NULL,
  `NumberofHavingBooks` int DEFAULT '0',
  PRIMARY KEY (`idMember`),
  UNIQUE KEY `idMember_UNIQUE` (`idMember`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member`
--

LOCK TABLES `member` WRITE;
/*!40000 ALTER TABLE `member` DISABLE KEYS */;
INSERT INTO `member` VALUES (1,'Utku Narin','Edirne','1234','1234@1234','1982-10-10',2),(2,'Tefik Uygun','Eskişehir','123456789','123456@gmail.com','1999-10-10',0),(3,'Gizem','Eskişehir','123456789','123456@gmail.com','1999-10-10',0),(4,'Erkut','Edirne','123456789','123456@gmail.com','1999-01-18',0),(5,'Murathan','İstanbul','123456789','123456@gmail.com','1999-01-18',0),(6,'Baran','İstanbul','123456789','123456@gmail.com','1999-01-18',0),(7,'Umut Engincan','İzmir','123456789','123456@gmail.com','1998-01-18',0),(8,'Alper Sahillioğlu','Hatay','123456789','123456@gmail.com','1999-01-18',2),(9,'Zeki Çolak','Ankara','123456789','123456@gmail.com','1999-08-14',2),(10,'Batuhan Kiraz','Muğla','123456789','123456@gmail.com','1999-08-14',0),(11,'Furkan','Eskişehir','123456789','123456@gmail.com','1999-08-14',0),(12,'Özlem','Kırklareli','123456789','123456@gmail.com','1999-08-14',0),(13,'Seray','Edirne','123456789','123456@gmail.com','1999-08-14',0),(14,'Onur','Adana','123456789','123456@gmail.com','1999-08-14',0),(15,'Bush','Usa','1649616','asas','2000-01-01',0),(16,'Tarkan','İSTANBUL','123457','tarkan@gmail.com','1996-01-01',0),(31,'Donald Trump','WhiteHouse','69555','trump@gmail.com','1954-01-01',0),(49,'Leonardo Caprio','La','4964196','leo@gmail.com','2000-01-01',0),(50,'EXAMPLE','Eskisehir','123695','example@gmail.com','2000-01-01',0);
/*!40000 ALTER TABLE `member` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reports`
--

DROP TABLE IF EXISTS `reports`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reports` (
  `idReports` int NOT NULL AUTO_INCREMENT,
  `Reason` varchar(120) NOT NULL,
  `ConditionofBooks` varchar(120) NOT NULL,
  PRIMARY KEY (`idReports`),
  UNIQUE KEY `idReports_UNIQUE` (`idReports`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reports`
--

LOCK TABLES `reports` WRITE;
/*!40000 ALTER TABLE `reports` DISABLE KEYS */;
INSERT INTO `reports` VALUES (1,'User harm book','bad'),(2,'Some papers is tear','unusable'),(26,'yenileme','iyi'),(27,'User lost book','solved'),(29,'Lost','unknown');
/*!40000 ALTER TABLE `reports` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-06-01 18:51:42
