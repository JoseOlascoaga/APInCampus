-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 27-05-2022 a las 23:50:28
-- Versión del servidor: 10.4.24-MariaDB
-- Versión de PHP: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `ncampus`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `asignaturas`
--

CREATE TABLE `asignaturas` (
  `idAsignatura` int(11) NOT NULL,
  `nombreAsig` varchar(30) NOT NULL,
  `jornada` varchar(30) NOT NULL,
  `idProaca` int(11) NOT NULL,
  `idEstu` int(11) NOT NULL,
  `idProfe` int(11) NOT NULL,
  `idSemes` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `asistencias`
--

CREATE TABLE `asistencias` (
  `idAsistencia` int(11) NOT NULL,
  `asistencia` int(1) NOT NULL,
  `fecha` date NOT NULL,
  `idProfe` int(11) NOT NULL,
  `idEstu` int(11) NOT NULL,
  `idAsign` int(11) NOT NULL,
  `idSemes` int(11) NOT NULL,
  `idCurs` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cursos`
--

CREATE TABLE `cursos` (
  `idCurso` int(11) NOT NULL,
  `numCurso` int(11) NOT NULL,
  `idEstu` int(11) NOT NULL,
  `idProfe` int(11) NOT NULL,
  `idMatric` int(11) NOT NULL,
  `idSemes` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detallematricula`
--

CREATE TABLE `detallematricula` (
  `idDetalle` int(11) NOT NULL,
  `vlrMatricula` int(11) NOT NULL,
  `idMatric` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estudiante`
--

CREATE TABLE `estudiante` (
  `IdEstudiante` int(11) NOT NULL,
  `identificacion` int(10) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `apellido` varchar(30) NOT NULL,
  `IdProfe` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `matriculas`
--

CREATE TABLE `matriculas` (
  `idMatricula` int(11) NOT NULL,
  `idEstu` int(11) NOT NULL,
  `idSemes` int(11) NOT NULL,
  `idAsign` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `notas`
--

CREATE TABLE `notas` (
  `idNota` int(11) NOT NULL,
  `corteuno` double NOT NULL,
  `cortedos` double NOT NULL,
  `cortetres` double NOT NULL,
  `promedio` double NOT NULL,
  `proGeneral` double NOT NULL,
  `idEstu` int(11) NOT NULL,
  `idProfe` int(11) NOT NULL,
  `idProaca` int(11) NOT NULL,
  `idSemes` int(11) NOT NULL,
  `idAsign` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proacad`
--

CREATE TABLE `proacad` (
  `idProacad` int(11) NOT NULL,
  `nomProacad` int(11) NOT NULL,
  `idEstu` int(11) NOT NULL,
  `idSemes` int(11) NOT NULL,
  `idProfe` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `profesores`
--

CREATE TABLE `profesores` (
  `IdProfesores` int(11) NOT NULL,
  `identificacion` int(11) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `apellido` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `semestres`
--

CREATE TABLE `semestres` (
  `idSemestre` int(11) NOT NULL,
  `semestre` int(11) NOT NULL,
  `idEstu` int(11) NOT NULL,
  `idProfe` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `asignaturas`
--
ALTER TABLE `asignaturas`
  ADD PRIMARY KEY (`idAsignatura`),
  ADD KEY `idProaca` (`idProaca`),
  ADD KEY `idEstu` (`idEstu`),
  ADD KEY `idProfe` (`idProfe`),
  ADD KEY `idSemes` (`idSemes`);

--
-- Indices de la tabla `asistencias`
--
ALTER TABLE `asistencias`
  ADD PRIMARY KEY (`idAsistencia`),
  ADD KEY `idProfe` (`idProfe`),
  ADD KEY `idEstu` (`idEstu`),
  ADD KEY `idAsign` (`idAsign`),
  ADD KEY `idSemes` (`idSemes`),
  ADD KEY `idCurs` (`idCurs`);

--
-- Indices de la tabla `cursos`
--
ALTER TABLE `cursos`
  ADD PRIMARY KEY (`idCurso`),
  ADD KEY `idEstu` (`idEstu`),
  ADD KEY `idProfe` (`idProfe`),
  ADD KEY `idMatric` (`idMatric`),
  ADD KEY `idSemes` (`idSemes`);

--
-- Indices de la tabla `detallematricula`
--
ALTER TABLE `detallematricula`
  ADD PRIMARY KEY (`idDetalle`),
  ADD KEY `idMatric` (`idMatric`);

--
-- Indices de la tabla `estudiante`
--
ALTER TABLE `estudiante`
  ADD PRIMARY KEY (`IdEstudiante`),
  ADD UNIQUE KEY `identificacion` (`identificacion`),
  ADD KEY `IdProfe` (`IdProfe`);

--
-- Indices de la tabla `matriculas`
--
ALTER TABLE `matriculas`
  ADD PRIMARY KEY (`idMatricula`),
  ADD KEY `idEstu` (`idEstu`),
  ADD KEY `idSemes` (`idSemes`),
  ADD KEY `idAsign` (`idAsign`);

--
-- Indices de la tabla `notas`
--
ALTER TABLE `notas`
  ADD PRIMARY KEY (`idNota`),
  ADD KEY `idEstu` (`idEstu`),
  ADD KEY `idProfe` (`idProfe`),
  ADD KEY `idProaca` (`idProaca`),
  ADD KEY `idSemes` (`idSemes`),
  ADD KEY `idAsign` (`idAsign`);

--
-- Indices de la tabla `proacad`
--
ALTER TABLE `proacad`
  ADD PRIMARY KEY (`idProacad`),
  ADD KEY `idEstu` (`idEstu`),
  ADD KEY `idSemes` (`idSemes`),
  ADD KEY `idProfe` (`idProfe`);

--
-- Indices de la tabla `profesores`
--
ALTER TABLE `profesores`
  ADD PRIMARY KEY (`IdProfesores`),
  ADD UNIQUE KEY `identificacion` (`identificacion`);

--
-- Indices de la tabla `semestres`
--
ALTER TABLE `semestres`
  ADD PRIMARY KEY (`idSemestre`),
  ADD KEY `idEstu` (`idEstu`),
  ADD KEY `idProfe` (`idProfe`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `asignaturas`
--
ALTER TABLE `asignaturas`
  MODIFY `idAsignatura` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `asistencias`
--
ALTER TABLE `asistencias`
  MODIFY `idAsistencia` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `cursos`
--
ALTER TABLE `cursos`
  MODIFY `idCurso` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `detallematricula`
--
ALTER TABLE `detallematricula`
  MODIFY `idDetalle` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `estudiante`
--
ALTER TABLE `estudiante`
  MODIFY `IdEstudiante` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `matriculas`
--
ALTER TABLE `matriculas`
  MODIFY `idMatricula` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `notas`
--
ALTER TABLE `notas`
  MODIFY `idNota` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `proacad`
--
ALTER TABLE `proacad`
  MODIFY `idProacad` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `profesores`
--
ALTER TABLE `profesores`
  MODIFY `IdProfesores` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `semestres`
--
ALTER TABLE `semestres`
  MODIFY `idSemestre` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `asignaturas`
--
ALTER TABLE `asignaturas`
  ADD CONSTRAINT `asignaturas_ibfk_1` FOREIGN KEY (`idEstu`) REFERENCES `estudiante` (`IdEstudiante`) ON UPDATE CASCADE,
  ADD CONSTRAINT `asignaturas_ibfk_2` FOREIGN KEY (`idProfe`) REFERENCES `profesores` (`IdProfesores`) ON UPDATE CASCADE,
  ADD CONSTRAINT `asignaturas_ibfk_3` FOREIGN KEY (`idSemes`) REFERENCES `semestres` (`idSemestre`) ON UPDATE CASCADE,
  ADD CONSTRAINT `asignaturas_ibfk_4` FOREIGN KEY (`idProaca`) REFERENCES `proacad` (`idProacad`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `asistencias`
--
ALTER TABLE `asistencias`
  ADD CONSTRAINT `asistencias_ibfk_1` FOREIGN KEY (`idCurs`) REFERENCES `cursos` (`idCurso`) ON UPDATE CASCADE,
  ADD CONSTRAINT `asistencias_ibfk_2` FOREIGN KEY (`idEstu`) REFERENCES `estudiante` (`IdEstudiante`) ON UPDATE CASCADE,
  ADD CONSTRAINT `asistencias_ibfk_3` FOREIGN KEY (`idAsign`) REFERENCES `asignaturas` (`idAsignatura`) ON UPDATE CASCADE,
  ADD CONSTRAINT `asistencias_ibfk_4` FOREIGN KEY (`idSemes`) REFERENCES `semestres` (`idSemestre`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `cursos`
--
ALTER TABLE `cursos`
  ADD CONSTRAINT `cursos_ibfk_1` FOREIGN KEY (`idSemes`) REFERENCES `semestres` (`idSemestre`) ON UPDATE CASCADE,
  ADD CONSTRAINT `cursos_ibfk_2` FOREIGN KEY (`idEstu`) REFERENCES `estudiante` (`IdEstudiante`) ON UPDATE CASCADE,
  ADD CONSTRAINT `cursos_ibfk_3` FOREIGN KEY (`idProfe`) REFERENCES `profesores` (`IdProfesores`) ON UPDATE CASCADE,
  ADD CONSTRAINT `cursos_ibfk_4` FOREIGN KEY (`idMatric`) REFERENCES `matriculas` (`idMatricula`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `detallematricula`
--
ALTER TABLE `detallematricula`
  ADD CONSTRAINT `detallematricula_ibfk_1` FOREIGN KEY (`idMatric`) REFERENCES `matriculas` (`idMatricula`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `estudiante`
--
ALTER TABLE `estudiante`
  ADD CONSTRAINT `estudiante_ibfk_1` FOREIGN KEY (`IdProfe`) REFERENCES `profesores` (`IdProfesores`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `matriculas`
--
ALTER TABLE `matriculas`
  ADD CONSTRAINT `matriculas_ibfk_1` FOREIGN KEY (`idSemes`) REFERENCES `semestres` (`idSemestre`) ON UPDATE CASCADE,
  ADD CONSTRAINT `matriculas_ibfk_2` FOREIGN KEY (`idAsign`) REFERENCES `asignaturas` (`idAsignatura`) ON UPDATE CASCADE,
  ADD CONSTRAINT `matriculas_ibfk_3` FOREIGN KEY (`idEstu`) REFERENCES `estudiante` (`IdEstudiante`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `notas`
--
ALTER TABLE `notas`
  ADD CONSTRAINT `notas_ibfk_1` FOREIGN KEY (`idProfe`) REFERENCES `profesores` (`IdProfesores`) ON UPDATE CASCADE,
  ADD CONSTRAINT `notas_ibfk_2` FOREIGN KEY (`idSemes`) REFERENCES `semestres` (`idSemestre`) ON UPDATE CASCADE,
  ADD CONSTRAINT `notas_ibfk_3` FOREIGN KEY (`idProaca`) REFERENCES `proacad` (`idProacad`) ON UPDATE CASCADE,
  ADD CONSTRAINT `notas_ibfk_4` FOREIGN KEY (`idEstu`) REFERENCES `estudiante` (`IdEstudiante`) ON UPDATE CASCADE,
  ADD CONSTRAINT `notas_ibfk_5` FOREIGN KEY (`idAsign`) REFERENCES `asignaturas` (`idAsignatura`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `proacad`
--
ALTER TABLE `proacad`
  ADD CONSTRAINT `proacad_ibfk_1` FOREIGN KEY (`idEstu`) REFERENCES `estudiante` (`IdEstudiante`) ON UPDATE CASCADE,
  ADD CONSTRAINT `proacad_ibfk_2` FOREIGN KEY (`idProfe`) REFERENCES `profesores` (`IdProfesores`) ON UPDATE CASCADE,
  ADD CONSTRAINT `proacad_ibfk_3` FOREIGN KEY (`idSemes`) REFERENCES `semestres` (`idSemestre`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `semestres`
--
ALTER TABLE `semestres`
  ADD CONSTRAINT `semestres_ibfk_1` FOREIGN KEY (`idEstu`) REFERENCES `estudiante` (`IdEstudiante`) ON UPDATE CASCADE,
  ADD CONSTRAINT `semestres_ibfk_2` FOREIGN KEY (`idProfe`) REFERENCES `profesores` (`IdProfesores`) ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
