-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 24, 2021 at 05:13 AM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `flaskapp`
--

-- --------------------------------------------------------

--
-- Table structure for table `useradmin`
--

CREATE TABLE `useradmin` (
  `sno` int(100) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `datetime` datetime NOT NULL DEFAULT current_timestamp(),
  `firstName` varchar(30) NOT NULL,
  `middleName` varchar(30) NOT NULL,
  `lastName` varchar(30) NOT NULL,
  `gender` varchar(15) NOT NULL,
  `dateOfBirth` date DEFAULT NULL,
  `mobileNo` int(12) NOT NULL,
  `emailID` varchar(30) NOT NULL,
  `designation` varchar(30) NOT NULL,
  `pinCode` int(10) NOT NULL,
  `houseNo` varchar(10) NOT NULL,
  `address` varchar(40) NOT NULL,
  `city` varchar(20) NOT NULL,
  `state` varchar(20) NOT NULL,
  `ifscCode` varchar(20) NOT NULL,
  `accountNo` varchar(30) NOT NULL,
  `bankName` varchar(40) NOT NULL,
  `branchName` varchar(30) NOT NULL,
  `panNo` varchar(15) NOT NULL,
  `qualificaton` varchar(30) NOT NULL,
  `dateOfJoin` date DEFAULT NULL,
  `contractType` varchar(20) NOT NULL,
  `salary` decimal(10,2) NOT NULL,
  `workShift` varchar(20) NOT NULL,
  `permission` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `useradmin`
--

INSERT INTO `useradmin` (`sno`, `username`, `password`, `datetime`, `firstName`, `middleName`, `lastName`, `gender`, `dateOfBirth`, `mobileNo`, `emailID`, `designation`, `pinCode`, `houseNo`, `address`, `city`, `state`, `ifscCode`, `accountNo`, `bankName`, `branchName`, `panNo`, `qualificaton`, `dateOfJoin`, `contractType`, `salary`, `workShift`, `permission`) VALUES
(24, 'satvik2021', '111111', '2021-10-20 09:49:05', 'satvik', 'ddff', 'dfsddffd', 'Male', '2021-10-12', 454548715, 'dfds.sf@gmail.com', 'vice principle', 34324, '234', 'dsadf dsfas', 'ddsf', 'sdfsdf', 'dfd34234', '3343244', 'fdf dfd', 'dfdf', 'df3423', 'dfdf', '2021-10-19', '0.00', '343232.34', 'dfdg', 'user');

-- --------------------------------------------------------

--
-- Table structure for table `userstudent`
--

CREATE TABLE `userstudent` (
  `sNo` int(100) NOT NULL,
  `username` varchar(30) NOT NULL,
  `password` varchar(255) NOT NULL,
  `firstName` varchar(20) NOT NULL,
  `middleName` varchar(20) NOT NULL,
  `lastName` varchar(20) NOT NULL,
  `fatherName` varchar(30) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `dateOfBirth` date DEFAULT NULL,
  `birthPlace` varchar(20) NOT NULL,
  `mobileNo` int(15) NOT NULL,
  `email` varchar(30) NOT NULL,
  `motherName` varchar(20) NOT NULL,
  `admNo` varchar(10) NOT NULL,
  `pinCode` varchar(15) NOT NULL,
  `houseNo` varchar(10) NOT NULL,
  `address` varchar(30) NOT NULL,
  `city` varchar(30) NOT NULL,
  `state` varchar(30) NOT NULL,
  `category` varchar(20) NOT NULL,
  `admDate` date DEFAULT NULL,
  `bloodGroup` varchar(5) NOT NULL,
  `religion` varchar(20) NOT NULL,
  `nationality` varchar(20) NOT NULL,
  `fatherOccupation` varchar(30) NOT NULL,
  `height` int(10) NOT NULL,
  `weight` int(10) NOT NULL,
  `nationalIDno` varchar(30) NOT NULL,
  `dateTime` datetime NOT NULL DEFAULT current_timestamp(),
  `teacherId` int(100) NOT NULL,
  `photo` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `userstudent`
--

INSERT INTO `userstudent` (`sNo`, `username`, `password`, `firstName`, `middleName`, `lastName`, `fatherName`, `gender`, `dateOfBirth`, `birthPlace`, `mobileNo`, `email`, `motherName`, `admNo`, `pinCode`, `houseNo`, `address`, `city`, `state`, `category`, `admDate`, `bloodGroup`, `religion`, `nationality`, `fatherOccupation`, `height`, `weight`, `nationalIDno`, `dateTime`, `teacherId`, `photo`) VALUES
(1, 'satvik2021', '111111', 'satvik', '', 'sharma', 'dfdk', 'Male', '2021-10-12', 'kjkjfsd', 25475125, 'kfjdkf@gmail.com', 'mokdjf', 'd525', '546456', 'd5145', 'jhdjfhjmdv djfnd', 'meerut', 'whatssd df', 'General', '2021-10-14', 'jhjg', 'hindu', 'indian', 'service', 23, 14, 'sd524521', '2021-10-19 21:36:29', 23, 'dvdv.jpg'),
(3, 'cvs2021', '111111', 'cvs', '', 'cbvbs', 'cvcbd', 'Male', '2021-10-12', 'fcgfd', 454353, 'fgfdgd@gmail.com', 'fdgdfgd', 'fg443', '4353', '4353', 'ff fgfhgd', 'dfgfd', 'dfgsdfd', 'General', '2021-10-11', 'ab', 'sffg fgd', 'fgfgdd', 'dfgfdgd', 44, 46, 'fgdf4454', '2021-10-19 22:58:56', 22, 'satvk.jpg'),
(4, 'yash2021', '111111', 'yash', 'df', 'sdfg', 'dfdg', 'Male', '2021-10-13', 'dfdfg', 34545, 'dfgsd', 'sddg', 'df34', '2343', 'sd34', 'sddg fgfg', 'dfsdf', 'sdffg', 'General', '2021-10-21', 'Ab', 'dfd', 'indian', '', 0, 0, '', '2021-10-19 23:33:08', 23, 'satvik.jpg');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `useradmin`
--
ALTER TABLE `useradmin`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `userstudent`
--
ALTER TABLE `userstudent`
  ADD PRIMARY KEY (`sNo`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `useradmin`
--
ALTER TABLE `useradmin`
  MODIFY `sno` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- AUTO_INCREMENT for table `userstudent`
--
ALTER TABLE `userstudent`
  MODIFY `sNo` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
