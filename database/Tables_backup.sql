/*
SQLyog - Free MySQL GUI v5.17
Host - 8.0.33 : Database - sbibank
*********************************************************************
Server version : 8.0.33
*/

SET NAMES utf8;

SET SQL_MODE='';

create database if not exists `sbibank`;

USE `sbibank`;

SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO';

/*Table structure for table `tblaccount` */

DROP TABLE IF EXISTS `tblaccount`;

CREATE TABLE `tblaccount` (
  `accno` int NOT NULL,
  `cname` varchar(50) DEFAULT NULL,
  `cadd` varchar(50) DEFAULT NULL,
  `cgen` varchar(50) DEFAULT NULL,
  `cmob` varchar(50) DEFAULT NULL,
  `odate` varchar(50) DEFAULT NULL,
  `balance` int DEFAULT NULL,
  PRIMARY KEY (`accno`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `tblaccount` */

insert into `tblaccount` (`accno`,`cname`,`cadd`,`cgen`,`cmob`,`odate`,`balance`) values (1,'Usha','fzr','Female','9417784569','11-05-2023',901),(2,'Mukesh','chd','Male','9811236478','11-07-2020',2599);

/*Table structure for table `tbladmin` */

DROP TABLE IF EXISTS `tbladmin`;

CREATE TABLE `tbladmin` (
  `admid` varchar(50) NOT NULL,
  `admpwd` varchar(50) DEFAULT NULL,
  `admsecques` varchar(50) DEFAULT NULL,
  `admsecans` varchar(50) DEFAULT NULL,
  `admname` varchar(50) DEFAULT NULL,
  `admadd` varchar(50) DEFAULT NULL,
  `admemail` varchar(50) DEFAULT NULL,
  `admphno` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`admid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `tbladmin` */

insert into `tbladmin` (`admid`,`admpwd`,`admsecques`,`admsecans`,`admname`,`admadd`,`admemail`,`admphno`) values ('hitin','hitin','Place of Birth','fzr','hitin','fzr','hitin161@gmail.com','9781615555');

/*Table structure for table `tbltransaction` */

DROP TABLE IF EXISTS `tbltransaction`;

CREATE TABLE `tbltransaction` (
  `transid` int NOT NULL,
  `transsrcaccno` int DEFAULT NULL,
  `transdestaccno` int DEFAULT NULL,
  `transtype` varchar(50) DEFAULT NULL,
  `transamt` int DEFAULT NULL,
  `transdate` varchar(50) DEFAULT NULL,
  `transtime` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`transid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `tbltransaction` */

insert into `tbltransaction` (`transid`,`transsrcaccno`,`transdestaccno`,`transtype`,`transamt`,`transdate`,`transtime`) values (1,1,NULL,'Deposit',500,'07/07/2023','09:36:02'),(2,1,NULL,'Withdraw',100,'07/07/2023','10:00:09'),(3,1,NULL,'Deposit',100,'07/07/2023','10:49:41'),(4,2,1,'Transfer',500,'07/07/2023','11:15:14'),(5,1,2,'Transfer',99,'10/07/2023','10:54:10');

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
