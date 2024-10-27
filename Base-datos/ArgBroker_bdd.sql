-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: arg_broker_demo_bdd
-- ------------------------------------------------------
-- Server version	8.4.0

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
-- Table structure for table `accion`
--

DROP TABLE IF EXISTS `accion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accion` (
  `id_accion` int NOT NULL AUTO_INCREMENT,
  `nombre_accion` varchar(255) DEFAULT NULL,
  `simbolo_accion` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id_accion`),
  UNIQUE KEY `simbolo_empresa` (`simbolo_accion`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accion`
--

LOCK TABLES `accion` WRITE;
/*!40000 ALTER TABLE `accion` DISABLE KEYS */;
INSERT INTO `accion` VALUES (1,'YPF S.A.','YPF'),(2,'Banco Macro S.A.','BMA'),(3,'Grupo Financiero Galicia S.A.','GGAL'),(4,'Telecom Argentina S.A.','TEO'),(5,'Pampa Energía S.A.','PAMP'),(6,'Mercado Libre','MELI'),(7,'Globant','GLOB'),(8,'Tenaris','TS'),(9,'IRSA','IRS'),(10,'Cresud','CRESY');
/*!40000 ALTER TABLE `accion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cotizacion_diaria`
--

DROP TABLE IF EXISTS `cotizacion_diaria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cotizacion_diaria` (
  `id_cotizacion` int NOT NULL AUTO_INCREMENT,
  `id_accion` int NOT NULL,
  `fecha` date NOT NULL,
  `ultimo_operado` decimal(15,2) NOT NULL,
  `cantidad_compra_diaria` int NOT NULL,
  `precio_compra_actual` decimal(15,2) NOT NULL,
  `precio_venta_actual` decimal(15,2) NOT NULL,
  `cantidad_venta_diaria` int NOT NULL,
  `valor_apertura` decimal(15,2) NOT NULL,
  `minimo_diario` decimal(15,2) NOT NULL,
  `maximo_diario` decimal(15,2) NOT NULL,
  `valor_cierre` decimal(15,2) NOT NULL,
  PRIMARY KEY (`id_cotizacion`),
  UNIQUE KEY `id_accion` (`id_accion`,`fecha`),
  CONSTRAINT `cotizacion_diaria_ibfk_1` FOREIGN KEY (`id_accion`) REFERENCES `accion` (`id_accion`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cotizacion_diaria`
--

LOCK TABLES `cotizacion_diaria` WRITE;
/*!40000 ALTER TABLE `cotizacion_diaria` DISABLE KEYS */;
INSERT INTO `cotizacion_diaria` VALUES (1,1,'2023-10-09',650.00,100,645.00,655.00,100,640.00,630.00,660.00,650.00),(2,2,'2023-10-09',350.00,200,345.00,355.00,200,340.00,330.00,360.00,350.00),(3,3,'2023-10-09',450.00,150,445.00,455.00,150,440.00,430.00,460.00,450.00),(4,4,'2023-10-09',200.00,250,195.00,205.00,250,190.00,180.00,210.00,200.00),(5,5,'2023-10-09',300.00,180,295.00,305.00,180,290.00,280.00,310.00,300.00),(6,1,'2024-10-14',640.50,150,645.00,650.00,120,630.00,620.00,655.00,645.50),(7,1,'2024-10-15',642.00,180,648.00,653.00,130,635.00,625.00,660.00,648.50),(8,1,'2024-10-16',643.50,200,650.00,655.00,140,640.00,630.00,665.00,650.50),(9,1,'2024-10-17',655.50,120,655.00,656.00,100,654.00,653.00,657.00,655.50),(10,2,'2024-10-17',352.00,80,351.50,352.50,75,350.00,349.00,353.00,352.00),(11,3,'2024-10-17',452.50,90,452.00,453.00,85,451.00,450.00,454.00,452.50),(12,4,'2024-10-17',202.00,150,201.50,202.50,140,200.00,199.00,203.00,202.00),(13,5,'2024-10-17',302.50,100,302.00,303.00,95,301.00,300.00,304.00,302.50),(14,6,'2024-10-17',1500.00,50,1499.00,1501.00,45,1495.00,1490.00,1505.00,1500.00),(15,7,'2024-10-17',220.00,200,219.50,220.50,180,218.00,217.00,221.00,220.00),(16,8,'2024-10-17',25.50,1000,25.40,25.60,950,25.30,25.20,25.70,25.50),(17,9,'2024-10-17',6.20,5000,6.15,6.25,4800,6.10,6.05,6.30,6.20),(18,10,'2024-10-17',4.80,8000,4.75,4.85,7500,4.70,4.65,4.90,4.80);
/*!40000 ALTER TABLE `cotizacion_diaria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `estado_portafolio`
--

DROP TABLE IF EXISTS `estado_portafolio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `estado_portafolio` (
  `id_estado_portafolio` int NOT NULL AUTO_INCREMENT,
  `id_portafolio` int NOT NULL,
  `id_accion` int NOT NULL,
  `nombre_accion` varchar(255) DEFAULT NULL,
  `simbolo_accion` varchar(10) DEFAULT NULL,
  `cantidad` int NOT NULL,
  `valor_actual` decimal(15,2) NOT NULL,
  PRIMARY KEY (`id_estado_portafolio`),
  KEY `fk_estado_portafolio_portafolio` (`id_portafolio`),
  KEY `fk_estado_portafolio_accion` (`id_accion`),
  CONSTRAINT `fk_estado_portafolio_accion` FOREIGN KEY (`id_accion`) REFERENCES `accion` (`id_accion`),
  CONSTRAINT `fk_estado_portafolio_portafolio` FOREIGN KEY (`id_portafolio`) REFERENCES `portafolio` (`id_portafolio`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estado_portafolio`
--

LOCK TABLES `estado_portafolio` WRITE;
/*!40000 ALTER TABLE `estado_portafolio` DISABLE KEYS */;
INSERT INTO `estado_portafolio` VALUES (1,1,1,'YPF S.A.','YPF',100,65000.00),(2,1,2,'Banco Macro S.A.','BMA',50,17500.00),(3,1,1,'YPF S.A.','YPF',100,65550.00),(4,1,2,'Banco Macro S.A.','BMA',50,17600.00),(5,2,3,'Grupo Financiero Galicia S.A.','GGAL',75,33937.50),(6,2,4,'Telecom Argentina S.A.','TEO',200,40400.00),(7,3,5,'Pampa Energía S.A.','PAMP',150,45375.00),(8,3,6,'Mercado Libre','MELI',30,45000.00),(9,4,7,'Globant','GLOB',100,22000.00),(10,4,8,'Tenaris','TS',500,12750.00),(11,5,9,'IRSA','IRS',2000,12400.00),(12,5,10,'Cresud','CRESY',3000,14400.00);
/*!40000 ALTER TABLE `estado_portafolio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `historial_saldo`
--

DROP TABLE IF EXISTS `historial_saldo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `historial_saldo` (
  `id_historial_saldo` int NOT NULL AUTO_INCREMENT,
  `id_inversor` int NOT NULL,
  `fecha` datetime NOT NULL,
  `saldo_anterior` decimal(15,2) NOT NULL,
  `saldo_nuevo` decimal(15,2) NOT NULL,
  `motivo` varchar(255) NOT NULL,
  PRIMARY KEY (`id_historial_saldo`),
  KEY `id_inversor` (`id_inversor`),
  CONSTRAINT `historial_saldo_ibfk_1` FOREIGN KEY (`id_inversor`) REFERENCES `inversor` (`id_inversor`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `historial_saldo`
--

LOCK TABLES `historial_saldo` WRITE;
/*!40000 ALTER TABLE `historial_saldo` DISABLE KEYS */;
INSERT INTO `historial_saldo` VALUES (1,1,'2024-10-15 09:00:00',1000000.00,935000.00,'compra'),(2,1,'2024-10-15 10:00:00',935000.00,917500.00,'compra'),(3,2,'2024-10-15 11:00:00',750000.00,716250.00,'compra'),(4,2,'2024-10-15 14:00:00',716250.00,676250.00,'compra'),(5,3,'2024-10-16 09:00:00',1200000.00,1155000.00,'compra'),(6,3,'2024-10-16 10:30:00',1155000.00,1110150.00,'compra'),(7,4,'2024-10-16 14:00:00',300000.00,278200.00,'compra'),(8,4,'2024-10-16 15:30:00',278200.00,265550.00,'compra'),(9,5,'2024-10-17 09:45:00',900000.00,887800.00,'compra'),(10,5,'2024-10-17 11:15:00',887800.00,873700.00,'compra');
/*!40000 ALTER TABLE `historial_saldo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inversor`
--

DROP TABLE IF EXISTS `inversor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inversor` (
  `id_inversor` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `cuil` varchar(20) NOT NULL,
  `email` varchar(100) NOT NULL,
  `contrasena` varchar(255) NOT NULL,
  `saldo_cuenta` decimal(15,2) NOT NULL DEFAULT '0.00',
  `intentos_fallidos` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`id_inversor`),
  UNIQUE KEY `cuil` (`cuil`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inversor`
--

LOCK TABLES `inversor` WRITE;
/*!40000 ALTER TABLE `inversor` DISABLE KEYS */;
INSERT INTO `inversor` VALUES (1,'Cristian','Vargas','20362321000','cristian.v62@gmail.com','redcros62',1000000.00,0),(2,'lolo','vargas','20151','cristian.pouls@gmail.com','redcros62',1000000.00,0),(3,'Juan','Perez','20-12345678-9','juan.perez@example.com','12345',10000.00,0),(4,'Maria','Gonzalez','27-98765432-1','maria.gonzalez@gmail.com','12345',500000.00,0),(5,'Carlos','Rodriguez','20-87654321-2','carlos.rodriguez@gmail.com','12345',750000.00,0),(6,'Laura','Fernandez','27-76543210-3','laura.fernandez@gmail.com','12345',1200000.00,0),(7,'Diego','Martinez','20-65432109-4','diego.martinez@gmail.com','12345',300000.00,0),(8,'Ana','Lopez','27-54321098-5','ana.lopez@gmail.com','12345',900000.00,0);
/*!40000 ALTER TABLE `inversor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `portafolio`
--

DROP TABLE IF EXISTS `portafolio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `portafolio` (
  `id_portafolio` int NOT NULL AUTO_INCREMENT,
  `id_inversor` int NOT NULL,
  PRIMARY KEY (`id_portafolio`),
  UNIQUE KEY `id_inversor` (`id_inversor`),
  CONSTRAINT `portafolio_ibfk_1` FOREIGN KEY (`id_inversor`) REFERENCES `inversor` (`id_inversor`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `portafolio`
--

LOCK TABLES `portafolio` WRITE;
/*!40000 ALTER TABLE `portafolio` DISABLE KEYS */;
INSERT INTO `portafolio` VALUES (1,1),(2,2),(3,3),(4,4),(5,5),(6,6);
/*!40000 ALTER TABLE `portafolio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transaccion`
--

DROP TABLE IF EXISTS `transaccion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `transaccion` (
  `id_transaccion` int NOT NULL AUTO_INCREMENT,
  `id_portafolio` int NOT NULL,
  `id_accion` int NOT NULL,
  `cantidad` int NOT NULL,
  `precio` decimal(15,2) NOT NULL,
  `tipo` varchar(10) NOT NULL,
  `fecha` datetime NOT NULL,
  `comision` decimal(15,2) NOT NULL DEFAULT '0.00',
  PRIMARY KEY (`id_transaccion`),
  KEY `fk_transaccion_portafolio` (`id_portafolio`),
  KEY `fk_transaccion_accion` (`id_accion`),
  CONSTRAINT `fk_transaccion_accion` FOREIGN KEY (`id_accion`) REFERENCES `accion` (`id_accion`),
  CONSTRAINT `fk_transaccion_portafolio` FOREIGN KEY (`id_portafolio`) REFERENCES `portafolio` (`id_portafolio`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transaccion`
--

LOCK TABLES `transaccion` WRITE;
/*!40000 ALTER TABLE `transaccion` DISABLE KEYS */;
INSERT INTO `transaccion` VALUES (1,1,1,100,650.00,'compra','2023-10-09 10:00:00',1.50),(2,1,2,50,350.00,'compra','2023-10-09 11:00:00',2.00),(3,1,1,100,650.00,'compra','2024-10-15 09:30:00',1.75),(4,1,2,50,350.00,'compra','2024-10-15 10:15:00',2.25),(5,2,3,75,450.00,'compra','2024-10-15 11:00:00',1.00),(6,2,4,200,200.00,'compra','2024-10-15 13:45:00',3.50),(7,3,5,150,300.00,'compra','2024-10-16 09:00:00',4.00),(8,3,6,30,1495.00,'compra','2024-10-16 10:30:00',4.50),(9,4,7,100,218.00,'compra','2024-10-16 14:00:00',2.00),(10,4,8,500,25.30,'compra','2024-10-16 15:30:00',5.50),(11,5,9,2000,6.10,'compra','2024-10-17 09:45:00',3.00),(12,5,10,3000,4.70,'compra','2024-10-17 11:15:00',2.50);
/*!40000 ALTER TABLE `transaccion` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-10-27  6:04:39
