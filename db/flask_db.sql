-- phpMyAdmin SQL Dump
-- version 4.9.5deb2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: May 24, 2023 at 04:57 PM
-- Server version: 8.0.33-0ubuntu0.20.04.2
-- PHP Version: 8.2.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `flask_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `user_details`
--

CREATE TABLE `user_details` (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `profile_img` varchar(50) DEFAULT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `is_admin` tinyint(1) DEFAULT '0',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `user_details`
--

INSERT INTO `user_details` (`id`, `name`, `profile_img`, `email`, `password`, `is_admin`, `created_at`) VALUES
(1, 'Sayan Maji', NULL, 'sayanmaji12@gmail.com', 'e10adc3949ba59abbe56e057f20f883e', 1, '2023-05-10 10:10:22'),
(2, 'Sayan', '1684947206.jpeg', 'sayan@quantumgrowth.ai', 'e10adc3949ba59abbe56e057f20f883e', 0, '2023-05-24 16:45:44');

-- --------------------------------------------------------

--
-- Table structure for table `user_otp`
--

CREATE TABLE `user_otp` (
  `id` int NOT NULL,
  `user_id` int NOT NULL,
  `otp` int NOT NULL,
  `isactive` tinyint(1) NOT NULL DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `user_otp`
--

INSERT INTO `user_otp` (`id`, `user_id`, `otp`, `isactive`) VALUES
(1, 2, 5719, 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `user_details`
--
ALTER TABLE `user_details`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user_otp`
--
ALTER TABLE `user_otp`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `user_details`
--
ALTER TABLE `user_details`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `user_otp`
--
ALTER TABLE `user_otp`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
