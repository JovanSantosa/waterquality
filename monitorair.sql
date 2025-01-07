-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 02, 2025 at 08:19 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `monitorair`
--

-- --------------------------------------------------------

--
-- Table structure for table `tb_kualitas_air`
--

CREATE TABLE `tb_kualitas_air` (
  `id` int(11) NOT NULL,
  `pH` float NOT NULL,
  `temperature` float NOT NULL,
  `turbidity` float NOT NULL,
  `conductivity` float NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tb_kualitas_air`
--

INSERT INTO `tb_kualitas_air` (`id`, `pH`, `temperature`, `turbidity`, `conductivity`, `created_at`) VALUES
(15, 6.5, 24, 2.3, 275, '2025-01-01 15:13:07');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tb_kualitas_air`
--
ALTER TABLE `tb_kualitas_air`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tb_kualitas_air`
--
ALTER TABLE `tb_kualitas_air`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
