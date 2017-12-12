DROP TABLE IF EXISTS `testtable`;
CREATE TABLE `testtable` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `target` varchar(50) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`),
  UNIQUE KEY `target` (`target`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8;

INSERT INTO `testtable` (`id`, `target`) VALUES
(1, 'test1'), 
(2, 'test2'),
(3, 'test3'),
(4, 'test4');
