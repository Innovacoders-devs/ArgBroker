-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: arg_broker_bdd
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
  `nombre_empresa` varchar(100) NOT NULL,
  `simbolo_empresa` varchar(10) NOT NULL,
  PRIMARY KEY (`id_accion`),
  UNIQUE KEY `simbolo_empresa` (`simbolo_empresa`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accion`
--

LOCK TABLES `accion` WRITE;
/*!40000 ALTER TABLE `accion` DISABLE KEYS */;
INSERT INTO `accion` VALUES (1,'YPF S.A.','YPF'),(2,'Banco Macro S.A.','BMA'),(3,'Grupo Financiero Galicia S.A.','GGAL'),(4,'Telecom Argentina S.A.','TEO'),(5,'Pampa Energía S.A.','PAMP');
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
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cotizacion_diaria`
--

LOCK TABLES `cotizacion_diaria` WRITE;
/*!40000 ALTER TABLE `cotizacion_diaria` DISABLE KEYS */;
INSERT INTO `cotizacion_diaria` VALUES (1,1,'2023-10-09',650.00,100,645.00,655.00,100,640.00,630.00,660.00,650.00),(2,2,'2023-10-09',350.00,200,345.00,355.00,200,340.00,330.00,360.00,350.00),(3,3,'2023-10-09',450.00,150,445.00,455.00,150,440.00,430.00,460.00,450.00),(4,4,'2023-10-09',200.00,250,195.00,205.00,250,190.00,180.00,210.00,200.00),(5,5,'2023-10-09',300.00,180,295.00,305.00,180,290.00,280.00,310.00,300.00);
/*!40000 ALTER TABLE `cotizacion_diaria` ENABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `historial_saldo`
--

LOCK TABLES `historial_saldo` WRITE;
/*!40000 ALTER TABLE `historial_saldo` DISABLE KEYS */;
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
  `direccion` varchar(255) DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `perfil_inversor` varchar(50) DEFAULT NULL,
  `intentos_fallidos` int NOT NULL DEFAULT '0',
  `bloqueado` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id_inversor`),
  UNIQUE KEY `cuil` (`cuil`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inversor`
--

LOCK TABLES `inversor` WRITE;
/*!40000 ALTER TABLE `inversor` DISABLE KEYS */;
INSERT INTO `inversor` VALUES (1,'Cristian','Vargas','20362321000','cristian.v62@gmail.com','redcros62',1000000.00,'eduardo maldonado 1188','3517883811','',0,0),(2,'lolo','vargas','20151','cristian.pouls@gmail.com','redcros62',1000000.00,NULL,NULL,NULL,0,0);
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
  `id_accion` int NOT NULL,
  `cantidad` int NOT NULL,
  `precio_promedio_compra` decimal(15,2) NOT NULL,
  PRIMARY KEY (`id_portafolio`),
  UNIQUE KEY `id_inversor` (`id_inversor`,`id_accion`),
  KEY `id_accion` (`id_accion`),
  CONSTRAINT `portafolio_ibfk_1` FOREIGN KEY (`id_inversor`) REFERENCES `inversor` (`id_inversor`),
  CONSTRAINT `portafolio_ibfk_2` FOREIGN KEY (`id_accion`) REFERENCES `accion` (`id_accion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `portafolio`
--

LOCK TABLES `portafolio` WRITE;
/*!40000 ALTER TABLE `portafolio` DISABLE KEYS */;
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
  `id_inversor` int NOT NULL,
  `id_accion` int NOT NULL,
  `tipo` enum('compra','venta') NOT NULL,
  `fecha` datetime NOT NULL,
  `precio` decimal(15,2) NOT NULL,
  `cantidad` int NOT NULL,
  `comision` decimal(15,2) NOT NULL,
  PRIMARY KEY (`id_transaccion`),
  KEY `id_inversor` (`id_inversor`),
  KEY `id_accion` (`id_accion`),
  CONSTRAINT `transaccion_ibfk_1` FOREIGN KEY (`id_inversor`) REFERENCES `inversor` (`id_inversor`),
  CONSTRAINT `transaccion_ibfk_2` FOREIGN KEY (`id_accion`) REFERENCES `accion` (`id_accion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transaccion`
--

LOCK TABLES `transaccion` WRITE;
/*!40000 ALTER TABLE `transaccion` DISABLE KEYS */;
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

-- Dump completed on 2024-10-09 21:18:49
