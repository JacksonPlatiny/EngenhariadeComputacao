-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 12-Out-2021 às 23:51
-- Versão do servidor: 10.4.20-MariaDB
-- versão do PHP: 8.0.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `escola_de_musica`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `apresenta`
--

CREATE TABLE `apresenta` (
  `Codigo` int(11) NOT NULL,
  `fk_sinfonia_codigo` int(11) NOT NULL,
  `fk_musico_matricula` int(11) NOT NULL,
  `InstrumentoUtilizado` varchar(50) NOT NULL,
  `DataApresentacao` date NOT NULL,
  `FuncaoEspecifica` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `apresenta`
--

INSERT INTO `apresenta` (`Codigo`, `fk_sinfonia_codigo`, `fk_musico_matricula`, `InstrumentoUtilizado`, `DataApresentacao`, `FuncaoEspecifica`) VALUES
(125001, 10001, 4002, 'Bastão', '2022-01-03', 'Maestro'),
(125002, 10005, 4002, 'Bastão', '2022-02-06', 'Maestro'),
(125003, 10010, 5001, 'Bastão', '2022-03-09', 'Maestro'),
(125004, 10015, 5001, 'Bastão', '2022-04-12', 'Maestro'),
(125005, 10020, 3003, 'Bastão', '2022-05-15', 'Maestro'),
(125006, 10019, 3003, 'Bastão', '2022-06-18', 'Maestro'),
(125007, 10017, 6006, 'Bastão', '2022-07-21', 'Maestro'),
(125008, 10003, 6006, 'Bastão', '2022-08-24', 'Maestro'),
(125009, 10004, 7024, 'Bastão', '2022-09-27', 'Maestro'),
(125010, 10002, 7024, 'Bastão', '2022-10-29', 'Maestro');

-- --------------------------------------------------------

--
-- Estrutura da tabela `executa`
--

CREATE TABLE `executa` (
  `Codigo` int(11) NOT NULL,
  `fk_sinfonia_codigo` int(11) NOT NULL,
  `fk_orquestra_codigo` int(11) NOT NULL,
  `DataExecucao` date NOT NULL,
  `Desempenho` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `executa`
--

INSERT INTO `executa` (`Codigo`, `fk_sinfonia_codigo`, `fk_orquestra_codigo`, `DataExecucao`, `Desempenho`) VALUES
(501, 10001, 2021001, '2021-02-25', 72),
(502, 10002, 2021001, '2018-07-12', 66),
(503, 10003, 2021001, '2015-03-19', 87),
(504, 10004, 2021001, '2001-01-16', 42),
(505, 10005, 2021001, '1988-07-30', 60),
(506, 10006, 2021001, '1999-08-01', 100),
(507, 10005, 2021002, '2011-01-01', 75),
(508, 10018, 2021002, '1900-01-02', 42),
(509, 10013, 2021002, '1925-01-03', 98),
(510, 10005, 2021002, '1930-01-04', 99),
(511, 10014, 2021002, '1988-02-05', 63),
(512, 10012, 2021002, '1955-06-08', 85),
(513, 10017, 2021002, '1890-04-05', 77),
(514, 10020, 2021002, '2001-02-02', 85),
(515, 10010, 2021003, '2015-05-04', 70),
(516, 10017, 2021003, '2010-01-01', 74),
(517, 10018, 2021003, '2012-12-20', 52),
(518, 10019, 2021003, '2018-04-12', 88),
(519, 10020, 2021003, '2014-01-01', 92),
(520, 10007, 2021004, '2000-01-01', 41),
(521, 10008, 2021004, '2019-02-01', 85),
(522, 10009, 2021004, '2003-05-17', 20),
(523, 10011, 2021004, '2002-06-24', 45),
(524, 10013, 2021004, '2014-02-03', 74),
(525, 10009, 2021006, '2020-01-30', 74),
(526, 10010, 2021006, '2012-02-28', 58),
(527, 10011, 2021006, '2005-08-30', 45),
(528, 10012, 2021006, '2014-04-30', 68),
(529, 10013, 2021006, '2021-06-30', 75);

-- --------------------------------------------------------

--
-- Estrutura da tabela `instrumentos`
--

CREATE TABLE `instrumentos` (
  `Codigo` int(11) NOT NULL,
  `Nome` varchar(30) NOT NULL,
  `Classificacao` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `instrumentos`
--

INSERT INTO `instrumentos` (`Codigo`, `Nome`, `Classificacao`) VALUES
(4001, 'Violino', 'Cordas'),
(4002, 'Viola', 'Cordas'),
(4003, 'Violoncelo', 'Cordas'),
(4004, 'Contrabaixo', 'Cordas'),
(4005, 'Harpa', 'Cordas'),
(4006, 'Flauta', 'Madeiras'),
(4007, 'Flautim', 'Madeiras'),
(4008, 'Oboé', 'Madeiras'),
(4009, 'Corne-inglês', 'Madeiras'),
(4010, 'Clarinete', 'Madeiras'),
(4011, 'Clarinete baixo', 'Madeiras'),
(4012, 'Fagote', 'Madeiras'),
(4013, 'Contrafagote', 'Madeiras'),
(4014, 'Trompete', 'Metais'),
(4015, 'Trombone', 'Metais'),
(4016, 'Trompa', 'Metais'),
(4017, 'Tuba', 'Metais'),
(4018, 'Tímpano', 'Percussão'),
(4019, 'Triangulo', 'Percussão'),
(4020, 'Caixa', 'Percussão'),
(4021, 'Bombo', 'Percussão'),
(4022, 'Prato', 'Percussão'),
(4023, 'Carrilhão sinfônico', 'Percussão'),
(4024, 'Piano', 'Teclas'),
(4025, 'Cravo', 'Teclas'),
(4026, 'Órgão', 'Teclas');

-- --------------------------------------------------------

--
-- Estrutura da tabela `musico`
--

CREATE TABLE `musico` (
  `Matricula` int(11) NOT NULL,
  `Nome` varchar(50) NOT NULL,
  `Snome` varchar(100) NOT NULL,
  `RG` int(11) NOT NULL,
  `Nacionalidade` varchar(50) NOT NULL,
  `DataNascimento` date NOT NULL,
  `FuncaoTradicional` varchar(50) NOT NULL,
  `fk_orquestra_codigo` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `musico`
--

INSERT INTO `musico` (`Matricula`, `Nome`, `Snome`, `RG`, `Nacionalidade`, `DataNascimento`, `FuncaoTradicional`, `fk_orquestra_codigo`) VALUES
(3000, 'Regina', 'Santos', 8856320, 'Brasileira', '1978-02-07', 'Harpista', 2021001),
(3001, 'Maria', 'Cruz', 6208335, 'Brasileira', '1985-04-21', 'Violinista', 2021001),
(3002, 'Beatriz', 'Oliveira', 3335261, 'Brasileira', '1987-03-01', 'Flautista', 2021001),
(3003, 'João', 'Silva', 3525261, 'Brasileira', '1987-03-01', 'Flautista', 2021001),
(3004, 'Lucas', 'Lins', 3698524, 'Brasileira', '1986-01-10', 'Contrafagotista', 2021001),
(3005, 'Suzana', 'Roque', 9631523, 'Brasileira', '2000-08-09', 'Fagotista', 2021001),
(3006, 'Pedro', 'Carvalho', 6398521, 'Brasileira', '1989-07-24', 'Trompetista', 2021001),
(3007, 'Mateus', 'Santos', 9865232, 'Brasileira', '1990-07-24', 'Harpista', 2021001),
(3008, 'José', 'Vieira', 8657200, 'Brasileira', '1989-04-24', 'Pianista', 2021001),
(3009, 'Pietra', 'Leite', 2031456, 'Brasileira', '1983-06-07', 'Cravista', 2021001),
(3010, 'Ana', 'Alves', 3698520, 'Brasileira', '1978-11-25', 'Trompista', 2021001),
(3011, 'Lucia', 'Andrade', 6851235, 'Brasileira', '1979-12-21', 'Trombonista', 2021001),
(3012, 'Theobaldo', 'Moura', 9875621, 'Brasileira', '1978-11-28', 'Clarinetista', 2021001),
(3013, 'Felipo', 'Krass', 3574123, 'Brasileira', '1980-04-21', 'Clarinetista', 2021001),
(3014, 'Felippe', 'Lions', 6532014, 'Brasileira', '1975-06-12', 'Tamborista', 2021001),
(3015, 'Cristovao', 'Dantas', 21533, 'Brasileira', '2000-01-23', 'Violista', 2021001),
(3016, 'Assis', 'Silva', 8657123, 'Brasileira', '1978-08-07', 'Violista', 2021001),
(3017, 'Thiago', 'Lima', 3012458, 'Brasileira', '1974-02-01', 'Oboísta', 2021001),
(3018, 'José', 'Patrício', 6985220, 'Brasileira', '1987-05-03', 'Contrabaixista', 2021001),
(3019, 'Jacó', 'Baggio', 8753692, 'Brasileira', '2002-06-07', 'Violoncelista', 2021001),
(3020, 'Luiz', 'Costa', 3698520, 'Brasileira', '1989-02-04', 'Violoncelista', 2021001),
(3021, 'Flora', 'Rocha', 2013015, 'Brasileira', '2001-07-01', 'Violoncelista', 2021001),
(3022, 'Cora', 'Estevan', 6374154, 'Brasileira', '1987-04-08', 'Flautista', 2021001),
(3023, 'Alana', 'Piccolo', 5874122, 'Brasileira', '1977-06-08', 'Cornerista', 2021001),
(3024, 'Olivia', 'Cabral', 7858522, 'Brasileira', '1972-06-08', 'Fagotista', 2021001),
(3025, 'Ivan', 'Pedro', 3697412, 'Brasileira', '1986-06-08', 'Cravista', 2021001),
(3026, 'Nilton', 'Silva', 9874563, 'Brasileira', '1982-06-08', 'Contrafagotista', 2021001),
(3027, 'Maria', 'Ribeiro', 4587130, 'Brasileira', '2000-10-05', 'Violinista', 2021001),
(3028, 'Ubaldo', 'Cristovao', 8756321, 'Brasileira', '1970-10-05', 'Trompetista', 2021001),
(3029, 'Diego', 'Pereira', 4203162, 'Brasileira', '1980-10-05', 'Violinista', 2021001),
(4000, 'Harper', 'Taylor', 2340789, 'Austriaca', '1980-10-05', 'Trompetista', 2021002),
(4001, 'Charlie', 'Smith', 9687456, 'Austriaca', '1981-10-05', 'Violinista', 2021002),
(4002, 'Hunter', 'Jades', 7034123, 'Austriaca', '1982-10-05', 'Contrafagotista', 2021002),
(4003, 'Aria', 'Taylor', 2438079, 'Austriaca', '1983-10-05', 'Flautista', 2021002),
(4004, 'Harlow', 'Sminth', 3172745, 'Austriaca', '1984-10-05', 'Cornerista', 2021002),
(4005, 'Riley', 'Jades', 3907412, 'Austriaca', '1985-10-05', 'Fagotista', 2021002),
(4006, 'Leo', 'Taylor', 4642079, 'Austriaca', '1986-10-05', 'Cravista', 2021002),
(4007, 'Frankie', 'Sminth', 5376745, 'Austriaca', '1987-10-05', 'Trompetista', 2021002),
(4008, 'Ollie', 'Sades', 6111412, 'Austriaca', '1988-10-05', 'Violinista', 2021002),
(4009, 'Luca', 'McCarter', 6846792, 'Austriaca', '1989-10-05', 'Contrafagotista', 2021002),
(4010, 'Logan', 'Sminth', 7580745, 'Austriaca', '1990-10-05', 'Flautista', 2021002),
(4011, 'Evelyn', 'Jades', 8315412, 'Austriaca', '1991-10-05', 'Cornerista', 2021002),
(4012, 'Parker', 'Taylor', 9050079, 'Austriaca', '1992-10-05', 'Fagotista', 2021002),
(4013, 'Quinn', 'Sminth', 8044713, 'Austriaca', '1993-10-05', 'Cravista', 2021002),
(4014, 'Darcy', 'Jades', 8353256, 'Austriaca', '1994-10-05', 'Trompetista', 2021002),
(4015, 'Marley', 'Taylor', 8661799, 'Austriaca', '1995-10-05', 'Violinista', 2021002),
(4016, 'Addison', 'Sminth', 8970342, 'Austriaca', '1996-10-05', 'Contrafagotista', 2021002),
(4017, 'River', 'Jades', 9278885, 'Austriaca', '1997-10-05', 'Flautista', 2021002),
(4018, 'Mackenzie', 'Taylor', 9587428, 'Austriaca', '1998-10-05', 'Cornerista', 2021002),
(4019, 'Harley', 'Sminth', 9895971, 'Austriaca', '1999-10-05', 'Fagotista', 2021002),
(4020, 'Bailey', 'Jades', 1020451, 'Austriaca', '2000-10-05', 'Cravista', 2021002),
(4021, 'Blair', 'Taylor', 1051305, 'Austriaca', '2001-10-05', 'Trompetista', 2021002),
(4022, 'Peyton', 'Sminth', 1082159, 'Austriaca', '2002-10-05', 'Violinista', 2021002),
(4023, 'Finley', 'Jades', 1113014, 'Austriaca', '2003-10-05', 'Contrafagotista', 2021002),
(4024, 'Avery', 'Taylor', 1143868, 'Austriaca', '2004-10-05', 'Flautista', 2021002),
(4025, 'Ashton', 'Sminth', 1174722, 'Austriaca', '2005-10-05', 'Cornerista', 2021002),
(4026, 'Eli', 'Jades', 1205577, 'Austriaca', '2006-10-05', 'Fagotista', 2021002),
(4027, 'Eden', 'Taylor', 1236431, 'Austriaca', '2007-10-05', 'Cravista', 2021002),
(4028, 'Aubrey', 'Sminth', 1267285, 'Austriaca', '2008-10-05', 'Trompetista', 2021002),
(4029, 'Jordan', 'Jades', 1298140, 'Austriaca', '2009-10-05', 'Violinista', 2021002),
(4030, 'Halle', 'Taylor', 1328994, 'Austriaca', '2010-10-05', 'Contrafagotista', 2021002),
(5001, 'Dick', 'Cooper', 8856320, 'Americana', '1998-06-11', 'Violinista', 2021003),
(5002, 'Thomasina', 'Mccoy', 6208335, 'Americana', '1998-06-12', 'Cravista', 2021003),
(5003, 'Tommy', 'Macy', 3335261, 'Americana', '1998-06-13', 'Fagotista', 2021003),
(5004, 'Chandler', 'Heath', 5698132, 'Americana', '1998-06-14', 'Contrafagotista', 2021003),
(5005, 'Wilda', 'Mason', 8795461, 'Americana', '1998-06-15', 'Cornerista', 2021003),
(5006, 'Nicole', 'Richardson', 5687451, 'Americana', '1998-06-17', 'Cravista', 2021003),
(5007, 'Queenie', 'Cannon', 2658894, 'Americana', '1998-06-18', 'Cornerista', 2021003),
(5008, 'Jackson', 'Pierpoint', 5623546, 'Americana', '1998-06-22', 'Violinista', 2021003),
(5009, 'Jesse', 'Watson', 2356956, 'Americana', '1998-06-20', 'Contrafagotista', 2021003),
(5010, 'Paisley', 'Cannon', 5647898, 'Americana', '1998-06-21', 'Violinista', 2021003),
(5011, 'Sybil', 'Wheatly', 1234567, 'Americana', '1998-06-22', 'Trompetista', 2021003),
(5012, 'Whitney', 'Massy', 6932587, 'Americana', '1998-06-23', 'Contrafagotista', 2021003),
(5013, 'Alfie', 'Middleton', 2316459, 'Americana', '1998-06-22', 'Violinista', 2021003),
(5014, 'Jade', 'Chavez', 326548, 'Americana', '1999-03-05', 'Cornerista', 2021003),
(5015, 'Andy', 'Barnett', 8521673, 'Americana', '2000-06-12', 'Contrafagotista', 2021003),
(5016, 'Curtis', 'Davidson', 3928175, 'Americana', '1987-03-22', 'Cornerista', 2021003),
(5017, 'Ivy', 'Clem', 6665598, 'Americana', '1978-06-25', 'Cornerista', 2021003),
(5018, 'Melanie', 'Kinsman', 5697465, 'Americana', '1999-06-11', 'Contrafagotista', 2021003),
(5019, 'Barnaby', 'Shortle', 5948620, 'Americana', '1999-06-12', 'Violinista', 2021003),
(5020, 'Jacqueline', 'Banks', 3616668, 'Americana', '1999-06-13', 'Cravista', 2021003),
(5021, 'Egbert', 'Schmidt', 9494796, 'Americana', '1999-06-14', 'Fagotista', 2021003),
(5022, 'Ford', 'Barlow', 3115649, 'Americana', '1999-06-15', 'Violinista', 2021003),
(5023, 'Rosalind', 'Fleming', 2151566, 'Americana', '1999-06-16', 'Contrafagotista', 2021003),
(5024, 'Vince', 'Briggs', 2554156, 'Americana', '1999-06-17', 'Trompetista', 2021003),
(5025, 'Winthrop', 'Goodman', 2333548, 'Americana', '1999-06-18', 'Cornerista', 2021003),
(5026, 'Wayne', 'Pena', 7899456, 'Americana', '1999-06-19', 'Contrafagotista', 2021003),
(5027, 'Hayden', 'Stevens', 5554669, 'Americana', '1999-06-20', 'Violinista', 2021003),
(5028, 'Sibley', 'Cooke', 2233111, 'Americana', '1999-06-21', 'Cornerista', 2021003),
(5029, 'Conrad', 'Richardson', 4448877, 'Americana', '1999-06-22', 'Contrafagotista', 2021003),
(5030, 'Fiona', 'Pierce', 3336622, 'Americana', '1999-06-23', 'Violinista', 2021003),
(6000, 'Aurora', 'Santos', 8856330, 'Brasileira', '1978-02-07', 'Harpista', 2021004),
(6001, 'Maria', 'Cruz', 6208345, 'Brasileira', '1985-04-21', 'Violinista', 2021004),
(6002, 'Bianca', 'Oliveira', 3335262, 'Brasileira', '1989-05-20', 'Violinista', 2021004),
(6003, 'José', 'Silva', 3525271, 'Brasileira', '1987-03-01', 'Flautista', 2021004),
(6004, 'Joseph', 'Lins', 3698525, 'Brasileira', '1986-01-10', 'Contrafagotista', 2021004),
(6005, 'Sueli', 'Roque', 9631530, 'Brasileira', '2000-08-09', 'Fagotista', 2021004),
(6006, 'Pedro', 'Carvalho', 6398525, 'Brasileira', '1989-07-24', 'Trompetista', 2021004),
(6007, 'Mateus', 'Santos', 9865232, 'Brasileira', '1990-07-24', 'Harpista', 2021004),
(6008, 'José', 'Vieira', 8657200, 'Brasileira', '1989-04-24', 'Pianista', 2021004),
(6009, 'Paloma', 'Leite', 2031456, 'Brasileira', '1983-06-07', 'Cravista', 2021004),
(6010, 'Ana', 'Alves', 3698520, 'Brasileira', '1978-11-25', 'Trompista', 2021004),
(6011, 'Lucia', 'Andrade', 6851235, 'Brasileira', '1979-12-11', 'Trombonista', 2021004),
(6012, 'Theobaldo', 'Moura', 9875621, 'Brasileira', '1978-11-18', 'Clarinetista', 2021004),
(6013, 'Felipo', 'Souza', 3574123, 'Brasileira', '1980-04-22', 'Clarinetista', 2021004),
(6014, 'Felipino', 'Luna', 6532014, 'Brasileira', '1975-06-13', 'Tamborista', 2021004),
(6015, 'Cristofer', 'Dantas', 21533, 'Brasileira', '2000-01-23', 'Violista', 2021004),
(6016, 'Aurelio', 'Silva', 8657123, 'Brasileira', '1978-08-07', 'Violista', 2021004),
(6017, 'Tharcio', 'Lima', 3012458, 'Brasileira', '1974-02-01', 'Oboísta', 2021004),
(6018, 'Josino', 'Pires', 6985220, 'Brasileira', '1987-05-03', 'Contrabaixista', 2021004),
(6019, 'Josué', 'Silva', 8753692, 'Brasileira', '2002-06-07', 'Violoncelista', 2021004),
(6020, 'Luiziane', 'Costa', 3698520, 'Brasileira', '1989-02-04', 'Violoncelista', 2021004),
(6021, 'Florinda', 'Rocha', 2013015, 'Brasileira', '2001-07-01', 'Violoncelista', 2021004),
(6022, 'Coralina', 'Cruz', 6374154, 'Brasileira', '1987-04-08', 'Flautista', 2021004),
(6023, 'Amanda', 'Palombo', 5874122, 'Brasileira', '1977-06-08', 'Cornerista', 2021004),
(6024, 'Sofia', 'Cabral', 7858522, 'Brasileira', '1972-06-08', 'Fagotista', 2021004),
(6025, 'Ivan', 'Perazzo', 3697412, 'Brasileira', '1986-06-08', 'Cravista', 2021004),
(6026, 'Natanael', 'Silva', 9874563, 'Brasileira', '1982-06-08', 'Contrafagotista', 2021004),
(6027, 'Mariana', 'Ribeiro', 4587130, 'Brasileira', '2000-10-05', 'Violinista', 2021004),
(6028, 'José', 'Silveira', 8756323, 'Brasileira', '1970-10-05', 'Trompetista', 2021004),
(6029, 'Diego', 'Lima', 4203165, 'Brasileira', '1980-10-05', 'Violinista', 2021004),
(7000, 'Tian', 'Zongying', 9874562, 'Chinesa', '2000-02-01', 'Contrafagotista', 2021006),
(7001, 'Guo', 'Zedong', 6859212, 'Chinesa', '2000-02-02', 'Violinista', 2021006),
(7002, 'Yi', 'Dingxiang', 6985232, 'Chinesa', '2000-02-03', 'Flautista', 2021006),
(7003, 'Zou', 'Shoushan', 6985232, 'Chinesa', '2000-02-04', 'Flautista', 2021006),
(7004, 'Hao', 'Yan', 6985432, 'Chinesa', '2000-02-05', 'Trompetista', 2021006),
(7005, 'Xiang', 'Shenv', 6987452, 'Chinesa', '2000-02-06', 'Fagotista', 2021006),
(7006, 'Fu', 'Zihao', 6982302, 'Chinesa', '2000-02-07', 'Violinista', 2021006),
(7007, 'Qiao', 'Zihao', 6985230, 'Chinesa', '2000-02-08', 'Cornerista', 2021006),
(7008, 'Xie', 'Xueqin', 3520122, 'Chinesa', '2000-02-09', 'Violinista', 2021006),
(7009, 'Yin', 'Changpu', 7412580, 'Chinesa', '2000-02-10', 'Violinista', 2021006),
(7010, 'Pan', 'Lanying', 3692121, 'Chinesa', '2000-02-11', 'Flautista', 2021006),
(7011, 'Mao', 'Guiren', 3659820, 'Chinesa', '2000-02-12', 'Trompetista', 2021006),
(7012, 'Li', 'Fan', 6952302, 'Chinesa', '2000-02-13', 'Violinista', 2021006),
(7013, 'Feng', 'Xiaotong', 6982230, 'Chinesa', '2000-02-14', 'Cornerista', 2021006),
(7014, 'Jin', 'Hun', 3692031, 'Chinesa', '2000-02-15', 'Fagotista', 2021006),
(7015, 'Gao', 'Honghui', 6982356, 'Chinesa', '2000-02-16', 'Cornerista', 2021006),
(7016, 'Yi', 'Kang', 6985230, 'Chinesa', '2000-02-17', 'Trompetista', 2021006),
(7017, 'Dong', 'Xifeng', 6982331, 'Chinesa', '2000-02-18', 'Violinista', 2021006),
(7018, 'Kong', 'Yuanjun', 7410258, 'Chinesa', '2000-02-19', 'Flautista', 2021006),
(7019, 'Xiang', 'Yuanjun', 1024753, 'Chinesa', '2000-02-20', 'Flautista', 2021006),
(7020, 'Zou', 'Meixiu', 3698522, 'Chinesa', '2000-02-21', 'Trompetista', 2021006),
(7021, 'Zhou', 'Tingguang', 3620154, 'Chinesa', '2000-02-22', 'Violinista', 2021006),
(7022, 'Hao', 'Jing', 3659821, 'Chinesa', '2000-02-23', 'Flautista', 2021006),
(7023, 'Xie', 'Daiyu', 6982310, 'Chinesa', '2000-02-24', 'Trompetista', 2021006),
(7024, 'Han', 'Li', 3698200, 'Chinesa', '2000-02-25', 'Trompetista', 2021006),
(7025, 'Dong', 'Qingge', 6985412, 'Chinesa', '2000-02-26', 'Violinista', 2021006),
(7026, 'Xia', 'Donghai', 3698500, 'Chinesa', '2000-02-27', 'Fagotista', 2021006),
(7027, 'Cui', 'Zedong', 3698520, 'Chinesa', '2000-02-28', 'Cravista', 2021006),
(7028, 'Lai', 'Deming', 3698547, 'Chinesa', '2000-02-29', 'Flautista', 2021006),
(7029, 'Yao', 'Yaoting', 9987455, 'Chinesa', '2000-02-28', 'Cravista', 2021006);

-- --------------------------------------------------------

--
-- Estrutura da tabela `orquestra`
--

CREATE TABLE `orquestra` (
  `Codigo` int(11) NOT NULL,
  `Nome` varchar(50) NOT NULL,
  `Cidade` varchar(30) NOT NULL,
  `Pais` varchar(15) NOT NULL,
  `DataCriacao` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `orquestra`
--

INSERT INTO `orquestra` (`Codigo`, `Nome`, `Cidade`, `Pais`, `DataCriacao`) VALUES
(2021001, 'Orquestra Sinfônica Do Estado De São Paulo', 'São Paulo', 'Brasil', '1954-09-13'),
(2021002, 'Vienna Philharmonic', 'Vienna', 'Áustria', '1842-03-28'),
(2021003, 'Chicago Symphony Orchestra', 'Chicago', 'Estados Unidos', '1891-10-16'),
(2021004, 'Amazonas Filarmônica', 'Amazonas', 'Brasil', '1997-09-26'),
(2021006, 'China Philharmonic Orchestra', 'Beijing', 'China', '2000-05-25');

-- --------------------------------------------------------

--
-- Estrutura da tabela `sinfonia`
--

CREATE TABLE `sinfonia` (
  `Codigo` int(11) NOT NULL,
  `Nome` varchar(50) NOT NULL,
  `Compositor` varchar(100) NOT NULL,
  `DataCriacao` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `sinfonia`
--

INSERT INTO `sinfonia` (`Codigo`, `Nome`, `Compositor`, `DataCriacao`) VALUES
(10001, 'Symphony No. 1 in C minor, Op. 68', 'Johannes Brahms', '2021-11-04'),
(10002, 'Suite No. 3 in D major, BWV 1068', 'Johann Sebastian Bach', '1730-05-22'),
(10003, 'Kullervo, Op. 7', 'Jean Sibelius', '1892-04-28'),
(10004, 'Symphony No. 6 in F major, Op. 68', 'Ludwig van Beethoven', '1808-12-22'),
(10005, 'Symphony No. 9 in C major, D 944', 'Franz Schubert', '1829-03-12'),
(10006, 'Symphony in F major, K. Anh. 223/19a', 'Wolfgang Amadeus Mozart', '1765-07-08'),
(10007, 'Symphony in D major \"No. 48\", K. 111+120', 'Wolfgang Amadeus Mozart', '1771-10-10'),
(10008, 'Sonata for Arpeggione and Piano in A minor, D. 821', 'Franz Schubert', '1824-11-05'),
(10009, 'String Quartet No. 14 in D minor, D 810', 'Franz Schubert', '1824-01-22'),
(10010, 'Symphony No. 7 in C major, Op. 105', 'Jean Sibelius', '1924-03-02'),
(10011, 'Symphony No. 1 in C major, Op. 21', 'Ludwig van Beethoven', '1800-04-02'),
(10012, 'Symphony No. 5 in E-flat major, Op. 82', 'Jean Sibelius', '1915-12-08'),
(10013, 'Symphony No. 5 in C minor, Op. 67', 'Ludwig van Beethoven', '1808-12-22'),
(10014, 'Symphony in D major \"No. 50\", K. 161/141a', 'Wolfgang Amadeus Mozart', '1772-01-01'),
(10015, 'Symphony No. 2 in D major, Op. 73', 'Johannes Brahms', '1877-12-30'),
(10016, 'Symphony No. 3 in F major, Op. 90', 'Johannes Brahms', '1883-12-02'),
(10017, 'Suite No. 4 in D major, BWV 1069', 'Johann Sebastian Bach', '1730-07-05'),
(10018, 'Suite No. 1 in C major, BWV 1066', 'Johann Sebastian Bach', '1724-09-17'),
(10019, 'The Symphony No. 29 in A major, K. 201/186a', 'Wolfgang Amadeus Mozart', '1774-04-06'),
(10020, 'Symphony No. 9 in D minor, Op. 125', 'Ludwig van Beethoven', '1824-05-07');

-- --------------------------------------------------------

--
-- Estrutura da tabela `toca`
--

CREATE TABLE `toca` (
  `fk_musico_matricula` int(11) NOT NULL,
  `fk_instrumento_codigo` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `toca`
--

INSERT INTO `toca` (`fk_musico_matricula`, `fk_instrumento_codigo`) VALUES
(3000, 4005),
(3001, 4001),
(3002, 4001),
(3003, 4006),
(3004, 4013),
(3005, 4012),
(3006, 4014),
(3007, 4005),
(3008, 4024),
(3009, 4025),
(3010, 4016),
(3011, 4015),
(3012, 4010),
(3013, 4010),
(3014, 4021),
(3015, 4002),
(3016, 4002),
(3017, 4008),
(3018, 4004),
(3019, 4003),
(3020, 4003),
(3021, 4003),
(3022, 4006),
(3023, 4009),
(3024, 4012),
(3025, 4025),
(3026, 4013),
(3027, 4001),
(3028, 4014),
(3029, 4001),
(4000, 4014),
(4001, 4001),
(4002, 4013),
(4003, 4006),
(4004, 4009),
(4005, 4012),
(4006, 4025),
(4007, 4014),
(4008, 4001),
(4009, 4013),
(4010, 4006),
(4011, 4009),
(4012, 4012),
(4013, 4025),
(4014, 4014),
(4015, 4001),
(4016, 4013),
(4017, 4006),
(4018, 4009),
(4019, 4012),
(4020, 4025),
(4021, 4014),
(4022, 4001),
(4023, 4013),
(4024, 4006),
(4025, 4009),
(4026, 4012),
(4027, 4025),
(4028, 4014),
(4029, 4001),
(4030, 4013),
(5001, 4001),
(5002, 4025),
(5003, 4012),
(5004, 4013),
(5005, 4009),
(5006, 4025),
(5007, 4009),
(5008, 4001),
(5009, 4013),
(5010, 4001),
(5011, 4014),
(5012, 4013),
(5013, 4001),
(5014, 4009),
(5015, 4013),
(5016, 4009),
(5017, 4009),
(5018, 4013),
(5019, 4001),
(5020, 4025),
(5021, 4012),
(5022, 4001),
(5023, 4013),
(5024, 4014),
(5025, 4009),
(5026, 4013),
(5027, 4001),
(5028, 4009),
(5029, 4013),
(5030, 4001),
(6000, 4005),
(6001, 4001),
(6002, 4001),
(6003, 4006),
(6004, 4013),
(6005, 4012),
(6006, 4014),
(6007, 4005),
(6008, 4024),
(6009, 4025),
(6010, 4016),
(6011, 4015),
(6012, 4010),
(6013, 4010),
(6014, 4021),
(6015, 4002),
(6016, 4002),
(6017, 4008),
(6018, 4004),
(6019, 4003),
(6020, 4003),
(6021, 4003),
(6022, 4006),
(6023, 4009),
(6024, 4012),
(6025, 4025),
(6026, 4013),
(6027, 4001),
(6028, 4014),
(6029, 4001),
(7000, 4013),
(7000, 4017),
(7000, 4020),
(7000, 4026),
(7001, 4001),
(7002, 4006),
(7003, 4006),
(7004, 4014),
(7005, 4012),
(7006, 4001),
(7007, 4009),
(7008, 4001),
(7009, 4001),
(7010, 4006),
(7011, 4014),
(7012, 4001),
(7013, 4009),
(7014, 4012),
(7015, 4009),
(7016, 4014),
(7017, 4001),
(7018, 4006),
(7019, 4006),
(7020, 4014),
(7021, 4001),
(7022, 4006),
(7023, 4014),
(7024, 4014),
(7025, 4001),
(7026, 4012),
(7027, 4025),
(7028, 4006),
(7029, 4025);

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `apresenta`
--
ALTER TABLE `apresenta`
  ADD PRIMARY KEY (`Codigo`),
  ADD KEY `fk_sinfonia_codigo` (`fk_sinfonia_codigo`),
  ADD KEY `fk_musico_matricula` (`fk_musico_matricula`);

--
-- Índices para tabela `executa`
--
ALTER TABLE `executa`
  ADD PRIMARY KEY (`Codigo`),
  ADD KEY `fk_sinfonia_codigo` (`fk_sinfonia_codigo`),
  ADD KEY `fk_orquestra_codigo` (`fk_orquestra_codigo`);

--
-- Índices para tabela `instrumentos`
--
ALTER TABLE `instrumentos`
  ADD PRIMARY KEY (`Codigo`);

--
-- Índices para tabela `musico`
--
ALTER TABLE `musico`
  ADD PRIMARY KEY (`Matricula`),
  ADD KEY `fk_orquestra_codigo` (`fk_orquestra_codigo`);

--
-- Índices para tabela `orquestra`
--
ALTER TABLE `orquestra`
  ADD PRIMARY KEY (`Codigo`);

--
-- Índices para tabela `sinfonia`
--
ALTER TABLE `sinfonia`
  ADD PRIMARY KEY (`Codigo`);

--
-- Índices para tabela `toca`
--
ALTER TABLE `toca`
  ADD PRIMARY KEY (`fk_musico_matricula`,`fk_instrumento_codigo`),
  ADD KEY `fk_instrumento_codigo` (`fk_instrumento_codigo`);

--
-- Restrições para despejos de tabelas
--

--
-- Limitadores para a tabela `apresenta`
--
ALTER TABLE `apresenta`
  ADD CONSTRAINT `apresenta_ibfk_1` FOREIGN KEY (`fk_sinfonia_codigo`) REFERENCES `sinfonia` (`Codigo`),
  ADD CONSTRAINT `apresenta_ibfk_2` FOREIGN KEY (`fk_musico_matricula`) REFERENCES `musico` (`Matricula`);

--
-- Limitadores para a tabela `executa`
--
ALTER TABLE `executa`
  ADD CONSTRAINT `executa_ibfk_1` FOREIGN KEY (`fk_sinfonia_codigo`) REFERENCES `sinfonia` (`Codigo`),
  ADD CONSTRAINT `executa_ibfk_2` FOREIGN KEY (`fk_orquestra_codigo`) REFERENCES `orquestra` (`Codigo`);

--
-- Limitadores para a tabela `musico`
--
ALTER TABLE `musico`
  ADD CONSTRAINT `musico_ibfk_1` FOREIGN KEY (`fk_orquestra_codigo`) REFERENCES `orquestra` (`Codigo`);

--
-- Limitadores para a tabela `toca`
--
ALTER TABLE `toca`
  ADD CONSTRAINT `toca_ibfk_1` FOREIGN KEY (`fk_musico_matricula`) REFERENCES `musico` (`Matricula`),
  ADD CONSTRAINT `toca_ibfk_2` FOREIGN KEY (`fk_instrumento_codigo`) REFERENCES `instrumentos` (`Codigo`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
