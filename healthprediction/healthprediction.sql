-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 25, 2021 at 10:13 AM
-- Server version: 10.1.35-MariaDB
-- PHP Version: 7.2.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `healthprediction`
--

-- --------------------------------------------------------

--
-- Table structure for table `health_doctors`
--

CREATE TABLE `health_doctors` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `phonenum` varchar(17) NOT NULL,
  `specialization` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `health_doctors`
--

INSERT INTO `health_doctors` (`id`, `name`, `email`, `password`, `phonenum`, `specialization`) VALUES
(19, 'James', 'james@gmail.com', '123', '9656342369', 'ortho'),
(20, 'Naiju', 'naiju@gmail.com', '900', '8976543260', 'cardiac'),
(21, 'Nerin', 'nerin@gmail.com', '222', '789866756', 'skin'),
(22, 'Naina', 'naina@gmail.com', '121', '799808970', 'dental'),
(23, 'ravi', 'ravi@gmail.com', '800', '878790042', 'mental'),
(24, 'tom', 'tom@gmail.com', '789', '8797906744', 'skin');

-- --------------------------------------------------------

--
-- Table structure for table `health_feedbacks`
--

CREATE TABLE `health_feedbacks` (
  `id` int(11) NOT NULL,
  `feedbackmsg` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `health_messages`
--

CREATE TABLE `health_messages` (
  `id` int(11) NOT NULL,
  `doctorid` int(11) NOT NULL,
  `patientid` int(11) NOT NULL,
  `message` varchar(200) NOT NULL,
  `replay` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `health_patients`
--

CREATE TABLE `health_patients` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `phonenum` varchar(17) NOT NULL,
  `status` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `health_doctors`
--
ALTER TABLE `health_doctors`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `health_feedbacks`
--
ALTER TABLE `health_feedbacks`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `health_messages`
--
ALTER TABLE `health_messages`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `health_patients`
--
ALTER TABLE `health_patients`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `health_doctors`
--
ALTER TABLE `health_doctors`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `health_feedbacks`
--
ALTER TABLE `health_feedbacks`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `health_messages`
--
ALTER TABLE `health_messages`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=99;

--
-- AUTO_INCREMENT for table `health_patients`
--
ALTER TABLE `health_patients`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
