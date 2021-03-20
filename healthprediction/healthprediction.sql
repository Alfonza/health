-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 19, 2021 at 05:33 AM
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
(3, 'nerin', 'nerin@gmail.com', '123', '67356832', 'skin'),
(4, 'saho', 'saho@gmail.com', '222', '67586387382', 'mental'),
(16, 'akz', 'akz@gmail.com', '234', '63582358', 'cardiac'),
(17, 'Lal', 'lal@gmail.com', '345', '8989786217', 'dental'),
(18, 'ashwin', 'ashwin@gmail.com', '456', '9828358', 'mental'),
(19, 'danu', 'danu@gmail.com', '567', '2432547', 'neuro'),
(20, 'sanal', 'sanal@gmail.com', '777', '9897867', 'neuro');

-- --------------------------------------------------------

--
-- Table structure for table `health_feedbacks`
--

CREATE TABLE `health_feedbacks` (
  `id` int(11) NOT NULL,
  `feedbackmsg` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `health_feedbacks`
--

INSERT INTO `health_feedbacks` (`id`, `feedbackmsg`) VALUES
(2, 'nice application'),
(4, 'nice');

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

--
-- Dumping data for table `health_messages`
--

INSERT INTO `health_messages` (`id`, `doctorid`, `patientid`, `message`, `replay`) VALUES
(30, 3, 11, 'can i use paracetamole', 'you can use'),
(31, 3, 11, 'cold water is good or bad in this time', NULL),
(32, 4, 11, 'can i use vomiting tablet', NULL),
(33, 17, 11, 'what medicine i can take for alergy', NULL),
(34, 17, 11, 'what do for preventing cough', NULL),
(41, 20, 11, 'what i do', NULL),
(42, 18, 11, 'helloooooo', NULL),
(43, 18, 11, 'how r u', NULL),
(60, 16, 11, 'jkjk', NULL),
(61, 17, 11, 'jkhjk', NULL),
(62, 17, 11, 'saaa', NULL),
(63, 18, 11, 'aaa', NULL),
(64, 18, 11, 'llll', NULL),
(65, 3, 11, 'haiii', NULL),
(66, 4, 11, 'kjk', NULL),
(67, 20, 11, 'haiiii', NULL),
(68, 19, 11, 'kaaaa', NULL),
(69, 20, 11, 'hhhh', NULL),
(70, 20, 11, 'jkhjkhjk', NULL),
(71, 20, 11, 'bjhk', NULL),
(72, 20, 11, 'bjhjahdk', NULL),
(73, 17, 11, 'jhkjkj', NULL),
(74, 18, 11, 'mmmm', NULL),
(75, 17, 11, 'vvnb', NULL),
(76, 16, 11, 'njhk', NULL),
(77, 16, 11, 'khjkhk', NULL),
(78, 17, 11, 'bhjjkjl', NULL),
(79, 20, 11, 'jjjj', NULL),
(80, 17, 11, 'hkjl', NULL),
(81, 18, 11, 'khkj', NULL),
(82, 19, 11, 'kjkj', NULL),
(83, 19, 11, 'hjk', NULL);

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
-- Dumping data for table `health_patients`
--

INSERT INTO `health_patients` (`id`, `name`, `email`, `password`, `phonenum`, `status`) VALUES
(1, 'alfonsa', 'alfonsa@gmail.com', '121', '8086439586', 'Take rest'),
(5, 'manu', 'manu@gmail.com', '999', '7564535436', NULL),
(6, 'albin', 'albin@gmail.com', '777', '34657798098', NULL),
(9, 'sumesh', 'sumesh@gmail.com', '333', '354365757', 'immediatly consult doctor'),
(10, 'ram', 'ram@gamil.com', '900', '87867564', 'consult doctor'),
(11, 'naina', 'naina@gmail.com', '123', '65387594', 'immediatly consult doctor'),
(13, 'anu', 'anu@gmail.com', '999', '98975645', 'take rest');

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `health_feedbacks`
--
ALTER TABLE `health_feedbacks`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `health_messages`
--
ALTER TABLE `health_messages`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=84;

--
-- AUTO_INCREMENT for table `health_patients`
--
ALTER TABLE `health_patients`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
